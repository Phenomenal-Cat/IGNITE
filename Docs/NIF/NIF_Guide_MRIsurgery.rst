.. _NIF_Guide_MRIsurgery:

=====================================
MRI-Guided Surgery
=====================================

.. image:: ../_images/Guides/MRI_Surgery/VirtualStereotaxDemo.png
  :width: 40%
  :align: right

.. contents:: :local:

.. panels::
  :column: col-lg-12 p-0 border-1
  :header: bg-primary text-bold p-1 pl-2
  :body: bg-secondary border-0 p-2

  :opticon:`info,mr-1` **Why Slicer?**
  ^^^^^^^^^^^^^^^^^^^^^^^^

  .. image:: ../_images/Logos/Slicer_button.png
    :align: left
    :width: 80

  There are many :ref:`software options <ViewingImages>` for viewing and processing 3D medical volume images such as MRI and CT. For anatomical image processing we prefer to use `Slicer <https://www.slicer.org/>`_ because it is free, `open-source <https://slicer.readthedocs.io/en/latest/user_guide/about.html#license>`_, `cross-platform <https://download.slicer.org/>`_, `NIH-funded <https://slicer.readthedocs.io/en/latest/user_guide/about.html#funding-sources>`_, `Python-scriptable <https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html>`_, `well documented <https://slicer.readthedocs.io/en/latest/index.html>`_ and has a `large user base <https://www.slicer.org/wiki/Main_Page/SlicerCommunity>`_ who provide a wealth of online resources and `tutorials <https://spujol.github.io/SkullStrippingTutorial/>`_. 

Aligning MRI to Stereotaxic Space
====================================

Care should be taken during acquisition of anesthetized MRI for surgical planning to ensure that the subject is correctly positioned in the stereotaxic frame and that the frame is carefully aligned with the magnet B0 field. However, it is still crucial to check and correct any discrepancy of alignment between stereotaxic and MRI coordinate frames. This section describes how to achieve this using Slicer.



Coarse alignment
--------------------

.. image:: ../_images/Guides/MRI_Surgery/Slicer_CoarseOrientation_Module.png
  :width: 50%
  :align: right

Data acquired on the NIF's 3T Siemens Prisma will initially appear in the wrong anatomical orientation on both the Siemens Syngo console and any 3D image viewing software. This is because the DICOM format is geared towards clinical use and doesn't provide an option for subjects in a 'sphinx' position. Instead, we set patient orientation to `prone <https://en.wikipedia.org/wiki/Prone_position>`_ position (DICOM code `head first prone (HFP) <https://dicom.innolitics.com/ciods/ct-image/general-series/00185100>`_). 
Most MRI file formats will contain header information describing the orientation of the 3D image relative to the MRI scanner's orientation (`'qform' and 'sform' <https://nifti.nimh.nih.gov/nifti-1/documentation/nifti1fields/nifti1fields_pages/qsform.html>`_ 4x4 transformation matrices). Software that display MR images will use that information for displaying the data relative to an anatomical `coordinate frame <https://www.slicer.org/wiki/Coordinate_systems>`_. 

To correct the volume orientation after importing to Slicer:

.. image:: ../_images/Guides/MRI_Surgery/Slicer_AxesToggle.png
  :width: 30%
  :align: right

1. To turn on axes labels, hover the cursor over or click on the :badge:`pin,badge-success` button in the top left corner of any of the 3 slice panels. On the top row of the dropdown panel that appears, click the :badge:`Show orientation marker,badge-success` icon (2nd icon from the right). In the dropdown menu that appears, select **Axes**. Labelled axes will appear in the bottom right corner of each slice view.

2. Open the :link-badge:`https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html,Transforms,cls=badge-success text-white` module from the :badge:`Modules,badge-primary` drop-down menu.

3. In the :badge:`Active Transform,badge-info` dropdown menu of the :link-badge:`https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html,Transforms,cls=badge-success text-white` module panel, select **Create New Linear Transform**.

4. In the :badge:`Rotation,badge-info` subpanel of the :badge:`Transforms,badge-success` panel, set the **LR** rotation to -90°.

