cmake_minimum_required(VERSION 3.16.3...3.19.7 FATAL_ERROR)

project(IGNITE)

#-----------------------------------------------------------------------------
# Extension meta-information
set(EXTENSION_HOMEPAGE "https://www.slicer.org/wiki/Documentation/Nightly/Extensions/IGNITE")
set(EXTENSION_CATEGORY "Custom")
set(EXTENSION_CONTRIBUTORS "Aidan P. Murphy (National Institutes of Health)")
set(EXTENSION_DESCRIPTION "Imaging-Guided Neural Implant Targeting Extension")
set(EXTENSION_ICONURL "https://www.example.com/Slicer/Extensions/IGNITE.png")
set(EXTENSION_SCREENSHOTURLS "https://www.example.com/Slicer/Extensions/IGNITE/Screenshots/1.png")
set(EXTENSION_DEPENDS "NA") # Specified as a list or "NA" if no dependencies

#-----------------------------------------------------------------------------
# Extension dependencies
find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})

#-----------------------------------------------------------------------------
# Extension modules
add_subdirectory(AlignStereotax)
add_subdirectory(NIF_Import)
## NEXT_MODULE

#-----------------------------------------------------------------------------
include(${Slicer_EXTENSION_GENERATE_CONFIG})
include(${Slicer_EXTENSION_CPACK})
