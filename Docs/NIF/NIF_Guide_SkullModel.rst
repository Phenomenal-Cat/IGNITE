.. _NIF_Guide_SkullModel:

=================================
Generating a Skull Model
=================================

.. image:: ../_images/Guides/SkullSegmentation/SkullTest1.png
  :width: 30%
  :align: right
  :alt: 3D rendered skull
  :target: https://www.slicer.org/

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

Data acquisition
==================

If you are collecting a CT data specifically for the construction of a skull model that can be 3D printed for surgical planning purposes then please let the :ref:`NIF staff <NIF_Team>` know this when you book your scan. CT scans are relatively quick (~10 minutes) and can be obtained in the same session as high-resolution anatomical MRIs.

To make the digital skull segmentation process easier, consider the following prior to CT acquisition:

  - When possible, acquire CT data prior to headpost or other implants since most hardware will cause some artifacts in the CT volume.
  - If the animal wears a collar, remove it before scanning
  - Consider forgoing the stereotaxic frame and instead resting the anesthetized animal's head on the foam chin rest block provided by the NIF. This will save you time manually removing the sterotaxic frame from you skull segmentation. 


Segmenting skull from MRI?
============================

.. dropdown:: :opticon:`info,mr-1` **Why use CT rather than MRI?**
  :open:
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :body: bg-dark

  Computed tomography (CT) and magnetic resonance imaging (MRI) volumes contain very different tissue contrasts, as shown in the example coronal slice images below. CT has relatively low contrast for different tissue types but has excellent contrast between bone and soft tissue. Bone in a T1-weighted MRI on the other hand has a range of intensities that overlap with that of air, which makes it more difficult to segment via thresholding. Since the NIF has a CT scanner, we therefore recommend acquiring a CT in addition to anatomical MRIs, for use in skull reconstruction. If for some reason you needed to reconstruct a skull from MRI data, it is still possible but it is slightly more work and the end result will be less accurate than with CT. The interactive 3D models embedded below demonstrate this difference. 


  .. panels::
    :column: col-lg-6 col-md-8 col-sm-12 p-1 border-1
    :header: bg-primary text-light text-justify p-1 pl-2
    :body: bg-secondary text-center border-1 p-2

    **MRI**
    ^^^^^^

    .. image:: ../_images/Guides/SkullSegmentation/ImageContrast_MRI.png
      :align: center
      :width: 400

    .. raw:: html

      <iframe title="MRI Skull Decimated" frameborder="0" allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" allow="fullscreen; autoplay; vr" xr-spatial-tracking execution-while-out-of-viewport execution-while-not-rendered web-share width="400" height="300" src="https://sketchfab.com/models/704648e9e4224e7fa14eae38f407bfa0/embed?autospin=0.5&autostart=1&ui_theme=dark"> </iframe>

    ---

    **CT**
    ^^^^^^

    .. image:: ../_images/Guides/SkullSegmentation/ImageContrast_CT.png
      :align: center
      :width: 400

    .. raw:: html

      <iframe title="CT_Skull_decimated" frameborder="0" allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" allow="fullscreen; autoplay; vr" xr-spatial-tracking execution-while-out-of-viewport execution-while-not-rendered web-share width="400" height="300" src="https://sketchfab.com/models/30c5d657f68e47f99befd2a5a2c2889e/embed?autospin=0.5&autostart=1&ui_theme=dark"> </iframe>

  The video below demonstrates how to segment a skull surface from a T1-weighted MRI using 3D Slicer. Note that this process requires the `SurfaceWrapSolidify <https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify>`_ extension, which can be easily installed via the :link-badge:`https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html, "Extensions manager",cls=badge-primary` wizard.


  .. raw:: html

    <iframe src="https://nih.app.box.com/embed/s/oo29puywnshxnlsda2xegnsfugvc080m?sortColumn=date&view=list" width="800" height="550" frameborder="0" allowfullscreen webkitallowfullscreen msallowfullscreen></iframe>


Preparing and loading data
==============================

