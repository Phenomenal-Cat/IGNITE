# ImportAtlas.py

import os
import numpy as np

AtlasVolume = '/Volumes/NIFVAULT/procdata/harish/MR/ScrappyDoo_J402/afni_output/D99ATL_in_ScrappyDooSlicer.nii.gz'
LabelFile 	= '/Users/murphyap/Documents/NIF_ImagingData/NMT_v2.0_sym/tables_D99/D99_labeltable.txt'

#==== Load atlas volume as a 'segmentation'
VolumeNode 	= slicer.util.loadSegmentation(AtlasVolume)
VolumeNode.SetName('Atlas_Loaded')
seg = VolumeNode.GetSegmentation()

#==== Read atlas labels from file
LabelExt = os.path.splitext(LabelFile)[1]
if LabelExt == '.txt':
	Labels = np.loadtxt(LabelFile, skiprows=0, dtype='str') 

elif LabelExt == '.csv':
	


NoSegments = seg.GetNumberOfSegments()
if NoSegments ~= len(Labels):
	print('Warning, number of labels (%d, from %s) does not match number of segments (%d, from %s)!' % (len(Labels), LabelFile, NoSegments, AtlasVolume))


#==== Rename segments to atlas labels
for s in range(0, len(Labels)):
	segment = seg.GetNthSegment(int(Labels[s][0]))
	segment.SetName(Labels[s][1])