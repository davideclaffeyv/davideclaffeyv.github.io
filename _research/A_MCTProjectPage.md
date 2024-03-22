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
Computed Tomography, or CT, is typically in reference to X-ray imaging technology. The fundamental idea begind the technology is that rays of light will interact with different densities of materials uniquely. Denser material will scatter the X-rays, and this "shadow" is then measured. X-rays are used since their wavelengths are on the order of the spacing of most atomic bonds, especially covalent bonding (more common than ionic for biological materials). Gamma ray imaging (scintigraphy), thermal imaging, and radio telescopes are all examples of electromagnetic imaging. 

<img src="{{ site.baseurl }}/assets/images/MCT/xray.jpg" alt="xray" style="width: 75%; display: block; margin: auto;">

MRI, or Magnetic Resonance Imaging, is also a magnetic scanning technology, but works quite differently from tomography. In MRI, magnetic waves are used to align atoms in the same direction, and then radio waves are used to measure the energy of the atoms. Magnetic Computed Tomography will use magnetic waves to image non-ferrous metals similar to how X-rays image materials, and is ideal for metals due to their unique magnetic properties. Additionally, MCT equipment is less expensive and safer than CT technology. 

## Magnetics

Magnetic Computed Tomography takes advantage of the properties of a magnetic field to image materials. Various materials react different to magnetic flux, particularly the change in magnetic flux. A material's magnetic resistance is known as its *permeability*. The way a material resists a magnetic field change is by creating magnetic fields of its own, known as *Eddy Currents*. Eddy currents are responsible for the phenomena of magnetic braking, shown in this gif. Eddy currents are also why metal should not go into microwaves. Eddy currents want to form certain radii within a material, and if the material has sharp edges, the currents will spark where the edge breaks up the field line. This is a brief simplification of eddy currents, and more rigorous proofs exist online for further details. Geometry, ferritity, and a property called "skin depth" all affect how eddy currents are formed, and thus are necessary when reconstructing the internal geometry of an MCT scanned part from the magnetic "shadow" formed on the detector. 

<img src="{{ site.baseurl }}/assets/images/MCT/eddy.gif" alt="EDDY" style="width: 75%; display: block; margin: auto;">

## Sinograms and Linear Backprojection

A 2D scan with any permeating field (light rays, electric fields, magnetic fields, etc) can be rotated and reconstructed to create a 2D scan of the object through time, representing a 3D object. This is called a *sinogram*. 

<img src="{{ site.baseurl }}/assets/images/MCT/skullSino.gif" alt="sino" style="width: 65%; display: block; margin: auto;">

Sinograms are reconstructed to create a 3D spatial model through a process called back-projection. 

<img src="{{ site.baseurl }}/assets/images/MCT/sinogramReco.gif" alt="back" style="width: 100%; display: block; margin: auto;">

## Nonlinear Backprojection

The good news about Computed Tomography techniques is that we have been developing them since the 70's! Most CT backprojection is relatively easy since the projection is itself linear and tractable due to the scanning beams linearity. Below is an image of the Feldkamp Davis-Kross (FDK) algorithm for conical beam reconstruction. 

<img src="{{ site.baseurl }}/assets/images/MCT/conical.png" alt="con" style="width: 75%; display: block; margin: auto;">

Reconstruction of linearly scanned images is mathematically much easier than a locally diverging magnetic field. Magnodynamics is a field populated with mathematics, and theoretically the reconstruction should be calculatable. However, for any system there will be extraneous magnetic fields, losses, and other non-linearities. An empirically tested characterization and reconstruction framework allows for calibrations for exotic alloys and sensor drift among other things. 

<img src="{{ site.baseurl }}/assets/images/MCT/field.png" alt="field" style="width: 100%; display: block; margin: auto;">

## Software Structures

Given some imaged 3D volume and a 2D detector image through time (rotation / sinogram), some transformation matrix is needed between 2D space and 3D space to localize the measurements (pixels) on the detector to the 3D points (voxels) in the scan space. This high order transformation tensor is then used to backproject each 2D scan to create the 3D object. Technically, Maxwell's equations state magnetic fields are strictly convergent and the field lines do not cross. Compared to linear beam projection, magnetic fields are more complex and for our purposes... divergent within our scan space. This makes the mathematics to create the transformation matrix quite involved and worthy of a multi-semester undergraduate research project. 

<img src="{{ site.baseurl }}/assets/images/MCT/magnofield.png" alt="mag" style="width: 50%; display: block; margin: auto;">

## Conclusion

With the BeamTeam at the Advanced Manufacturing Pilot Facility, I am developing novel reconstruction algorithms for non-linear inversely converging fields, building software to construct high order transformation matrices from measurement plane to scan volume for these fields, and proofing out the mathematics of the system as well as testing the physical device being built by the project lead.

<img src="{{ site.baseurl }}/assets/images/MCT/prettyorder.png" alt="mag" style="width: 75%; display: block; margin: auto;">
(What DALL-E thinks a 5th order rank 3 tensor looks like)

Publications coming soon!