.. image:: ../_images/Guides/SkullSegmentation/SlicerUI_SkullSegmentation.png
  :width: 50%
  :align: right
  :alt: Slicer user interface

1. Copy your animal's CT data from the NIF's `DICOM server <https://nif.nimh.nih.gov/doc/dicom/app/explorer.html>`_ or :ref:`network storage <NIF-storage>` to a local drive on your computer. 

2. Download and install `Slicer <https://download.slicer.org/>`_, ensuring that your local computer meets the `system requirements <https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#system-requirements>`_.

3. Briefly familiarize yourself with the Slicer `application layout <https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html>`_. Slicer is a modular application and modules can be selected from the :badge:`Modules,badge-primary` drop-down menu in the :badge:`Toolbar,badge-info` row at the top of the window. Controls for the currently selected module will appear in the :badge:`Module panel,badge-info` located by default on the left side of the application window. The layout of the :badge:`Views,badge-info` panel can be customized via the :badge:`Layout toolbar, badge-primary`. 

4. To load DICOM format data into Slicer, open the pop-up :badge:`DICOM module, badge-success` via the button on the left of the :badge:`Toolbar,badge-info`. In the :badge:`DICOM module, badge-success` click the :badge:`Import DICOM files,badge-primary` button in the left panel and select the DICOM folder of your locally copied CT data. The scan header information will appear in the :badge:`DICOM database,badge-info` panel. With the CT scan selected, click the :badge:`Load,badge-info` button at the bottom of the module window. 

5. Once loaded you should immediately see the CT volume in the :badge:`Views,badge-info` panel. If the views appear black, you may need to adjust the contrast range by clicking and holding the cursor on any of the slice views and dragging left/ right. 

6. To visualize the CT data in 3D, select the :badge:`Volume Rendering,badge-success` module from the :badge:`Modules,badge-primary` drop-down menu in the :badge:`Toolbar,badge-info`. In the module panel you should see the name of the CT volume in the dropdown menu next to :badge:`Volume:,badge-primary`. If you have loaded multiple volumes, select the volume you want to visualize from the dropdown menu. Then click the closed eye :fa:`eye,mr-1` icon to the left of the :badge:`Volume:,badge-primary` dropdown. A 3D rendering of the current segmentation should appear in the 3D view. If it doesn't, try clicking the :badge:`Center 3D view,badge-info` icon (third icon from the left on the blue bar at the top of the 3D view panel), which should center the 3D view on the scene. 


Segmenting the skull from CT
=============================

.. raw:: html

  <iframe src="https://nih.app.box.com/embed/s/dw2h15tih3l8v81i9pbmw9mulmfj25py?sortColumn=date&view=list" width="800" height="550" frameborder="0" allowfullscreen webkitallowfullscreen msallowfullscreen></iframe>

.. image:: ../_images/Guides/SkullSegmentation/SegmentEditor.png
  :width: 40%
  :align: right
  :alt: Slicer segment editor window

1. Select the :link-badge:`https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html,"Segment Editor",cls=badge-success` module from the :badge:`Modules,badge-primary` drop-down menu. With the CT volume selected in the :badge:`Master volume,badge-info` dropdown menu of the :badge:`Segment Editor,badge-success` module panel, click the :badge:`+Add,badge-info` button to create a new segment, which will appear in the segment list. Double click the default green color box and set the segment name to **Bone** (which will appear yellowish in color).

2. Select the :badge:`Threshold,badge-primary` effect button. The slice view will begin to flash bone color. Adjust the threshold using the slider or the range counter fields. The left hand slider adjusts the lower threshold, so as you move it rightward, fewer low-intensity voxels will be selected (shown in yellow in the slice view). Moving the right hand slider to the left will deselect the highest intensity voxels, such as the enamel of the teeth and non-bone materials such as fiberglass headposts. When you are happy with the selection, click :badge:`Apply,badge-pirmary`.

