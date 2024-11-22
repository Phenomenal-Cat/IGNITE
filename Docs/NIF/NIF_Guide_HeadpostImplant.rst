.. _NIF_HeadpostImplant:

=====================================
MR-compatible headpost implantation
=====================================

.. figure:: ../_images/Guides/HeadpostImplants/Headpost.jpg
  :width: 200
  :align: right

It is critical for subjects to maintain a stable head position during
fMRI data acquisition in order for the data to be usable. While motion
correction processing can compensate for small deviations in head position across
volumes within a run, larger movements typically require researchers to
exclude data.

.. panels::
  :column: col-lg-12 p-0 border-1
  :header: bg-warning text-bold text-dark p-1
  :body: bg-warning text-dark border-0 p-2 
  
  :fa:`exclamation-triangle` **Disclaimer**
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  This page provides information about methods and materials that have previously been used successfully by NIF researchers to implant MR-compatible headpost hardware on adult NHPs for head restraint during fMRI. However, the NIF makes no guarantee as to the longevity of implants using these methods. 

.. contents::
  :local:


Headpost Design
==================

The criteria for an implanted headpost design are that it must be MR-compatible, strong enough to withstand the forces exerted by an adult NHP, and biocompatible. While the search for better solutions in this area is ongoing (`Mulliken et al.,
2015 <https://doi.org/10.1016/j.jneumeth.2014.12.011>`_; `Ortiz-Rios et al.,
2018 <https://doi.org/10.1016/j.jneumeth.2018.09.013>`_; `Blonde et al., 2018 <https://doi.org/10.1016/j.jneumeth.2018.04.016>`_), the `NIMH Section on Instrumentation <https://www.nimh.nih.gov/research/research-conducted-at-nimh/research-areas/research-support-services/section-on-instrumentation>`_ who designs and fabricates headposts for the NIF has currently settled on `G10 fiberglass <https://en.wikipedia.org/wiki/G-10_(material)>`_. The benefits of G10 are that is has a tensile strength ~3 times greater than `polyether ether ketone (PEEK) <https://en.wikipedia.org/wiki/Polyether_ether_ketone>`_ and a flexural modulus 2 orders of magnitude lower. Consequently, G10 headposts never break - the ceramic screws or acrylic will instead be the weakest link of the implant. However, G10 is more difficult to machine and cannot be 3D printed, making it more difficult to customize.


NIMH Octagon
--------------

.. image:: ../_images/Guides/HeadpostImplants/NIH_OctagonHeadposts.jpg
  :width: 30%
  :align: right

The octagonal headpost design was developed by David Ide at the `NIMH Section on Instrumentation <https://www.nimh.nih.gov/research/research-conducted-at-nimh/research-areas/research-support-services/section-on-instrumentation>`_ around 2016 following multiple headpost design iterations. The symmetrical design maximizes surface area contact between the implanted headpost and the holder, which is press-fit and released via a central PEEK rod that threads into the central hole. Both the headpost and the holder are machined from G10 fiberglass at the NIMH machine shop and can be customized with the base cut at an angle depending where on the skull it will be implanted.

  .. container:: clearer
     .. image :: ../_images/spacer.png
        :width: 1

.. dropdown:: :opticon:`info,mr-1` **NIH Octagon Headpost Materials**
  :open:
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :body: bg-dark

  .. image:: ../_images/Guides/HeadpostImplants/NIH_OctagonHeadpostDesign.png
    :width: 30%
    :align: right

  .. csv-table::
    :file: ../_static/CSVs/NIF_HeadpostHolder_BOM.csv
    :align: left
    :header-rows: 1
    :widths: auto

  .. container:: clearer
     .. image :: ../_images/spacer.png
        :width: 1


Commercial Trapezoid
------------------------------

.. image:: ../_images/Guides/HeadpostImplants/NIH_TrapezoidHeadpost.jpg
  :width: 20%
  :align: right

A trapezoid shaped headpost has been offered by some commercial vendors (e.g. the PEEK version pictured here from Applied Prototypes, who are no longer in business). This design adds two through-holes for screwing the headpost holder securely to the headpost. This design can also be fabricated from G10 fiberglass by the `NIMH Section on Instrumentation <https://www.nimh.nih.gov/research/research-conducted-at-nimh/research-areas/research-support-services/section-on-instrumentation>`_, with optional base angle customization, as pictured.


