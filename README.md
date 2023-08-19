# SantiScan

## 🦠 Introduction
  This product was a collaboration between 

## Hardware

## Pretraining

## 🛠 Process

  1. #### On-Device processing
     - The ESP32-CAM board captures and saves a video to its SD card each time the sanitizer is dispensed
     - When the user walks away, each of these 15 frames are uploaded to a Google Colab notebook
  2. #### Data Cleaning 
     - A machine learning algorithm, [Mediapipe](https://google.github.io/mediapipe/solutions/face_mesh.html), locates each joint of the hand
     - These 20 points are used to perfectly mask the hand from its background using the [Segment Anything](https://github.com/facebookresearch/segment-anything.git) approach
  3. #### Hand Recognition
     - Now that every frame only contains data about the palm, 
     ![Screenshot 2023-08-18 at 4 43 41 PM](https://github.com/NoahBSchwartz/SantiScan/assets/44248582/4ba95f6c-d22e-4841-960e-10981f5f12d1)

ㅤ


## 🎉 Result
In person, the effect is convincing enough to give the illusion of looking through the screen. In fact, it's more effective than 3D glasses in some cases because of the head tracking.

ㅤㅤㅤㅤㅤㅤ![unnamed__4_-removebg-preview](https://github.com/NoahBSchwartz/SantiScan/assets/44248582/3eeae46e-b1d2-4cdd-91ca-6b222211ae1a)
![unnamed__5_-removebg-preview](https://github.com/NoahBSchwartz/SantiScan/assets/44248582/a0088407-cbbc-4115-b61a-0ea14475dcc9)


## Security Considerations and Reliability


## 🚀 How to Use

Explain how others can use your project, including setup instructions, dependencies, and examples.




https://nbschwa.wixsite.com/santi-scan

## 👥 Contributors

- Noah Schwartz
- 
