---
title: "Magnetic Computed Tomography"
excerpt: "Development of novel backprojection algorithm of locally diverging fields."
header:
  teaser: /assets/images/MCT/sinogram.png
order: 1
share: false
toc: true
toc_sticky: true
---

## CT Background

Computed Tomography (CT) commonly refers to X-ray imaging technology. The core principle behind CT involves the interaction of X-rays with materials of varying densities. Denser materials scatter the X-rays, creating a "shadow" that can be measured to form an image. X-rays are used because their wavelengths are comparable to the spacing of atomic bonds, particularly covalent bonds, which are more prevalent than ionic bonds in biological materials. Other forms of electromagnetic imaging include gamma ray imaging (scintigraphy), thermal imaging, and radio telescopes.

<img src="{{ site.baseurl }}/assets/images/MCT/xray.jpg" alt="xray" style="width: 75%; display: block; margin: auto;">

MRI, or Magnetic Resonance Imaging, is also a magnetic scanning technology, but works quite differently from CT. In MRI, magnetic waves are used to align atoms in the same direction, and then radio waves are used to measure the energy of the atoms. Considering ideas from CT and MRI, Magnetic Computed Tomography uses magnetic waves to image non-ferrous metals similar to how X-rays image materials, but with a nonlinear imaging field like MRI. MCT equipment can be less expensive and safer than CT technology, and is useful for metals due to their unique magnetics attenuation properties like Skin Depth.

## Magnetics

Different materials respond uniquely to changes in magnetic flux. A material's resistance to magnetic flux is defined by its _permeability_. When exposed to changing magnetic fields, materials generate their own opposing magnetic fields, known as _eddy currents_. These currents are responsible for phenomena like magnetic braking, as demonstrated in the accompanying image, and why we can't put sharp metal objects in the microwave. The currents prefer to form in specific radii within a material, and sharp edges can disrupt the magnetic field lines, causing sparking. Factors such as geometry, magnetic properties (ferritity), and skin depth influence the formation of eddy currents, all of which are critical in reconstructing the internal geometry of a part during Magnetic Computed Tomography (MCT) imaging, based on the magnetic "shadow" detected on the sensor plane.

<img src="{{ site.baseurl }}/assets/images/MCT/eddy.gif" alt="EDDY" style="width: 75%; display: block; margin: auto;">

## Sinograms and Linear Backprojection

A 2D scan with any permeating field (light rays, electric fields, magnetic fields, etc) can be rotated and reconstructed to create a 2D scan of the object through time, representing a 3D object. This is called a _sinogram_.

<img src="{{ site.baseurl }}/assets/images/MCT/skullSino.gif" alt="sino" style="width: 65%; display: block; margin: auto;">

Sinograms are reconstructed to create a 3D spatial model through a process called back-projection.

<img src="{{ site.baseurl }}/assets/images/MCT/sinogramReco.gif" alt="back" style="width: 100%; display: block; margin: auto;">

## Nonlinear Backprojection

The good news about Computed Tomography techniques is that we have been developing them since the 70's! Most CT backprojection is relatively easy since the projection is itself linear and tractable due to the scanning beams linearity. Below is an image of the Feldkamp Davis-Kross (FDK) algorithm for conical beam reconstruction.

<img src="{{ site.baseurl }}/assets/images/MCT/conical.png" alt="con" style="width: 75%; display: block; margin: auto;">

Reconstruction of linearly scanned images is mathematically much easier than a locally diverging magnetic field. Magnodynamics is a field populated with mathematics, and theoretically the reconstruction should be calculatable. However, for any system there will be extraneous magnetic fields, losses, and other non-linearities. An empirically tested characterization and reconstruction framework allows for calibrations for exotic alloys and sensor drift among other things. The below image in an example of a sigma field constructed from the gradient of gaussians for simulation purposes.

<img src="{{ site.baseurl }}/assets/images/MCT/field.png" alt="field" style="width: 70%; display: block; margin: auto;">

## Software Structures

Given some imaged 3D volume and a 2D detector image through time (rotation / sinogram), some transformation matrix is needed between 2D space and 3D space to localize the measurements (pixels) on the detector to the 3D points (voxels) in the scan space. This high order transformation tensor is then used to backproject each 2D scan to create the 3D object. Technically, Maxwell's equations state magnetic fields are strictly convergent and the field lines do not cross. Compared to linear beam projection, magnetic fields are more complex and for our purposes... divergent within our scan space. This makes the mathematics to create the transformation matrix quite involved and worthy of a multi-semester undergraduate research project.

<img src="{{ site.baseurl }}/assets/images/MCT/magnofield.png" alt="mag" style="width: 50%; display: block; margin: auto;">

## Conclusion

With the BeamTeam at the Advanced Manufacturing Pilot Facility, I am developing novel reconstruction algorithms for non-linear inversely converging fields, building software to construct high order transformation matrices from measurement plane to scan volume for these fields, and proofing out the mathematics of the system as well as testing the physical device being built by the project lead. The software simulates the forward and backward problems (i.e. propogating a field through and predicting the sensor plane, or finding a field based on the sensor plane data).

I am also building software to run on our physical MCT system for scanning AM parts for defects during the printing process!

Some other aspects of the project I am working on are the mechatronics for controlling a massive variable capacitor, visualization techniques for educational purposes, and analytical geometrical theory. We are currently using _scutoids_ and _prismatoids_ to calculate the volume of magnetic field within a voxel of the scan region, and have tested using the more typical tetrahedrons with Delauney algorithms.
