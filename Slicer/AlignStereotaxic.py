

#==================== AlignStereotaxic.py ====================
# This script currently contains snippets of code that can be used
# to initialize fiducial control points for stereotaxic alignment of
# MRI in the Slicer GUI. This involves:
#
# 	1. automatically creating fiducial markers for earbar and orbit bar tips
#	2. the user manually adjusting the placement
#	3. translating the volume to make the stereotaxic origin the volume origin
#	4. rotating the volume to make the axial plan parallel to the Frankfurt plane
#	5. 
#
# - 11/13/2024 - Aidan Murphy



#========== Initialize default stereotaxic fiducial points
Macaque_IPD 		= 35 			# Average inter-pupillary distance (mm) for adult macaque
Macaque_IAD			= 76			# Average inter-aural distance (mm) for adult macaque
Macaque_IOAD		= 52			# Average inter orbital-auditory meatus distance (mm) for adult macaque

Fiducial_names 		= ['Earbar_R','Earbar_L','Orbit_R','Orbit_L','Volume_Origin']
Fiducial_xyz 	= [[Macaque_IAD/2, 0, 0], [-Macaque_IAD/2, 0, 0], [Macaque_IPD/2, Macaque_IOAD, 0], [-Macaque_IPD/2, Macaque_IOAD, 0],[0,0,0]]

pointListNode 		= getNode("vtkMRMLMarkupsFiducialNode1")
for f in range(0, len(Fiducial_names)):
	n = pointListNode.AddControlPoint(Fiducial_xyz[f][0], Fiducial_xyz[f][1], Fiducial_xyz[f][2])
	pointListNode.SetNthControlPointLabel(n, Fiducial_names[f])






#========== Calculate stereotaxic origin
fn = slicer.util.getNode('F')
fn.SetName('Frankfurt plane')

points = []
for f in range(0, fn.GetNumberOfControlPoints()):
	Label 	= fn.GetNthControlPointLabel(f)
	Pos 	= fn.GetNthControlPointPosition(f)
	points.append((Label, Pos))


Earbar_Right 	= np.array(fn.GetNthControlPointPosition(0), dtype='float32')
Earbar_Left 	= np.array(fn.GetNthControlPointPosition(1), dtype='float32')
Earbar_Offset 	= np.diff([Earbar_Right, Earbar_Left], axis=0)
Earbar_Midpoint = Earbar_Right + (Earbar_Offset/2)


Fiducial_names 	= ['Volume_Origin', 'Stereotaxic_Origin']
Fiducial_xyz 	= [[0,0,0], Earbar_Midpoint.tolist()[0]]
for f in range(0, len(Fiducial_names)):
	n = pointListNode.AddControlPoint(Fiducial_xyz[f][0], Fiducial_xyz[f][1], Fiducial_xyz[f][2])
	pointListNode.SetNthControlPointLabel(n, Fiducial_names[f])


#========== Fit plane to markup control points
pointListNode = slicer.mrmlScene.GetFirstNodeByName("F")
p1 = np.zeros(3)
p2 = np.zeros(3)
p3 = np.zeros(3)
pointListNode.GetNthControlPointPosition(0, p1)
pointListNode.GetNthControlPointPosition(1, p2)
pointListNode.GetNthControlPointPosition(2, p3)
# Get plane axis directions
n = np.cross(p2-p1, p2-p3) # plane normal direction
n = n/np.linalg.norm(n)
t = np.cross([0.0, 0.0, 1], n) # plane transverse direction
t = t/np.linalg.norm(t)
# Set slice plane orientation and position
sliceNode.SetSliceToRASByNTP(n[0], n[1], n[2], t[0], t[1], t[2], p1[0], p1[1], p1[2], 0)



#====== Create transform





#====== Update Frankfurt plane from fiducial points
def UpdateSlicePlane(param1=None, param2=None):
  nOfFiduciallPoints = markups.GetNumberOfFiducials()
  if nOfFiduciallPoints < 3:
    return  # not enough points
  points = np.zeros([3,nOfFiduciallPoints])
  for i in range(0, nOfFiduciallPoints):
    markups.GetNthFiducialPosition(i, points[:,i])
  
  # Compute plane position and normal
  planePosition = points.mean(axis=1)
  planeNormal 	= np.cross(points[:,1] - points[:,0], points[:,2] - points[:,0])
  planeX 		= points[:,1] - points[:,0]
  sliceNode.SetSliceToRASByNTP(planeNormal[0], planeNormal[1], planeNormal[2],
    planeX[0], planeX[1], planeX[2],
    planePosition[0], planePosition[1], planePosition[2], 0)

# Get markup node from scene
sliceNode 	= slicer.app.layoutManager().sliceWidget('Red').mrmlSliceNode()
markups 	= slicer.util.getNode('F')

# Update slice plane manually
UpdateSlicePlane() 		

# Update slice plane automatically whenever points are changed
#markupObservation = [markups, markups.AddObserver("ModifiedEvent", UpdateSlicePlane, 2)]




# # activate placement of multiple points
# w=slicer.qSlicerMarkupsPlaceWidget()
# w.setMRMLScene(slicer.mrmlScene)
# markupsNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsCurveNode")
# w.setCurrentNode(slicer.mrmlScene.GetNodeByID(markupsNode.GetID()))
# # Hide all buttons and only show place button
# w.buttonsVisible=False
# w.placeButton().show()
# w.show()