# Load dry bone CT of skull into the scene and run this script to automatically segment endocranium

masterVolumeNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLScalarVolumeNode")
smoothingKernelSizeMm = 3.0  # this is used for closing small holes in the se

# Compute bone threshold value automatically
import vtkITK
thresholdCalculator = vtkITK.vtkITKImageThresholdCalculator()
thresholdCalculator.SetInputData(masterVolumeNode.GetImageData())
thresholdCalculator.SetMethodToOtsu()
thresholdCalculator.Update()
boneThresholdValue = thresholdCalculator.GetThreshold()
volumeScalarRange = masterVolumeNode.GetImageData().GetScalarRange()
logging.info("Volume minimum = {0}, maximum = {1}, bone threshold = {2}".format(volumeScalarRange[0], volumeScalarRange[1], boneThresholdValue))
slicer.app.processEvents()

# Create segmentation
slicer.app.processEvents()
segmentationNode = slicer.vtkMRMLSegmentationNode()
slicer.mrmlScene.AddNode(segmentationNode)
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)

# Create segment editor to get access to effects
slicer.app.processEvents()
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
# To show segment editor widget (useful for debugging): segmentEditorWidget.show()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
if not segmentEditorWidget.effectByName("Wrap Solidify"):
    slicer.util.errorDisplay("Please install 'SurfaceWrapSolidify' extension using Extension Manager.")

segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()
slicer.mrmlScene.AddNode(segmentEditorNode)
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)

# Create bone segment by thresholding
slicer.app.processEvents()
boneSegmentID = segmentationNode.GetSegmentation().AddEmptySegment("bone")
segmentEditorNode.SetSelectedSegmentID(boneSegmentID)
segmentEditorWidget.setActiveEffectByName("Threshold")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("MinimumThreshold",str(boneThresholdValue))
effect.setParameter("MaximumThreshold",str(volumeScalarRange[1]))
effect.self().onApply()

# Smooth bone segment (just to reduce solidification computation time)
slicer.app.processEvents()
segmentEditorWidget.setActiveEffectByName("Smoothing")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("SmoothingMethod", "MORPHOLOGICAL_CLOSING")
effect.setParameter("KernelSizeMm", str(smoothingKernelSizeMm))
effect.self().onApply()

# Solidify bone
slicer.app.processEvents()
segmentEditorWidget.setActiveEffectByName("Wrap Solidify")
effect = segmentEditorWidget.activeEffect()
effect.self().onApply()

# Create segment for cavity within bone region using thresholding
slicer.app.processEvents()
segmentEditorNode.SetOverwriteMode(slicer.vtkMRMLSegmentEditorNode.OverwriteNone)
segmentEditorNode.SetMaskMode(slicer.vtkMRMLSegmentEditorNode.PaintAllowedInsideAllSegments)
cavitySegmentID = segmentationNode.GetSegmentation().AddEmptySegment("cavity")
segmentEditorNode.SetSelectedSegmentID(cavitySegmentID)
segmentEditorWidget.setActiveEffectByName("Threshold")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("MinimumThreshold",str(volumeScalarRange[0]))
effect.setParameter("MaximumThreshold",str(boneThresholdValue))
effect.self().onApply()

# Cavity shrink
slicer.app.processEvents()
segmentEditorWidget.setActiveEffectByName("Margin")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("MarginSizeMm", str(-smoothingKernelSizeMm))
effect.self().onApply()

# Find largest cavity
slicer.app.processEvents()
segmentEditorWidget.setActiveEffectByName("Islands")
effect = segmentEditorWidget.activeEffect()
effect.setParameterDefault("Operation", "KEEP_LARGEST_ISLAND")
effect.self().onApply()

# Cavity restore
slicer.app.processEvents()
segmentEditorNode.SetMaskMode(slicer.vtkMRMLSegmentEditorNode.PaintAllowedInsideAllSegments)  # ensure we don't leak into bone
segmentEditorWidget.setActiveEffectByName("Margin")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("MarginSizeMm", str(smoothingKernelSizeMm))
effect.self().onApply()

# Clean up
slicer.mrmlScene.RemoveNode(segmentEditorNode)
segmentEditorWidget = None

# Make segmentation results nicely visible in 3D
segmentationDisplayNode = segmentationNode.GetDisplayNode()
segmentationDisplayNode.SetSegmentOpacity3D(boneSegmentID, 0.4)
