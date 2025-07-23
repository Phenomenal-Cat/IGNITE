
# desphinx.py




# This markups point list node specifies the center of rotation
centerOfRotationMarkupsNode = getNode("F")
# This transform can be  edited in Transforms module
rotationTransformNode = getNode("LinearTransform_3")
# This transform has to be applied to the image, model, etc.
finalTransformNode = getNode("LinearTransform_4")

def updateFinalTransform(unusedArg1=None, unusedArg2=None, unusedArg3=None):
  rotationMatrix = vtk.vtkMatrix4x4()
  rotationTransformNode.GetMatrixTransformToParent(rotationMatrix)
  rotationCenterPointCoord = [0.0, 0.0, 0.0]
  centerOfRotationMarkupsNode.GetNthControlPointPositionWorld(0, rotationCenterPointCoord)
  finalTransform = vtk.vtkTransform()
  finalTransform.Translate(rotationCenterPointCoord)
  finalTransform.Concatenate(rotationMatrix)
  finalTransform.Translate(-rotationCenterPointCoord[0], -rotationCenterPointCoord[1], -rotationCenterPointCoord[2])
  finalTransformNode.SetAndObserveMatrixTransformToParent(finalTransform.GetMatrix())

# Manual initial update
updateFinalTransform()

# Automatic update when point is moved or transform is modified
rotationTransformNodeObserver = rotationTransformNode.AddObserver(slicer.vtkMRMLTransformNode.TransformModifiedEvent, updateFinalTransform)
centerOfRotationMarkupsNodeObserver = centerOfRotationMarkupsNode.AddObserver(slicer.vtkMRMLMarkupsNode.PointModifiedEvent, updateFinalTransform)

# Execute these lines to stop automatic updates:
# rotationTransformNode.RemoveObserver(rotationTransformNodeObserver)
# centerOfRotationMarkupsNode.RemoveObserver(centerOfRotationMarkupsNodeObserver)