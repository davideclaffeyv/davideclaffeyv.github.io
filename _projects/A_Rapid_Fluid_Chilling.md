---
title: "Rapid Beverage Chilling"
excerpt: "Exploring Interesting Heat Transfer Techniques for Chilling Coffee Startup"
header:
  teaser: /assets/images/Coffee/TEC.png
order: 5
share: false
toc: true
toc_sticky: true
---

## Introduction

In an attempt to rapidly cool "water" at 200C to 8C (403200 Joules) in under 5 minutes (1344 Watts) from a system that needs to steady state within 5 minutes, I have been exploring several interesting ways to transfer heat from one body to another. Refridgeration Cycles take too long to steady state, and most working fluids are toxic if leaked and ingested. Thus, we have been experimenting with turbulent air cooling techniques (Vortex Tubes), thermoelectric pumps (TECs), and some other novel heat pump technologies still in the research phase.

## Thermoelectric Heat Pumps

![TEC Theory]({{ site.baseurl }}/assets/images/Coffee/tectheory.png){: .align-center style="width: 75%;"}

Peltier modules work via the _Seebeck_ effect if generating electricity from a heat differential, or by the _Peltier Effect_ if pumping heat from input electricity. When creating electricity, these are called "TEGs" and when pumping heat, they are "TECs".

Peltiers work by separating two ceramic places with pairs of PN gates. When the electrons on either side of the gate are stimulated with electricity, they jump the gap and carry heat with them to the other plate. When the deltaT is high between the plates, the electrons likewise excite enough to cross the gap and create a voltage potential.

TECs have relatively complicated efficiencies that are low for high delta T hot side to cold side. Thus, it is important to cool the hot side sufficiently to maintain the highest efficiency possible for heat transfer. I modeled these effects in Matlab to determine how many modules we would need at what wattage to create the amount of heat transfer necessary for the project.

![TEC Matlab]({{ site.baseurl }}/assets/images/Coffee/tecMatlab.png){: .align-center style="width: 75%;"}

This was with 6 TEC modules of TEC12715.

We've lately been running physical experiments to prove out the assumptions of the model. Keeping the hotside of the TECs low enough to allow heat transfer has been difficult, and additionally we have not been able to source enough power for the system (1800 W).

![TEC Experiment]({{ site.baseurl }}/assets/images/Coffee/TECTEST.png){: .align-center style="width: 75%;"}

A shopvac provides air flow across the fins, which are thermally padded to the hot side of the modules. The cold sides are thermally greased to a chilling block, which has hot water pumped through at various rates. Temps are measured at the inlet and outlet of the block.

## Vortex Tubes

![Vortex Tech]({{ site.baseurl }}/assets/images/Coffee/VortexTech.png){: .align-center style="width: 75%;"}

Vortex Tubes were first accidently discovered by French Physics student Ranque, and later formalized by Hilsch. The action for how these tubes (with no moving parts!) separate air into cold and hot streams is still debated. The air coming into the tube is directed into a vortex, and one theory that I find easiest explained is that the hotter air has more energy and separates to the edges of the tube, escaping the hot end outlet while the inner lower energy air remains in the middle and escapes the cold side.

We designed a 3D printable vortx tube for our Form4s, and tested with 90 psi shop air.

![Vortex Test]({{ site.baseurl }}/assets/images/Coffee/vTest.png){: .align-center style="width: 75%;"}

We achieved -3 C on the cold end, and 30C on the hot end from 20C inlet air. Some initial tests showed relatively promising results: ~500 W of heat transfer from 200C water. The cold air from the tube was directed to the bottom of the vestibule to induce turbulence and further chill the water. We are currently redesigning the tube based on some Vortex Tube Geometry Optimization white papers.

## ThermoAcoustic Heat Pumps

While not tested, I thought it was interesting to list some of the other technologies we have thought about! Sound is, of course, areas of compressed and expanded air. From thermodynamic laws, the volume and temperature of a gas are tightly connected, and Thermoacoustic Heat Engines take advantage of this fact to pump heat with bass boosted sound waves. The theory is actually similar to how a sterling engine operates.

![Thermoacoustics]({{ site.baseurl }}/assets/images/Coffee/thermoA.png){: .align-center style="width: 75%;"}

## Shape Memory Alloy Heat Pumps

I have had some conversations with the material scientists in my additive shape memory lab who study the action of shape memory refridgeration systems. Shape memory alloys, and indeed any elastic like rubber bands, store energy when they are deformed. The entropy changes during this procedure is complicated and worth studying, but maybe not worth detailing in this blog. To see the power of shape memory alloy refridgeration, place a rubberband between your lips. Now pull on the sides, stretching the rubber band. The band should cool (i.e. pull heat from your lips). For a shape memory alloy, this phase change (solid-solid phase change) is endothermic, similar to how the latent heat works from a phase change of ice to water. Deforming a SMA, placing it in a closed volume, and allowing it to relax will move energy from the air to the element, which can then be pulled out and redeformed to continue the process! This effect is called the _Elastocaloric Effect_.

![SMA]({{ site.baseurl }}/assets/images/Coffee/elastic_theory.jpg){: .align-center style="width: 75%;"}
