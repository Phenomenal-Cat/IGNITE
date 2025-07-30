#================== Generate_ConnectorBlock.py ===================
# This script generates a CAD model of a microdrive tower that can be 
# imported into a milti-drive assembly.
# For more information, see: https://py-ignite.readthedocs.io/en/latest/ImplantDesign.html
#     _________  ________     ____    ___  _________  _________  _______
#    /__   ___/ /  _____/    /    |  /  / /__   ___/ /__   ___/ /  ____/
#      /  /    /  / ___     /     | /  /    /  /       /  /    /  /___
#     /  /    |  | |_  |   /  /|  |/  /    /  /       /  /    /  ____/
#  __/  /__   |  \__/  /  /  / |     /  __/  /__     /  /    /  /____
# /_______/    \______/  /__/  |____/  /_______/    /__/    /_______/
#
# Image-Guided Neural Implantation Targeting Extensions
# https://py-ignite.rtfd.io
#=========================================================

import FreeCAD as App
import Part
import Draft
import numpy as np
import math
from BOPTools import BOPFeatures

#======== Clear FeeCAD 'report view' window
def clear_report_view():
	Gui.getMainWindow().findChild(QtGui.QTextEdit, "Report view").clear()

#======== Set color of object in GUI
def setObjColor(obj, color):
	colorlist=[]
	for i in range(len(obj.Shape.Faces)):
		colorlist.append(color)
	if (len(colorlist) == 0):
		print('Warning: Object ''%s'' contains %d faces - unable to set color.\n'%(obj.Name, len(colorlist),))
	obj.ViewObject.DiffuseColor = colorlist

#=============== Create and save document
filename = 'TEST'
FullFilename = "ConnectorBlock_%s" % (filename)
doc 	= FreeCAD.newDocument(FullFilename) 				# Create new document
bp 	= BOPFeatures.BOPFeatures(App.activeDocument())	


#=============== Connector block settings
Connector_Make 	= "Omnetics"	# Connector manufacturer 
Connector_Channels 	= 32			# Number of channels per connector
Connector_Gender 	= 'F' 			# Gender of connector - femal (F) or male (M)
Connector_Number 	= 4			# Number of connectors
Connector_Spacing	= 3			# Spacing between the center-lines of adjacent connectors (mm) - must be > connector width
Connector_orientation = 'V'			# connector pin oreitnation - Vertical (V) or horizontal (H)

if Connector_orientation == 'V':
	Rotation 		= App.Rotation(0, 0, math.radians(90))
	SpacingDim 	= 2
elif Connector_orientation == 'H':
	Rotation 		= App.Rotation(0, 0, 0)
	SpacingDim 	= 1
else:
	print('Warning - unknown connector orientation (%s) was provided!\n' % Connector_orientation)

# Import connector from STEP file
IgniteDir 			= '/Volumes/NIFVAULT/projects/murphyap_NIF/NIF_Code/IGNITE/FreeCAD/Parts/'
DS_Filename 		= 'Connector_%s_%sch_%s.STEP' % (Connector_Make, Connector_Channels, Connector_Gender)
DS_FullFile 		= os.path.join(IgniteDir, 'Connectors', Connector_Make, DS_Filename)
Connector			= App.ActiveDocument.addObject("Part::Feature","Connector")
Connector.Shape 	= Part.read(DS_FullFile)
Connector.Placement 	= App.Placement(App.Vector(0,0,0), Rotation)
#Screw.Visibility 	= False
#setObjColor(Screw, (0.0, 1.0, 0.0))

# Create bounding box for each connector
BoundingBox 				= doc.addObject("Part::Box", "ConnectorHole")	
BoundingBox.Length 			= 13	
BoundingBox.Width 			= 2
BoundingBox.Height 			= 10	
BoundingBox.Placement 		= App.Placement(App.Vector(-BoundingBox.Length/2,-BoundingBox.Width/2, -BoundingBox.Height/2), App.Rotation(0,0,0))
BoundingBox.ViewObject.Transparency 	= 50
ConnectorOffsets 			= np.linspace(0, (Connector_Number-1)*Connector_Spacing, Connector_Number)

# Duplicate connectors and bounding boxes
for c in range(1, Connector_Number):
	NewPlacement 			= App.Placement()
	NewPlacement.Base 		= App.Vector(0, ConnectorOffsets[c], 0)
	NewConnector 			= doc.copyObject(Connector, False)
	NewConnector.Placement 	= NewPlacement

	NewPlacement 			= App.Placement()
	NewPlacement.Base 		= App.Vector(-BoundingBox.Length/2, ConnectorOffsets[c] - float(BoundingBox.Width/2), -BoundingBox.Height/2)
	NewConnectorBlock 		=doc.copyObject(BoundingBox, False)
	NewConnectorBlock.Placement = NewPlacement

doc.recompute() 						# Display results in GUI

# Create main body of connector block
MainBlock 			= doc.addObject("Part::Box", "ConnectorBlock")	
MainBlock.Length 	= 20
MainBlock.Width		= 30
MainBlock.Height 	= 40