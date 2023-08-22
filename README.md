# SantiScan

## 🧼 Introduction

SantiScan solves the problem of poor employee hygiene in hospitals. It's a soap dispenser that uses computer vision to accurately record how many times each faculty member washes their hands. When a network of SantiScans is connected in a building, hospitals can:

- Automatically detect sanitation concerns on a person-by-person basis
- Autonomously remind specific employees of the need for sanitation
- Track the spread of disease from room to room (based on when and where someone washes their hands)

## 💡 Hardware

- ESP32 circuit board: $8
- HD camera module: $4
- ESP32 boot loader: $4

Total cost: Only $16 more than a normal dispenser

## 📖 Pretraining

When the devices are installed, every hospital employee will need to be "scanned" into the system. They will move their hand back and forth underneath one of our cameras for 30 seconds, generating 900 frames of palm print data.

## 🛠 Process

![Screenshot 2023-08-18 at 4 43 41 PM](https://github.com/NoahBSchwartz/SantiScan/assets/44248582/4ba95f6c-d22e-4841-960e-10981f5f12d1)

1. #### On-Device Actions
   - The ESP32-CAM captures and saves a video to its SD card each time the sanitizer is dispensed
   - When the user walks away, each of these 15 frames is uploaded to a Google Colab notebook

2. #### Data Cleaning
   - A machine learning algorithm, [Mediapipe](https://google.github.io/mediapipe/solutions/face_mesh.html), locates each joint of the hand
   - These 20 points are used to perfectly mask the hand from its background using the [Segment Anything](https://github.com/facebookresearch/segment-anything.git) approach

3. #### Hand Recognition
   - Now that each frame only contains data about the palm, the video can be cross-referenced with our palm database using Keras (with 97% accuracy)
   - This data can finally be permanently saved in a spreadsheet and then displayed on our [website](https://nbschwa.wixsite.com/santi-scan)

## 🎉 Result

The final product is compact enough to look and function exactly like a normal automatic soap dispenser. The only changes are a small maintenance port and 3 switches on the backside of the device.

![unnamed__4_-removebg-preview](https://github.com/NoahBSchwartz/SantiScan/assets/44248582/3eeae46e-b1d2-4cdd-91ca-6b222211ae1a)
![unnamed__5_-removebg-preview](https://github.com/NoahBSchwartz/SantiScan/assets/44248582/a0088407-cbbc-4115-b61a-0ea14475dcc9)

## 🔐 Security Considerations and Reliability

- We save all data to google drive, and our server has the only key to access it
- We delete all scanned camera data within 2 minutes after it’s collected (no human will ever see it)
- The camera module is linked to the dispenser’s electronics so it can’t miss scans
- All code runs in the cloud (even if the server fails, no data will be lost)
- Every library used in the software is enterprise quality
- No additional infrastructure, only a wifi network is needed

## 👥 Contributors

This product was a collaboration between the Computer Science and Biomedical programs at County High. The biomedical engineers came up with the project idea, validated, researched, and grounded their claims in scientific studies. I was responsible for the full software and hardware development.

- Noah Schwartz (Product Engineer)
- Brandt Roman (Product Designer)
- Taylor Gonzales (Product Designer)
- Olivia Cordova (Product Designer)
- Eric David (Documentation Writer)
