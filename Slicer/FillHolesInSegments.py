segmentationNode = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLSegmentationNode')
# set value to the size of the larges cracks in the segment surfaces
maximumHoleSizeMm = 2.0

############
masterVolumeNode = segmentationNode.GetNodeReference(segmentationNode.GetReferenceImageGeometryReferenceRole())

# Create segment editor to get access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
# To show segment editor widget (useful for debugging):
# segmentEditorWidget.show()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()
slicer.mrmlScene.AddNode(segmentEditorNode)
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)

# Visible segments will be processed
inputSegmentIDs = vtk.vtkStringArray()
segmentationNode.GetDisplayNode().GetVisibleSegmentIDs(inputSegmentIDs)

# Create a segment that will contain all vertebrae
allVertebraeSegmentId = segmentationNode.GetSegmentation().AddEmptySegment()
segmentEditorNode.SetOverwriteMode(slicer.vtkMRMLSegmentEditorNode.OverwriteNone)
segmentEditorNode.SetMaskMode(slicer.vtkMRMLSegmentEditorNode.PaintAllowedEverywhere)

# Fill surface cracks in each segment and add to allVertebraeSegment
for index in range(inputSegmentIDs.GetNumberOfValues()):
  segmentID = inputSegmentIDs.GetValue(index)
  segmentEditorWidget.setCurrentSegmentID(segmentID)
  # Grow the segment to fill in surface cracks
  segmentEditorWidget.setActiveEffectByName("Margin")
  effect = segmentEditorWidget.activeEffect()
  effect.setParameter("MarginSizeMm",str(maximumHoleSizeMm))
  effect.self().onApply()
  # Invert the segment
  segmentEditorWidget.setActiveEffectByName("Logical operators")
  effect = segmentEditorWidget.activeEffect()
  effect.setParameter("Operation", "INVERT")
  effect.self().onApply()
  # Remove islands in inverted segment (these are the holes inside the segment)
  segmentEditorWidget.setActiveEffectByName("Islands")
  effect = segmentEditorWidget.activeEffect()
  effect.setParameter("Operation", "KEEP_LARGEST_ISLAND")
  effect.self().onApply()
  # Grow the inverted segment by the same margin as before to restore the original size
  segmentEditorWidget.setActiveEffectByName("Margin")
  effect = segmentEditorWidget.activeEffect()
  effect.self().onApply()
  # Invert the inverted segment (it will contain all the segment without the holes)
  segmentEditorWidget.setActiveEffectByName("Logical operators")
  effect = segmentEditorWidget.activeEffect()
  effect.setParameter("Operation", "INVERT")
  effect.self().onApply()
  # Add it to the allVertebraeSegment
  segmentEditorWidget.setCurrentSegmentID(allVertebraeSegmentId)
  segmentEditorWidget.setActiveEffectByName("Logical operators")
  effect = segmentEditorWidget.activeEffect()
  effect.setParameter("Operation", "UNION")
  effect.setParameter("ModifierSegmentID", segmentID)
  effect.self().onApply()

# Grow from seeds, restricting growth to allVertebrae
segmentationNode.GetDisplayNode().SetSegmentVisibility(allVertebraeSegmentId, False)
segmentEditorNode.SetMaskSegmentID(allVertebraeSegmentId)
segmentEditorNode.SetMaskMode(slicer.vtkMRMLSegmentEditorNode.PaintAllowedInsideSingleSegment)
segmentEditorWidget.setActiveEffectByName("Grow from seeds")
effect = segmentEditorWidget.activeEffect()
effect.self().onPreview()
effect.self().onApply()

# Remove the mask segment
segmentationNode.RemoveSegment(allVertebraeSegmentId)
slicer.mrmlScene.RemoveNode(segmentEditorNode)
del segmentEditorWidget
