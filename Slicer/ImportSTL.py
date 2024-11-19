

# importSTL.py


STLfile = '/Users/murphyap/Documents/NIF_ImagingData/MR/Phelps_H73R/Phelps_STLs/Phelps_Chamber_VeryFinal.stl'

Model= slicer.util.loadModel(STLfile)
DisplayNode = Model.GetDisplayNode()
DisplayNode.SetColor(0.5, 0.5, 0)