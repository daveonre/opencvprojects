**Real-Time Edge Detection with OpenCV**
This Python script implements real-time edge detection on a video stream captured from your webcam.

**Features:**

Uses OpenCV library for image processing.
Applies Canny edge detection to identify object outlines.
Overlays the detected edges on the original frame for visualization.

**Functions:**

canny_edge_detection(frame):
Converts the frame to grayscale.
Applies Gaussian blur for noise reduction.
Performs Canny edge detection with pre-defined thresholds.
Returns both the blurred image and the edge map.
main():
Captures video from the default webcam.
Reads frames in a loop.
Calls the canny_edge_detection function to process each frame.
Overlays edges on the blurred frame for visualization.
Displays three windows: Blurred frame, Detected edges, Overlay image.
Allows exiting the program with the 'q' key.
Releases the webcam and closes all OpenCV windows on exit.


**Instructions:**

Save the code as a Python file (e.g., edge_detection.py).
Run the script from your terminal using python edge_detection.py.
The program will display three windows: Blurred frame, Detected edges, Overlay image.
Press 'q' on the keyboard to stop the program and close the windows.

**Customization:**

You can adjust the Canny edge detection thresholds (70 and 135) in the canny_edge_detection function to fine-tune edge detection sensitivity.
Dependencies:

This script requires the OpenCV library. You can install it using pip install opencv-python.
