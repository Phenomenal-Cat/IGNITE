

# AlignStereotaxic.py



#========== Initialize default stereotaxic fiducial points
Macaque_IPD 		= 35 			# Average inter-pupillary distance (mm) for adult macaque
Macaque_IAD			= 80			# Average inter-aural distance (mm) for adult macaque
Macaque_IOAD		= 52			# Average inter orbital-auditory meatus distance (mm) for adult macaque

Fiducial_names 		= ['Earbar_R','Earbar_L','Orbit_R','Orbit_L']
Fiducial_starts 	= [[Macaque_IAD/2, 0, 0], [-Macaque_IAD/2, 0, 0], [Macaque_IPD/2, Macaque_IOAD, 0], [-Macaque_IPD/2, Macaque_IOAD, 0]]

pointListNode 		= getNode("vtkMRMLMarkupsFiducialNode1")
for n in range(0, len(Fiducial_names)):
	n = pointListNode.AddControlPoint(Fiducial_starts[n][0], Fiducial_starts[n][1], Fiducial_starts[n][2])
	pointListNode.SetNthControlPointLabel(n, Fiducial_names[n])





# Calculate stereotaxic origin point

fn = slicer.util.getNode('F')

for f in range(0, fn.GetNumberOfControlPoints()):
	Label 	= fn.GetNthControlPointLabel(f)
	Pos 	= fn.GetNthControlPointPosition(f)


Earbar_Offset = []
for xyz in range(0,3):
	Earbar_Offset.append(fn.GetNthControlPointPosition(0)[xyz]-fn.GetNthControlPointPosition(1)[xyz])


Earbar_Left 	= fn.GetNthControlPointPosition(0)
Earbar_Midpoint = Earbar_Offset/2




# # activate placement of multiple points
# w=slicer.qSlicerMarkupsPlaceWidget()
# w.setMRMLScene(slicer.mrmlScene)
# markupsNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsCurveNode")
# w.setCurrentNode(slicer.mrmlScene.GetNodeByID(markupsNode.GetID()))
# # Hide all buttons and only show place button
# w.buttonsVisible=False
# w.placeButton().show()
# w.show()