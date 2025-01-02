.. _ImplantDesign:

================================================
:fa:`ruler-combined` Implant design
================================================

In contemporary experimental neuroscience there are a range of neural recording and stimulation techniques that require the surgical implantation of hardware. These range from micro-electrode recordings of extracellular action potentials ('spikes'), electrocorticography (ECoG) arrays measuring local field potentials (LFPs) at the cortical surface, optical imaging, and optical, chemical and electrical stimulation. Common to all of these methods is the need for any implanted hardware to be minimally disruptive of the subjects' normal behavior (e.g. minimizing size and weight and optimizing form factor), safe for long periods (e.g. mechanically robust, biocompatible, minimizing risk of infections).


Dual Chamber Parameters
==============================



Dual Chamber Parameters
==============================

.. image:: _images/Figures/Multidrive_parameters.png
  :align: right
  :width: 50%
  :alt: Parameters for a dual drive chamber


To accelerate and simplify the process of designing custom chambers for chronic electode recording implants using FreeCAD, the design of these chambers can be constrained and parameterized. The Python script `GenerateDualChamber.py <https://github.com/Phenomenal-Cat/IGNITE/blob/main/FreeCAD/GenerateDualChamber.py.FCMacro>`_ functions as a macro in :bdg-link-success:`FreeCAD <https://www.freecad.org>`.