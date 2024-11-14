# LoadDICOM.py

from DICOMLib import DICOMUtils

def LoadDICOM(dicomDir):
	loadedNodeIDs = []  							# list of all loaded node IDs
	with DICOMUtils.TemporaryDICOMDatabase() as db:
		DICOMUtils.importDicom(dicomDir, db)
		patientUIDs 	= db.patients()
		for patientUID in patientUIDs:
			loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))



dicomDir = "c:/my/folder/with/dicom-files"  # input folder with DICOM files
LoadDICOM(dicomDir)