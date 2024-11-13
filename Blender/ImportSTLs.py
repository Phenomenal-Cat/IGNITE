# ImportSTLs.py

import bpy
import os

SubjectStlDir   = '/Users/murphyap/Documents/NIF_ImagingData/MR/Phelps_H73R/STLs'


AllStlFiles     = [f for f in os.listdir(SubjectStlDir) if os.path.isfile(os.path.join(SubjectStlDir, f))]
SearchStrings = ["skull", "arteries"]
for s in range(0, len(SearchStrings)):
    StlMatch  = [phrase for phrase in AllStlFiles if SearchStrings[s] in phrase]


SkullModel      = os.path.join(SubjectDir, 'Phelps_SkullSegmentation_V2.stl')
ArteryModel     = os.path.join(SubjectDir, 'Phelps_Slicer', 'Phelips_artery_2.stl')



bpy.ops.import_mesh.stl(filepath=abs_filename_with_folder , filter_glob="*.stl", directory=folder) 
