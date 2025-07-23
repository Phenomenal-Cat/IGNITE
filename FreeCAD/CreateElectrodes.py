
import FreeCAD as App
import Part
import Draft
import numpy as np
from BOPTools import BOPFeatures

CoordinateList 	= [[22.589, 4.5, 7.251],[13.589, 6.5, 23.751], [21.589, -23, 0.251], [21.589, -23, 7.251]]
Coordnames 	= ['V4v', 'MST', 'TEad', 'STP']

#=============== Create and save document
FullFilename = "ElectrodePositions"
doc 	= FreeCAD.newDocument(FullFilename) 				# Create new document
bp 	= BOPFeatures.BOPFeatures(App.activeDocument())		

#=============== Create electrodes
BaseCylinder 				= doc.addObject("Part::Cylinder", "Electrode")
BaseCylinder.Radius 			= 1
BaseCylinder.Height 			= 55

for e in range(0, len(CoordinateList)):
	NewElectrode			= Draft.clone(BaseCylinder)
	NewElectrode.Placement 	= App.Placement(App.Vector(CoordinateList[e]), App.Rotation(0,0,0))
	NewElectrode.Label 		= "Electrode_%s" % Coordnames[e]

#============ Finish up
FreeCADGui.updateGui()
doc.recompute() 						# Display results in GUI
Gui.SendMsgToActiveView("ViewFit")			# Set GUI window view to fit