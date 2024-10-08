Project Name simple Face detection and recognition 

Introduction

This project implements two functionalities related to facial recognition:

**Facial Data Collection**: This script allows you to collect facial data for a specific person. It captures images from your webcam and saves them in a designated folder.
**Facial Recognition:** This script utilizes a trained facial recognition model to identify faces in real-time using your webcam.

**Requirements**

Python 3.x
OpenCV (pip install opencv-python)
NumPy (pip install numpy)

**Data Collection:**

The script will activate your webcam.
Faces detected in the webcam feed will be highlighted with a red rectangle.
Up to 30 images will be captured and saved in the FacesData/dave directory (replace dave with your desired subfolder name). You can adjust this limit by modifying the condition if len(items) > 29.
Press Esc key to stop capturing data.
**Explanation:**

The script imports libraries for computer vision, system operations, numerical computations, and file system interaction.
It uses a pre-trained Haar cascade classifier to detect frontal faces in the webcam stream.
Detected faces are saved as resized PNG images in a designated folder.
The script displays the webcam video with detected faces marked by red rectangles.
**Customization:**

You can modify the script to:
Change the target subfolder name (dave) for storing images.
Adjust the maximum number of images captured by modifying the if len(items) > 29 condition.

README: Facial Recognition Script
This Python script utilizes OpenCV to perform real-time facial recognition using a pre-trained model.


**Loads Training Data:**
Scans the FacesData directory for subdirectories representing different individuals.
Loads images from each subdirectory and associates them with the corresponding person's name.
Creates a NumPy array of images and labels for training the model.
Facial Recognition:
Accesses your webcam and captures video frames.
Detects faces in each frame using a pre-trained Haar cascade classifier.
Attempts to recognize the detected face using the loaded model.
If a face is recognized, its name and a confidence score are displayed on the video frame.
A green rectangle surrounds recognized faces, while undetected faces are enclosed in a red rectangle.
Usage:

Ensure you have a trained facial recognition model named my_face_model.yml in the same directory as the script. You'll need to create this model using training data (images of different individuals) beforehand. Tools like OpenCV offer model training functionalities.

**Face Recognition:**

The script will access your webcam and try to recognize faces in real-time.
Recognized faces and their names will be displayed on the screen.
Press Esc key to stop the recognition process.
Customization:

The script can be further optimized for better recognition accuracy.
Explore advanced facial recognition techniques and libraries for additional functionalities.



