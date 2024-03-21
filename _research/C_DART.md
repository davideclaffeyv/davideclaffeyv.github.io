---
title: "DART Labs Exoskeleton"
excerpt: "Researched and developed a pipeline that fully processed kinematic data from emg to motion primitive classification. Developed XGBoost model and training framework. Additional CAD Contributions and Motor Builds."
header:
  teaser: /assets/images/DART/DARTCOVER.png
order: 3
share: false
toc: true
toc_sticky: true
---

**Fall 2021 - Summer 2023**

![]({{ site.baseurl }}/assets/images/DART/Layout.png){: .align-center}
Researched and developed a pipeline that fully processed kinematic data from emg to motion classification. The first stage qualitatively analyzes EMG signals and filters out noisy trials. The second stage uses kinematics and movement vector estimation to segment trials in static, transition, and translation motion primitives. The third stage generated feature tables based on the MATLAB structures for the trials. Finally, several scripts were created to run varying machine learning analysis: forward feature selection of 289 features, exo-specific feature analysis, confusion matrices, window and increment size sweeps, and hyperparameter grid sweeps that utilized Bayes and DART XGBoost boosters and optimizers to find high accuracy models.
## Hip Torque Pipeline

With OpenSim and Matlab, I refactored a legacy code base to automatically process subject trials, auto-scale digital skeleton with static trial information, assign marker location for accurate tracking, and extract position, orientation, and inertial data.

Calculating inverse dynamics is a computationally expensive process. The goal of this project was to create a data set of kinetics and kinematics for 10 sets of subject joints in order to train a model to predict such dynamics.

![]({{ site.baseurl }}/assets/images/DART/image11.png){: .align-center}

## IMU Data and Channel Filtering for Model Training 

From the gigabytes of data developed in the Hip Torque Pipeline, 238 feature signals needed selected and conditioned for XGBoost training. Partly automated with matlab filtering, and manual qualitative analysis, 1000 feature tables were generated between the 10 subjects. Additionally, feature extraction calculated and saved motion primitive data labels: whether the subject was static, moving (and in what direction) or rotating. 

![]({{ site.baseurl }}/assets/images/DART/channel.png){: .align-center}
![]({{ site.baseurl }}/assets/images/DART/feature.png){: .align-center}

## XGBoost Model Training, Hyperparameter Tuning, and RasPi Implementation

With feature tables at hand, I developed an XGBoost model and tuning framework to explore various hyperparameters and their convergence. I used WandB to visualize the training methods and monitor through the cloud. The final subject independent model had a prediction accuracy of 90-95% with various tree pruning, subsampling, and estimator numbers applied. Finally, forward feature analysis was done to select what channels from the IMU were most important to reduce the size of the model. 

Implementation on the exoskeleton was smooth and accuracy up to 90% for an unseen subject. 

![]({{ site.baseurl }}/assets/images/DART/hyperparam2.png){: .align-center}![]({{ site.baseurl }}/assets/images/DART/image20.png){: .align-center}
![]({{ site.baseurl }}/assets/images/DART/image18.png){: .align-center}![]({{ site.baseurl }}/assets/images/DART/image24.png){: .align-center}

## CAD Contributions and Misc. 

In addition to the software work, I also worked on some CAD projects and motor reconstruction. 

### Exoskeleton Framing 

![]({{ site.baseurl }}/assets/images/DART/exoskeleton.png){: .align-center}
![]({{ site.baseurl }}/assets/images/DART/image10.png){: .align-center}
![]({{ site.baseurl }}/assets/images/DART/image1.png){: .align-center}
![]({{ site.baseurl }}/assets/images/DART/motorBoc1.png){: .align-center}
![]({{ site.baseurl }}/assets/images/DART/motorBox2.png){: .align-center}

### Motor Rebuild

![]({{ site.baseurl }}/assets/images/DART/image17.jpg){: .align-center}
![]({{ site.baseurl }}/assets/images/DART/image5.jpg){: .align-center}
![]({{ site.baseurl }}/assets/images/davidPhotos/IMG_3062.JPG){: .align-center}

### Studies I was a Subject in or Helped Run 
- Walking Assistance Metabolic Cost Improvement Study
- Gait Prediction from Limited Ankle IMU Data
- Torsional Redirection of Subjects Around an Obstacle with Artificial Potential Fields
- Sprint Assistance and Speed 

![]({{ site.baseurl }}/assets/images/davidPhotos/IMG_4064.HEIC){: .align-center}
![]({{ site.baseurl }}/assets/images/davidPhotos/IMG_4065.HEIC){: .align-center}

## Publication 

[Under Review]

