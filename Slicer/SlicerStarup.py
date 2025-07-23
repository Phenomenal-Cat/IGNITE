

#============= SlicerStartup.py ==================
# Customizes the default SLicer GUI environment:
#	- link views
#	- add orientation markers
#	- add  
#



# Display crosshair at a 3D position

position_RAS 	= [0, 0, 0]
crosshairNode 	= slicer.util.getNode("Crosshair")
# Set crosshair position
crosshairNode.SetCrosshairRAS(position_RAS)
# Center the position in all slice views
slicer.vtkMRMLSliceNode.JumpAllSlices(slicer.mrmlScene, *position_RAS, slicer.vtkMRMLSliceNode.CenteredJumpSlice)
# Make the crosshair visible
crosshairNode.SetCrosshairMode(slicer.vtkMRMLCrosshairNode.ShowBasic)


# Add orientation marker
viewNode = getNode('vtkMRMLSliceNodeRed')
viewNode.SetOrientationMarkerType(viewNode.OrientationMarkerTypeAxes)


# Link slice views
for node in getNodesByClass('vtkMRMLSliceCompositeNode'):
	node.SetLinkedControl(1)

defaultSliceCompositeNode = slicer.vtkMRMLSliceCompositeNode()
defaultSliceCompositeNode.SetLinkedControl(1)
slicer.mrmlScene.AddDefaultNode(defaultSliceCompositeNode)