Crist Cylindrical
------------------

.. image:: ../_images/Guides/HeadpostImplants/Crist_CylindricalHeadpost.jpg
  :width: 20%
  :align: right

`Crist Instruments <https://www.cristinstrument.com/products/implant-intro/head-holders-on-head>`_ offer their hollow cylindrical style of headposts in several MR-compatible materials, including `Cilux` (6-FHP-J1) (which is essentially Ultem 1010 - pictured) and PEEK (6-FHP-K1), as well as Titanium, which is MR-safe but not recommended for MRI projects. As mentioned above, these materials are substantially weaker than G10 and we do not recommend them for use with larger animals.


Materials
=============

Bone screws
--------------

MR-compatible bone screws can be ceramic (typically zirconium dioxide, but also calcium phosphate) or thermoplastic (PEKK, PEEK, Ultem). Ceramic has greater strength than thermoplastics and is typically preferred, although its higher density does cause more starburst artifacts in CT images.


.. dropdown:: :fa:`screwdriver-wrench` **Thomas Recording ceramic screws**
  :open:
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :body: bg-dark

  .. image:: ../_images/Guides/HeadpostImplants/Tools/TRec_screws.jpeg
    :width: 40%
    :align: right

  `Thomas Recording <https://www.thomasrecording.com/screws>`_ ceramic screws are composed of Zirconium dioxide and are available in a range of lengths. NIH labs using these screws for MR-compatible macaque cranial implants have typically used the SA45 size, which has a 4mm hexagonal head, with a 4.5 mm length thread. This length allows the head of the screw to sit above the outer skull surface with the threads fully engaged so that acrylic can flow beneath the screw head. These screws should not be driven all the way into the skull since the macaque skull is less than 4.5mm thick in most places, and doing so would therefore cause the screw to press against the dura. Note also that, although third-party tools are available and have been used successfully to implant TRec screws (e.g. Wiha drivers and Synthes drills and taps), Thomas Recording do manufacture their own tool sets, which they recommend using.
  
  .. image:: ../_images/Guides/HeadpostImplants/Tools/TRec_ScrewKit.jpg
    :width: 70%
    :align: left

  .. csv-table:: 
     :file: ../_static/CSVs/NIF_Surgical_TRecScrewKit.csv
     :widths: auto
     :align: left
     :header-rows: 1


.. dropdown:: :fa:`screwdriver-wrench` **Rogue Research ceramic screws**
  :open:
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :body: bg-dark

  .. image:: ../_images/Guides/HeadpostImplants/Tools/Rogue_screws.png
    :width: 20%
    :align: right

  `Rogue Research <https://www.rogue-research.com/veterinary/tools-implants/>`_ ceramic screws are another Zirconium dioxide option, available in different lengths. The NIF and SCNI recently started using these screws based on the fact that the threads form a tighter seal with the cranial bone. Rogue screws use a standard Philips head and are provided with a drill and tap set suitable for the 3 mm diameter screw threads.


Other sources of MR-compatible bone screws for securing headposts include `Grey Matter Research <https://www.graymatter-research.com/bone-screws/>`_ and `Crist Instruments <https://www.cristinstrument.com/products/implant-intro/fasteners-bone-screws>`_. 


Adhesives
--------------


Adhesive: `Bisco All Bond Universal <https://www.bisco.com/all-bond-universal-/>`_
Cement: `Bisco Duo-Link Universal <https://www.bisco.com/duo-link-universal-/>`_ 

`Denmat Geristore <https://www.denmat.com/products/restorative/ionomers.html>`_
`BioMet Palacos R <https://www.zimmerindia.com/medical-professionals/products/surgical-and-operating-room-solutions/palacos-bone-cements.html>`_







For example, coating MR-safe materials with hydroxylapatite to promote osseointegration (`Ortiz-Rios et al., 2018 <https://doi.org/10.1016/j.jneumeth.2018.09.013>`_).




Headpost Implant Surgery
============================

Preparation
-------------

Scheduling a surgery
~~~~~~~~~~~~~~~~~~~~~~~~~

