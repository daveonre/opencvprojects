
**Project Title: Real-Time Hand Detection and Tracking with Handedness Display**

**Description**:

This Python script uses MediaPipe Hands to detect and track hands in real-time video captured from your webcam. It displays "Both Hands" if two hands are detected and displays "Left Hand" or "Right Hand" based on the handedness of the detected hand.

**Usage**:

**Install dependencies:**

Bash
pip install mediapipe opencv-python
Use code with caution.

**Run the script:**

**Bash**
python hand_detection_handedness.py
Use code with caution.

The script will start capturing video from your webcam. Press the 'q' key to quit.

**How it works:**

The script imports necessary libraries for image processing (OpenCV), hand detection (MediaPipe), and converting Protobuf messages (used by MediaPipe) to Python dictionaries.
It then initializes the MediaPipe Hands model with specific parameters for real-time processing, minimum detection/tracking confidence, and maximum number of hands to track.
The script continuously captures video frames from the webcam, flips them horizontally for better display, and converts them to RGB format (required by MediaPipe).
MediaPipe Hands is used to process the frames, and the results are stored in a variable named results.
If hands are detected, the script checks if there are two hands present. If so, it displays "Both Hands".
Otherwise, it iterates through each detected hand and uses the MessageToDict function to extract the handedness label ("Left" or "Right").
Based on the label, the script displays "Left Hand" or "Right Hand" on the corresponding side of the video window.
The processed video frame is then displayed, and the program exits when the 'q' key is pressed.
**Dependencies**:

MediaPipe (latest stable version recommended)
OpenCV (latest stable version recommended)
