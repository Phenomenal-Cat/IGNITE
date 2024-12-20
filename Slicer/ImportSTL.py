

# ImportSTL.py


STLfile = '/Users/murphyap/Documents/NIF_ImagingData/MR/Phelps_H73R/Phelps_STLs/Phelps_Chamber_VeryFinal.stl'

Color 		= [0.5, 0.5, 0]
Opacity 	= 0.5
LineWidth 	= 3
 

Model  		= slicer.util.loadModel(STLfile)
DisplayNode = Model.GetDisplayNode()
DisplayNode.SetColor(Color)
DisplayNode.SetOpacity(Opacity)
DisplayNode.SetSliceIntersectionThickness(LineWidth)
