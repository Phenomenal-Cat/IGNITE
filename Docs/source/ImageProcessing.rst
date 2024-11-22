.. _ImageProcessing:

=========================================
:fa:`brain` Image processing
=========================================

.. contents:: :local:


:fa:`brain` Imaging data acquisition
======================================







.. dropdown:: :fa:`server` Data storage and access for :bdg-link-danger:`NIF <>` users
  :color: primary
  :chevron: down-up





:fa:`ruler-combined` Aligning MRI volumes to stereotaxic space
=====================================================================


1. Localize stereotaxic frame
------------------------------------------


2. Calculate and apply transform
------------------------------------------




:fa:`object-ungroup` Cross-modal volume alignment
======================================================





:fa:`skull` Creating a skull model
=========================================

.. image:: _images/Guides/SkullSegmentation/SkullTest1.png
  :width: 30%
  :align: right
  :alt: 3D rendered skull

The subject's skull is the surface that most implanted neural hardware needs to attach to. 



Segmenting skull from MRI?
------------------------------


.. dropdown:: :opticon:`info,mr-1` **Why use CT rather than MRI?**
  :open:
  :color: primary
  :chevron: down-up

  Magnetic resonance imaging :bdg-info:`MRI` and Computed tomography :bdg-danger:`CT` volumes contain very different tissue contrasts, as shown in the example coronal slice images below. CT has relatively low contrast for different tissue types but has excellent contrast between bone and soft tissue. Bone in a T1-weighted MRI on the other hand has a range of intensities that overlap with that of air, which makes it more difficult to segment via thresholding. Additionally, CT scans tend to be higher resolution. In the images below, the MRI has 0.5mm isotropic voxels and took ~30 minutes to acquire, while the CT has 0.2mm isotropic voxels and took ~1 minute to acquire. **It is therefore recommended to acquire a CT of the subject when possible** (in addition to anatomical MRIs), for use in skull reconstruction process. If for some reason you needed to reconstruct a skull from MRI data, it is still possible but requires more manual intervention and the end result will be less accurate than with CT. The interactive 3D models embedded below demonstrate this difference. 


	.. grid:: 2
		:gutter: 2
		:margin: 0
		:padding: 0

		.. grid-item-card::
   			:margin: 0
   			:columns: 6
   			:class-card: sd-bg-secondary sd-text-white sd-rounded-3 sd-border-0
   			:class-header: sd-bg-info sd-rounded-3
   			:class-footer: sd-bg-dark

			:fa:`magnet` **MRI**
			^^^^^^

			.. image:: _images/Guides/SkullSegmentation/ImageContrast_MRI.png
				:align: center
				:width: 400

			+++++
			.. raw:: html

				<iframe title="MRI Skull Decimated" frameborder="0" allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" allow="fullscreen; autoplay; vr" xr-spatial-tracking execution-while-out-of-viewport execution-while-not-rendered web-share width="300" height="200" src="https://sketchfab.com/models/704648e9e4224e7fa14eae38f407bfa0/embed?autospin=0.5&autostart=1&ui_theme=dark"> </iframe>

			- **Scanner:** 			Siemens Prisma 3T
			- **Voxel size:**		0.5 mm  isotropic
			- **Scan duration:**	~30 minutes
			- **Reconstruction:**	Manual

		.. grid-item-card::
			:margin: 0
			:columns: 6
			:class-card: sd-bg-secondary sd-text-white sd-rounded-3 sd-border-0
			:class-header: sd-bg-danger sd-rounded-3
			:class-footer: sd-bg-dark

			:fa:`radiation` **CT**
			^^^^^^

			.. image:: _images/Guides/SkullSegmentation/ImageContrast_CT.png
				:align: center
				:width: 400

			+++++
			.. raw:: html

				<iframe title="CT_Skull_decimated" frameborder="0" allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" allow="fullscreen; autoplay; vr" xr-spatial-tracking execution-while-out-of-viewport execution-while-not-rendered web-share width="300" height="200" src="https://sketchfab.com/models/30c5d657f68e47f99befd2a5a2c2889e/embed?autospin=0.5&autostart=1&ui_theme=dark"> </iframe>

			- **Scanner:** 			Epica Vimago CT
			- **Voxel size:**		0.2 mm  isotropic
			- **Scan duration:**	<1 minute
			- **Reconstruction:**	Automated


	The video below demonstrates how to segment a skull surface from a T1-weighted MRI using 3D Slicer. Note that this process requires the :bdg-link-primary:`SurfaceWrapSolidify <https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify>` extension, which can be easily installed via the :bdg-link-primary:`Extensions Manager <https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html>` wizard.

  	.. raw:: html

  		<iframe src="https://nih.app.box.com/embed/s/oo29puywnshxnlsda2xegnsfugvc080m?sortColumn=date&view=list" width="600" height="450" frameborder="0" allowfullscreen webkitallowfullscreen msallowfullscreen></iframe>

