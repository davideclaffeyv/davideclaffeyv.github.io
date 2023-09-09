---
title: "Chaotic Pendulum with Dead Reckoning"
excerpt: "A project designed around modular develop and study of the chaotic movement of a double, triple, or quadruple pendulum."
header:
  teaser: /assets/images/projects/pend.jpg
order: 3.1
share: false
toc: true
toc_sticky: true
---
## Introduction 

This project was undertaken to further explore controls and chaotic systems. A double pendulum is an example of a chaotic controls system. The goal of this project was to drive a linear rail to balance such a pendulum. This sort of project has been done with various tracking techniques for each joint. We opted for a modular design so that more linkages could be added later on to experiment with triple or quadruple linkage pendulums. 

![Linear Rail]({{ site.baseurl }}/assets/images/photos/linear.png){: .align-center}

## Design 

![Module]({{ site.baseurl }}/assets/images/projects/modPend.png){: .align-center}

Each module consists of an IMU (Inertial Measurement Unit), ESP32 Wi-Fi module, and arduino nano. Integrating acceleration from initial velocity and position terms to calculate position is known as dead reckoning, and generally considered a poor choice for position calculation. 

![Pully for belt drive]({{ site.baseurl }}/assets/images/projects/pend_gear.png){: .align-center}

The modules would compute this position on the onboard nano, and send the position to the Arduino Mega running the linear rail. 

![Simple Simulation]({{ site.baseurl }}/assets/images/projects/hamiltonian_sim.png){: .align-center}

We developed simulation for such a system using the Hamiltonian equations of a double pendulum, and experiment with base velocity inputs. 

![Soldering]({{ site.baseurl }}/assets/images/projects/pendSolder.png){: .align-center}

Unfortunately, once assembled the project went on the back burner to some other cool projects but hopefully one day it will be revisited and tested. 