5. Under the :badge:`Apply transform,badge-info` subpanel of the :badge:`Transforms,badge-success` panel, select the imported volume from the **Transformable** column, and click the :badge:`green arrow,badge-success` button to move it into the **Transformed** column. The slice images in the view should immediately update their orientation.

6. To 'harden' (i.e. permanently apply) the transform to the selected volume, click the :badge:`Harden transform,badge-success` button in the :badge:`Apply transform,badge-info` subpanel of the :badge:`Transforms,badge-success` panel. The selected volume will automatically move back into the **Transformable** column, with the transform applied.



Fiducial Markup of the Frankfurt Plane
----------------------------------------

Once the MRI volume is in approximately the correct orientation, we need to perform fine orientation adjustments in order for the 3D MRI volume to be aligned with stereotaxic coordinate space. To achieve this we first identify the stereotaxic coordinate frame and then apply the necessary transforms to bring the MRI volume into alignment with it.

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/jkqhIkxWcbA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


.. image:: ../_images/Guides/MRI_Surgery/Slicer_Fiducials.png
  :align: right
  :width: 50%


1. Open the :link-badge:`https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html,Markups,cls=badge-success text-white` module from the :badge:`Modules,badge-primary` drop-down menu. 

2. In the :badge:`Create,badge-info` section at the top of the :link-badge:`https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html,Markups,cls=badge-success text-white` module panel, click the :badge:`Create fiducial markup,badge-success` button (first button on the left). A new **MarkupsFiducial** node will appear in the list below. Give it an appropriate name by right clicking on the node and selecting **Rename**. Here we use 'Frankfurt' since the fiducial markers we are placing will define the stereotaxic `Franfurt plane <https://en.wikipedia.org/wiki/Standard_anatomical_position#Frankfurt_plane>`_.

3. Select the :badge:`Create and place,badge-success` tool from the :badge:`Toolbar,badge-info` at the top of the Slicer window. From the dropdown menu, select the :badge:`Fiducial,badge-success` option. 

.. image:: ../_images/Guides/MRI_Surgery/Slicer_EarBar_Tip.png
  :align: right
  :width: 20%

4. Start with the ear bar tips. In either the axial or coronal slice views, scroll through the slices (using the :badge:`slider,badge-primary` at the top of the slice panel or the :badge:`arrow,badge-primary` keys on your keyboard) until you find slices where the left ear bar is visible. In a T1-weighted MRI the plastic ear bar tips appear low intensity (black) with a high intensity (white) line inside them caused by the Gadolinium contrast agent that they have been filled with. `Zoom <https://www.slicer.org/wiki/Documentation/4.1/SlicerApplication/MouseandKeyboardShortcuts#Rotate.2C_Zoom.2C_Pan>`_ in on the tip of ear bar and scroll back and forth through the slices to find the slice in which the ear bar protrudes furthest medial. Click on the boundary between the ear bar tip  (black) and tissue (grey) to place the fiducial marker. A new marker will appear in the :badge:`Control Points,badge-info` panel of the :link-badge:`https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html,Markups,cls=badge-success text-white` module panel. 

5. Repeat the process in step 4 for the right ear bar tip and the left and right infraorbital ridges.


Aligning Volume to Stereotaxic Space
--------------------------------------

In order to manually rotate the volume, it's helpful to first modify some display settings that will help you visualize the required transform more easily:

1. To view the fiducial markers more clearly, open the :badge:`Display,badge-info` sub-panel of the :link-badge:`https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html,Markups,cls=badge-success text-white` module panel. Increase :badge:`Glyph Size,badge-primary` so that the markers can be clearly seen. 

2. In the :badge:`2D Display,badge-primary` section of the :badge:`Advanced,badge-info` sub-panel, check the **Projection Visibility** box. This makes the 2D projection of all fiducial markers visible in each slice view panel, irrespective of which slice is currently visible. 

3. Turn on crosshairs by clicking . Then click on one of the ear bar tip fiducial markers in the coronal slice view. The crosshair should jump to the intersecting slices in all 3 slice windows.

