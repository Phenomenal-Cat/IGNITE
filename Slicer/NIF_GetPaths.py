
# NIF_GetPaths.py


import platform
import os
import glob


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



#====== Desphinxify all MRI volumes using AFNI


desphinxify
    -orient_mid  RIP 
    -input       sub-001_T1w.nii.gz
    -prefix      sub-001_T1w_DSPH.nii.gz