---
title: "CNN to Lego Construction"
excerpt: "Fueled by my interests in general assembler robotics, this project aims to use CNN and complex control to assemble 1st grade level legos from an instruction booklet. "
header:
  teaser: /assets/images/projects/arm.png
order: 3.1
share: false
toc: true
toc_sticky: true
---

I am in the process of developing a robotic arm that uses an Arduino Mega, Raspberry Pi, AX12a Servos, machined gripper, convolutional neural networks, high-fidelity part imaging, and path planning to process instruction manuals *hopefully* assemble simple lego sets.

![Arm CAD]({{ site.baseurl }}/assets/images/projects/armCAD.png){: .align-center}

So far, I've reprogrammed the servos and set up large-packet serial communication between the Raspberry pi and Arduino Mega. The pi is currently able to sent commands to the servo chain and receive information back such as temperature, load, voltage, and position. The gantry will utilize CoreXY control to move the robot base. CoreXY allows for fast and precise geometric calculation of the change in position, and it's simply a cool method that I wanted to test knowledge by building.

![Arm CAD]({{ site.baseurl }}/assets/images/projects/armforward.png){: .align-center}

The script on the py will use PyBullet, OpenCV, and possibly ROS to output movement commands to the arm. The arm will return actual positions, and through this pattern of forward and inverse dynamics and kinematics I expect the position error to be minimized. On the software side, I wrote and trained a lego generator to adversarially train the lego classifier. Initial tests only showed accuracy around 60%, and I decided to focus the project by already having the legos sorted and ID'd before contruction. 

![Lego Generator]({{ site.baseurl }}/assets/images/projects/generatoroutput.png){: .align-center}

The lego building algorithm will either used a lego brick classifier (which I have already trained) or a library of lego parts with their respective part number that is given at the front of the instruction booklets. The program will use convolutional neural networks and path planning to process the assembly manuals and plan construction of the legos. 

[PROGRESS COMING SOON]