Now we can begin transforming the volume:

4. In the :link-badge:`https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html,Transforms,cls=badge-success text-white` module, select **Create New Linear Transform** in the :badge:`Active Transform,badge-info` dropdown menu and move both the MRI volume and the fiducial markers from the **Transformable** column to the **Transformed** column.

5. In the :badge:`Rotation,badge-info` sub-panel of the :link-badge:`https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html,Transforms,cls=badge-success text-white` module, start by applying **LR** rotation until the eye bar fiducials are level with the ear bar fiducial in the coronal slice view.

6. In the 




Centering Volume Origin to Stereotaxic Space
---------------------------------------------

Once the MRI volume has been reoriented to match stereotaxic space, we finally need to update the volume origin coordinates to match ear bar zero. Origin information is stored in the volume file header and will initially be determined by the scanner's isocenter, and thus will be arbitrary relative to the stereotaxic origin.

1. In the :link-badge:`https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html,Markups,cls=badge-success text-white` module, note the 'RAS' (xyz) coordinates of the left and right ear bar tips. 




Registering other data to the MRI
==================================

.. image:: ../_images/Guides/MRI_Surgery/Slicer_CT-MR_reg.png
  :align: right
  :width: 50%

The MRI volume that was adjusted in the previous steps now defines stereotaxic coordinate space for that individual subject. If you have other MR images that were acquired in the same session (i.e. the animal did not move) then you can simply apply the same transforms to them. If you have volumes of other image modalities from the same subject, these can be co-registered to this MRI. For example, it can often be useful to produce a :ref:`3D model of the skull surface using CT data <NIF_Guide_SkullModel>`. However, it is recommended that CT be acquired without the use of a stereotax in order to minimize image artifacts. If you want to use the digital 3D model of the skull (derived from CT) to customize cranial implants then it is important for the CT volume to first be co-registered with the MRI that is in stereotaxic space.

1. With the MRI and CT volumes both loaded into the Slicer scene, open the :badge:`Volumes,badge-success` module and select the CT volume as the :badge:`Active Volume,badge-primary`. Under the :badge:`Display,badge-info` subpanel of the :badge:`Volumes,badge-success` module, set the :badge:`Lookup Table,badge-primary` to a bright color (e.g. 'ReverseRainbow') and raise the lower :badge:`Threshold,badge-primary` value so that only the bone is labelled.

2. In the Slice view, click on any slice and the press the :badge:`>>,badge-primary` button in the dropdown menu at the top of that panel. Set the background (:badge:`B,badge-primary`) volume as the MRI and the foreground (:badge:`F,badge-primary`) volume as the CT. Then move the vertical slider so that both the MRI and the thresholded CT label are visible.

3. Next, use the :link-badge:`https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html,Transforms,cls=badge-success text-white` module to manually adjust the orientation and position of the CT volume to match that of the MRI volume (as described above).

4. In the :link-badge:`https://www.slicer.org/wiki/Documentation/4.4/Modules/Registration,Registrations,cls=badge-primary text-white` dropdown menu of the :badge:`Modules,badge-primary` dropdown menu, select the :link-badge:`https://www.slicer.org/wiki/Modules:BRAINSFit,"General registration (BRAINS)",cls=badge-success text-white` module.

5. In the :link-badge:`https://www.slicer.org/wiki/Modules:BRAINSFit,"General registration (BRAINS)",cls=badge-success text-white` module panel, set the adjusted MRI as the :badge:`Fixed Image Volume,badge-primary` and the CT volume as the :badge:`Moving Image Volume,badge-primary`. Increase the :badge:`Percentage of Samples,badge-primary` value to **0.02** and select a :badge:`Rigid (6 DOF),badge-primary` registration phase. Then click the :badge:`Apply,badge-primary` button to run.

6. Visually assess the quality of the registration by scrolling through the slice views. Differences in subject posture between CT and MRI acquisition (e.g. vertebra positions, mandible opening, soft tissue deformations) may negatively impact registration accuracy. In this case an image mask should be created to exclude voxels outside of the brain / skull region from influencing the registration.


