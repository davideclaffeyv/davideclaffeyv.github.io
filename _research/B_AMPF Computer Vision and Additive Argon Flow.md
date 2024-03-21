---
title: "Advanced Manufacturing Argon Flow for DED"
excerpt: "Using OpenCV, Python, Fluid Mechanics, and DAQ to automate the monitoring and control of argon flow rates for the Optomec DED Additive CNC"
header:
  teaser: /assets/images/AMPF/ded_cover.png
order: 2
share: false
toc: true
toc_sticky: true
---

## Introduction 

In lieu of the 2022 national AIM grant, the AMPF is automating a large portion of the additive metal machinery for mass physical data collection and processing in order to further study these advanced manufacturing techniques. 

![Optomec DED Hybrid Machine]({{ site.baseurl }}/assets/images/AMPF/Optomec.png){: .align-center}

The Optomec delivers powdered metals to a weld pool formed by lasers on top of metal substrate. This entire process is done in an inert environment of argon. Argon is also used to deliver the powdered metal to the pool. 

There currently lacks a standard flow rate for argon delivery of varying materials (this changed based on material/thermal properties, weight, etc). The argon also fluctuates across the building as the tank depletes and other machines are used in tandem. 

The Purpose of this project is to create a cost-effective reliable apparatus to measure and set argon flow rate using computer vision and stepper motors. The end product should be able to incorporate gcode instructions that set the argon flow rates for each hooper during toolpath generation.

## What is DED?

![Image from sciencedirect.com]({{ site.baseurl }}/assets/images/AMPF/DED_science_direct.png){: .align-center}

Directed Energy Deposition, or DED, is an advanced manufacturing technique for metal printing. Typically the stock media is powder or filament fed through a nozzle to intercept laser energy. Powder is advantageous due to the ability to mix several powders when printing. However, precise Mass Flow calculations are necessary to predict and command certain percentages of materials. 

## Problems with Mass Flow

Mass flow is a tricky measurement to make through a powder flowing tube. AMPF is engaged in several methods of measuring Mass flow, most having to do with measuring aspects of mass flow that can be correlated. Examples are number of impacts of individual powders on a piezoelectric sensor, correlating the argon flow rate with the mass rate, measuring capacitance of the flow, and measuring magnetic fluctuations through the flow. 

![]({{ site.baseurl }}/assets/images/AMPF/ArgonCal){: .align-center}

Argon Rotameters are cheap and vastly used, however the measurements are taken by eye, and argon levels have been shown to fluctuate and drop during a print due to building argon levels and machine use. Sensors that do this sort of monitoring are expensive and hard to scale. 

![]({{ site.baseurl }}/assets/images/AMPF/hopper.png){: .align-center}

## Computer Vision Rotameter Monitoring

One low cost solution to monitoring and dynamically setting flow rate is using computer vision to track the rotameters. Getting accurate measurements is a balance of distance to the rotameter and the distortion and lighting of the scene. Distance to measurement matters because the more pixels you can fit into an area allows for higher tolerance of measurement even with subpixel analysis. 

![System CAD]({{ site.baseurl }}/assets/images/AMPF/CameraCAD.png){: .align-center}

![Monitoring System]({{ site.baseurl }}/assets/images/AMPF/cameraDistortion.png){: .align-center}

Several methods were employed to correct for camera distortion, machine vibration, and nonlinear rotameter scales. 

This was my first computer vision project, and it gave me a sense of appreciation for the complexity of CV calculations, filtering, convolutions, and tracking. 

## Flowmeter Communication

When I had returned from an internship, a new cheap flowmeter had just hit the market. The project thus pivoted to developing a code base to interact with these meters through modbus protocol for a smaller footprint flow control system. 

[Updates Coming!]