In order to schedule a surgery for NHPs in Bld 49, you will need to contact one of VMRB's lead technicians responsible for scheduling the operating rooms (ORs) to find a currently available date:

`Johnetta Gray Forgy <https://ned.nih.gov/search/ViewDetails.aspx?NIHID=0010188753>`_, VMRB Lead Technician

  - :fa:`envelope` **E-mail:** grayj@mail.nih.gov
  - :fa:`phone` **Office:** +1 301-496-0717

Once you have established an available OR slot, you will need to submit the VMRB Surgical request Form *and* a copy of the animal's transfer sheet via e-mail to VMRBTechnicalRequest@mail.nih.gov. The request form as well as an example can be downloaded using the buttons below. 

.. link-button:: ../_static/PDFs/Forms/CAF_SurgicalRequestForm.pdf
    :type: url
    :text: PDF
    :classes: btn-primary

.. link-button:: ../_static/PDFs/Forms/CAF_SurgicalRequestForm_Annotated.pdf
    :type: url
    :text: Example
    :classes: btn-success


.. panels::
  :column: col-lg-12 p-0 border-1
  :header: bg-primary text-bold p-1 pl-2
  :body: bg-secondary border-0 p-2

  :opticon:`info,mr-1` **Note**
  ^^^^^^^^^^^^^^^^^^^^^^^^

  Note that even though the VMRB surgical request form claims that it must be submitted "48 hours" in advance of the surgery date, the surgery is not booked until VMRB sends a confirmation e-mail that they have processed the forms. It is therefore recommended to submit the surgical request form immediately once you have ascertained an available date.


Tools and sterilization
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../_images/Guides/HeadpostImplants/SCNI_PrepRoomCabinet.jpg
  :width: 20%
  :align: right

- Pre-made octagonal G10 headposts and ceramic screws (both Thomas Recording and Rogue Research) are located in the `Blickman cabinet <https://www.blickman.com/category/cabinets>`_ in the :ref:`SCNI planning room (B1C68) <NIF-facility>`. 

.. image:: ../_images/Guides/HeadpostImplants/CAF_B1S43_ETOshelf.jpg
  :width: 20%
  :align: right

- These items will need to be `Ethylene oxide (ETO) <https://www.fda.gov/medical-devices/general-hospital-devices-and-supplies/sterilization-medical-devices#ethylene>`_ gas sterilized by taking them to the :ref:`CAF Instrument Preparation Room (B1S43) <NIF-facility>`, packing them into a gas-sterilization bag and placing it on the metal rack at the back of the room. CAF personnel will put items left on this rack into gas sterilization around 2:00pm daily. You can enter the CAF from the B1C63 entrance (opposite the SCNI lab office), with appropriate badge access, but you must not enter the surgical suite without a Tyvek coverall or surgical scrubs, hair bonnet, shoe covers and a face mask. 

.. image:: ../_images/Guides/HeadpostImplants/CAF_B1S43_Blickman.jpg
  :width: 20%
  :align: right

- Items for gas sterilization should be placed in a bag (available from the Blickman cabinets in B1S43) along with a GasChecks test strip and sealed. Each bag should be labelled with the date as well the group / OR it belongs to.

- An appropriate :ref:`stereotaxic frame <Stereotaxes>` should be selected and reserved if necessary. The stereotax should be sterilized by...

.. image:: ../_images/Guides/HeadpostImplants/CAF_OR3_Blickman.jpg
  :width: 20%
  :align: right

- The following pre-sterilized 'standard' surgical kits and equipment should be located and checked prior to the surgery:

  1. Standard Leopold surgical pack
  2. Standard Leopold head frame
  3. Manual drill and threading kit (Rogue Research *or* Thomas Recording)
  4. Cautery tools



.. dropdown:: :fa:`screwdriver-wrench` **Standard Leopold surgical packs**
  :open:
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :body: bg-dark

  The standard surgical pack for the Leopold groups includes the various tools required for nearly any surgery, but does not include more specialized tools for specific types of procedure.

  .. image:: ../_images/Guides/HeadpostImplants/Tools/Surgical_LeopoldStdPack.jpeg
    :width: 75%
    :align: left









