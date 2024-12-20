
#==================  NIF_GetPaths.py ================== 
# This script is specifically for use by researchers at the
# National Institutes of Health (NIH) who have acquired experimental
# imaging data in the Neurophysiology Imaging Facility (NIF). It
# uses the known structure of the NIF's networked storage server where
# DIOCM data are hosted (and other idiosyncrasies of those data) to
# simplify selection, loading and initial processing of MRI and CT
# datasets.
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
#=========================================================

import platform
import os
import glob
from DICOMLib import DICOMUtils


#========= Load DICOM volumes to Slicer
def LoadDICOM(dicomDir):
loadedNodeIDs = []  								# list of all loaded node IDs
with DICOMUtils.TemporaryDICOMDatabase() as db:
	DICOMUtils.importDicom(dicomDir, db)
	patientUIDs 	= db.patients()
	for patientUID in patientUIDs:
		loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))




AnimalID = "Scrappy"
SessionIndx_MR 	= 0


#===== Check OS and NIFVAULT mount point
OS = platform.system()
if OS == "Darwin": 				# Mac
	DcmDir = '/Volumes/NIFVAULT/dicom/'

#elif OS == "Linux":
	 #DcmDir = 'N:\\dicom\'

if not os.path.exists(DcmDir):
	print("Default NIFVAULT DICOM directory was not found on this system!")


#===== Find subject's MRI and CT directories and return session dates
MR_dir = os.path.join(DcmDir, "MR")
CT_dir = os.path.join(DcmDir, "CT")

AllSubjects_MR = [os.path.split(f.path)[1] for f in os.scandir(MR_dir) if f.is_dir()]
AllSubjects_CT = [os.path.split(f.path)[1] for f in os.scandir(CT_dir) if f.is_dir()]

MR_Match = [phrase for phrase in AllSubjects_MR if AnimalID in phrase]
CT_Match = [phrase for phrase in AllSubjects_CT if AnimalID in phrase]

if len(MR_Match) > 0:
	Sessions_MR = [os.path.split(f.path)[1] for f in os.scandir(os.path.join(MR_dir, MR_Match[0])) if f.is_dir()]

if len(CT_Match) > 0:
	Sessions_CT = [os.path.split(f.path)[1] for f in os.scandir(os.path.join(CT_dir, CT_Match[0])) if f.is_dir()]


#===== Find all scans from selected session dates and search for specific sequences
SequenceStrings = ['T1_MPRAGE', 'T2_space','tof_fl3d', 'MEAN']
SequenceLabels  = ['T1', 'T2', 'TOF', 'Average']
SessionFullpath = os.path.join(DcmDir, "MR", MR_Match[0], Sessions_MR[SessionIndx_MR])
SessionScansAll = os.listdir(SessionFullpath)
for s in range(0, len(SequenceStrings)):
	StrMatch = [phrase for phrase in SessionScansAll if SequenceStrings[s] in phrase]


v1 = slicer.util.loadVolume(os.path.join(DcmDir, "MR", Sessions_MR[SessionIndx_MR]))


#===== Load requested scans

LoadDICOM(SessionFullpath)


#====== Desphinxify all MRI volumes using AFNI


desphinxify
    -orient_mid  RIP 
    -input       sub-001_T1w.nii.gz
    -prefix      sub-001_T1w_DSPH.nii.gz