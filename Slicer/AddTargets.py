# AddTargets.py

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
# Developed by Aidan P. Murphy, Ph.D
#============================================================================= 

import numy as np
import csv

TargetCoordsFile = '/Users/murphyap/Documents/NIF_ImagingData/MR/ScrappyDoo_/Slicer/ScrappyDoo_TargetROIs.csv'

#===== Read target data from file
FileString 	= os.path.splitext(os.path.basename(TargetCoordsFile))[0]
FileExt  	= os.path.splitext(TargetCoordsFile)[1]


if FileExt == '.csv':
	printf('Attempting to load targets from csv file %s...' % (TargetCoordsFile))
	with open(TargetCoordsFile, 'r') as f:
	    reader = csv.reader(f)
	    Coords = list(reader)
	CoordsArray 		= np.array(Coords) 			
	pointListNode 		= slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode")

	# Create markups for each target
	for c in range(1, len(Coords)):
		xyz = np.asfarray(CoordsArray[c][1:])
		n = pointListNode.AddControlPoint(xyz[0], xyz[1], xyz[2])
		pointListNode.SetNthControlPointLabel(n, CoordsArray[c][0])

elif FileExt in ['.fcsv','.json']:
	printf('Loading targets from file %s...' % (TargetCoordsFile))
	pointListNode = slicer.util.loadMarkups(TargetCoordsFile)

else:
	print('Warning: input file extension %s is not a recognized format for target coordinates!' % (FileExt))


# Set default appearance
TargetColors 	= [0,0,1]
TextScale 		= 3

# Format points
pointListNode.SetName(FileString) 					# Name the point list Node
pointListNode.SetLocked(True) 						# Lock all points (prevent user accidentally moving them)
DisplayNode = pointListNode.GetDisplayNode()		
DisplayNode.SetSelectedColor(TargetColors)			# Set all points to a color
DisplayNode.SetTextScale(TextScale) 				# Scale label text




	