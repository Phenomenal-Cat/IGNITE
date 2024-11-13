
# NIF_GetPaths.py


import platform
import os
import glob


AnimalID = "Palak"

#===== Check OS and NIFVAULT mount point
OS = platform.system()
if OS == "Darwin": 				# Mac
	DcmDir = '/Volumes/NIFVAULT/dicom/'

elif OS == "Linux":
	 DcmDir = 'N:\\dicom\'

if !os.path.exists(DcmDir):
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


