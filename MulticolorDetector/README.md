**Readme: Real-Time Multiple Color Detection with OpenCV**
**Purpose**

This Python script demonstrates real-time detection and tracking of red, green, and blue colors in a video stream using OpenCV.

**Features**

Detects red, green, and blue colors in video frames.
Draws bounding boxes around detected color objects.
Labels the bounding boxes with the color name.
Filters out small objects using a threshold for contour area.
**Requirements**

Python 3.x
OpenCV library
Webcam or video file
Installation

Install Python 3.x if not already installed.

Install OpenCV using pip:

Bash
pip install opencv-python
Use code with caution.

**Usage**

Run the script.
The script will capture video from your webcam (default).
If you want to use a video file, replace cv2.VideoCapture(0) with cv2.VideoCapture("path/to/your/video.mp4") in the code.
Colored objects (red, green, blue) will be detected and displayed with bounding boxes and labels.
Press 'q' to exit the program.
**Customization**

Adjust the color ranges defined by red_lower, red_upper, etc. to detect different color variations.
Modify the threshold for cv2.contourArea to filter out smaller objects.
Experiment with different morphological operations for refining color masks (currently using dilation).
**Enjoy using this script for your multi-color detection projects!**