3. To remove all labelled voxels that are not contiguous with the cranium, select the :badge:`Islands,badge-info` effect button. Select the :badge:`Keep selected islands,badge-info` radio button in the Islands effect panel and then click the cursor in the slice view window on a labelled voxel in the cranial bones. Any labelled voxels not contiguously connected to the cranial bones will be removed from the segmentation.

4. If there are labelled elements remaining that you wish to remove, you will need to manually disconnect them from the cranium voxels. One fast approach for achieving this is to navigate to the appropriate slice in one of the slice view panels (using the slider at the top of the view panel), and then use the :badge:`Scissors,badge-info` effect from the :link-badge:`https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html,"Segment Editor",cls=badge-success` module. Set :badge:`Operation,badge-info` to **Erase inside** and :badge:`Shape,badge-info` to whatever setting will make it easiest to select the voxels you wish to remove. It is important to unsure that :badge:`Slice cut` is set to **Symmetric**, or else voxels in the selected 2D region will be removed from every slice and not just the one you are currently viewing.

5. After removing some labelled voxels from the segmentation manually, try re-applying the :badge:`Islands,badge-info` effect again.  and the ear bar should become unlabeled. If it doesn't then there must be another point of contact between the earbar and the skull. Scroll through the slices to find it and remove it.

6. For removing irregular shaped regions from the segmented volume, use the :badge:`Paint,badge-info` effect. You can adjust the radius of the brush for removing different size regions, and you can even select a spherical brush that will remove voxels from neighboring slices for faster removal of larger regions.

7. When you are finished working:
  - Save the skull segmentation by clicking the :badge:`Save,badge-primary` button on the :badge:`Toolbar,badge-info`. By default the segmentation will save as a **.seg.nrrd** format.  Set the directory you wish to save your data to and give the segmentation a descriptive name before saving. 
  - Export the segmentation as a surface mesh by clicking the dropdown arrow on the :badge:`Segmentations...,badge-info` button in the :link-badge:`https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html,"Segment Editor",cls=badge-success` module, and select `Export to files...`. 

Convert segmentation to mesh and export
=========================================

Select the :badge:`Model Maker,badge-success` module by clicking the module drop-down menu, hovering the pointer over the :badge:`Surface models,badge-info` option and then selecting it from the second dropdown list.

1. Under the :badge:`Input Volume,badge-info` dropdown menu, select your label volume.
2. Under the :badge:`Models,badge-info` dropdown menu, select 'Create new ModelHeirarchy'.
3. Under :badge:`Model Maker Parameters,badge-info`, make any adjustments you wish. For example, you can increase the amount of smoothing that is applied to the mesh surface using the **Smooth** slider, or reduce the complexity of the resulting mesh (i.e. reduce the number of vertices and polygons) by increasing the **Decimate** slider.
4. Click **Apply** to run the model maker. When the process is complete, you will see the model appear in 3D view (overlaid on the 3D visualization of your label map). Go to the :link-badge:`https://slicer.readthedocs.io/en/latest/user_guide/modules/volumerendering.html,"Volume Rendering",cls=badge-success` module and turn off the label volume by clicking the open eye icon. Now you can inspect your model surface in the 3D view. If you are not happy with the result, you can re-run the ``Model maker`` with different parameters.
5. Save the surface mesh by clicking the :badge:`Save,badge-primary` icon in the top left of the Slicer window, selecting the file name of the surface, which by default will be something like ‘bone.vtk’, and changing it to a .stl file format. This format can be imported by nearly every 3D-printer software, as well as 3D editing software. 


Mesh editing and 3D printing
================================

.. image:: ../_images/Guides/SkullSegmentation/Skull3Dprint.jpg
  :width: 30%
  :align: right
  :alt: 3D printed skull

Before sending an exported surface mesh for 3D printing, it's important to inspect the surface. This is best done in a dedicated 3D surface editing software, such as the open-source `MeshLab <https://www.meshlab.net/>`_. 

There are various 3D printing facilities available at NIH, including through the NIMH and NEI machine shops. There are also many commercial printing options that offer a broader range of specialized materials depending on your requirements. 


