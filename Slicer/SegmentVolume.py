#=========================== SegmentVolume.py ==============================
# 
#     _________  ________     ____    ___  _________  _________  _______
#    /__   ___/ /  _____/    /    |  /  / /__   ___/ /__   ___/ /  ____/
#      /  /    /  / ___     /     | /  /    /  /       /  /    /  /___
#     /  /    |  | |_  |   /  /|  |/  /    /  /       /  /    /  ____/
#  __/  /__   |  \__/  /  /  / |     /  __/  /__     /  /    /  /____
# /_______/    \______/  /__/  |____/  /_______/    /__/    /_______/
#
# Image-Guided Neural Implantation Targeting Extensions
# https://github.com/Phenomenal-Cat/IGNITE
#============================================================================= 


def SegmentCT():

#===== Create segmentation
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)
addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment("skin")

#===== Create segment editor to get access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)

#===== Set thresholding
segmentEditorWidget.setActiveEffectByName("Threshold")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("MinimumThreshold","35")
effect.setParameter("MaximumThreshold","695")
effect.self().onApply()

#=====Apply Smoothing
segmentEditorWidget.setActiveEffectByName("Smoothing")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("SmoothingMethod", "MEDIAN")
effect.setParameter("KernelSizeMm", 11)
effect.self().onApply()

#=====Clean up
segmentEditorWidget = None
slicer.mrmlScene.RemoveNode(segmentEditorNode)

#=====Make segmentation results visible in 3D
segmentationNode.CreateClosedSurfaceRepresentation()

#===== Write to STL file?
#slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsClosedSurfaceRepresentationToFiles("c:/tmp", segmentationNode, None, "STL")
