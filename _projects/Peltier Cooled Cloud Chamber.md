---
title: "Peltier Cloud Chamber"
excerpt: "Who doesn't want to view subatomic particles flying through our atmosphere? A Cloud chamber is a relatively old-school device for subatomic particle viewing."
header:
  teaser: /assets/images/finCloud.jpg
order: 3.1
share: false
toc: true
toc_sticky: true
---

## What is a Cloud Chamber? 

Cloud chambers were used in theoretic physics antiquity to view subatomic particles. They were originally invented by Charles Wilson in 1911 to study cloud formation. Fundamentally all that is required is a saturated vapor such as Isopropyl Alcohol that will ionize as electrically charged particles fly through. Thus, any neutral charged particles such as neutrons and Z bosons will not be visible. To achieve the saturated vapor, a chamber with Isopropyl and a temperature gradient is required. Typically, this gradient is achieved from room temp to dry ice. 

![cloud]({{ site.baseurl }}/assets/images/cloud.png){: .align-center}

I went to the gas station and they didn't have dry ice, so I decided instead to create a temperature gradient with stacked peltier coolers. 

## Peltier Coolers

Peltier coolers are semiconductor plates that generate heat transfer through the peltier effect. By passing an electrical current through the device, alternating P and N type gates move electrons, transferring heat. 

![peltier]({{ site.baseurl }}/assets/images/peltier.png){: .align-center}

## Overall Design

Inspired by several other projects, I decided to use stacked peltier coolers to create a higher temperature gradient at lower power, and a CPU cooler to dissipate the heat on the bottom of the cooler stack. Additionally, I machined a copper housing for the plates so that they maintain proper contact (aided by thermal paste) and more efficiently transfer heat out of the IPA chamber. Additionally, I'd like to use computer vision to view the chamber for large periods of time and document/identify particles as they pass through. Particles can be identified by the radius of their trail depending on electronegativity and the straightness of the trail depending on inertia and mass. Higher mass higher speed particles leave straight trails, for example. 

![cpu]({{ site.baseurl }}/assets/images/cpuF.png){: .align-center}

![draw]({{ site.baseurl }}/assets/images/cloudDraw.png){: .align-center}

## Construction

Materials 
- 1/4 x 2 x 12 in 110 copper flat bar 
- CPU Heat Sink and Fans
- Variable 6-30 V 150 W Buck Converters
	- https://www.amazon.com/Converter-1-25-30V-Regulator-Constant-Charging/dp/B08HS76XG1/ref=cm_cr_arp_d_product_top?ie=UTF8
- Acrylic Sheet
- Iso Alcohol
- 24 V power supply
- LCD Screen 
- LED (to backlight the chamber)
