.. _ImplantDesign:

================================================
:fa:`ruler-combined` Implant design
================================================

In contemporary experimental neuroscience there are a range of neural recording and stimulation techniques that require the surgical implantation of hardware. These range from micro-electrode recordings of extracellular action potentials ('spikes'), electrocorticography (ECoG) arrays measuring local field potentials (LFPs) at the cortical surface, optical imaging, and optical, chemical and electrical stimulation. Common to all of these methods is the need for any implanted hardware to be minimally disruptive of the subjects' normal behavior (e.g. minimizing size and weight and optimizing form factor), safe for long periods (e.g. mechanically robust, biocompatible, minimizing risk of infections).


Dual Chamber Parameters
==============================


.. grid::

  .. grid-item::
    :columns: 8
    :margin: 0
    :padding: 0 0 0 3


    To accelerate and simplify the process of designing custom chambers for chronic electode recording implants using :bdg-link-success:`FreeCAD <https://www.freecad.org>`, the design of these chambers can be constrained and parameterized. The Python script :bdg-link-primary:`GenerateDualChamber.py <https://github.com/Phenomenal-Cat/IGNITE/blob/main/FreeCAD/GenerateDualChamber.py.FCMacro>` functions as a macro in FreeCAD, and takes user-specified parameters (illustrated in the figure on the right and listed in the table below) to automatically generate a CAD design for a 'dual chamber' that can accommodate two :ref:`MBA electrodes <MicrowireArrays>` with independent microdrives. 

  .. grid-item::
    :columns: 4
    :margin: 0
    :padding: 0 0 2 0

    .. image:: _images/Figures/Multidrive_parameters.png
      :align: right
      :width: 100%
      :alt: Parameters for a dual drive chamber


:fa:`bullseye` Post-surgical Localization Grid 
======================================================

In 2-step surgery procedures, such as those used for the implantation of chronic :ref:`microwire bundle array electrodes <MBAs>`, researchers acquire MRI and/ or CT images between the first and second surgery. These data are used to verify the accuracy of the chamber implant relative to the neuronal recording or stimulation target, and to calculate where the electrode needs to be positioned in *chamber coordinates* (as opposed to stereotaxic coordinates) in order to reach the target. To achieve this, we generate a 'scan grid' that will be inserted into the implanted chamber during imaging, allowing us to visualize the grid holes. 

This grid scan method derives from a practice used to localize acute recordings with MRI. However, in that practice, the grid being visualized is typically the actual grid being used to insert guide tubes and electrodes into the brain, and is therefore subject to additional geometrical constraints (e.g. a need for many densely arranged and narrow diameter grid holes). In the chronic recording method, our scan grid is only used for the scan and then discarded, so the geometry is much more flexible and can instead be optimized for image acquisition. For example, since a standard voxel size might be 0.5mm isotropic in a whole brain T1w scan of a large animal in a 3T MRI, we should ensure that each grid hole has a large enough diameter to avoid partial volume effects.



Preparing the grid
=====================

MR and CT-contrast agents can be used to improve visualization of the grid holes

- Magnevist (`gadopentetate dimeglumine <https://en.wikipedia.org/wiki/Gadopentetic_acid>`_) - 469.01mg / ml
- Ablavar (`gadofosveset <https://en.wikipedia.org/wiki/Gadofosveset>`_ trisodium) - 244mg / ml



