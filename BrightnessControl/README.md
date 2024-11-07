## Drowsiness Detection with Hand Gesture Brightness Control

This Python script leverages OpenCV and MediaPipe to create a real-time drowsiness detection system with hand gesture control for brightness adjustment.

**Features:**

* Detects the user's face and hands using MediaPipe.
* Calculates Eye Aspect Ratio (EAR) to assess drowsiness (**not implemented in this code example**).
* Tracks the distance between the thumb and index finger to control brightness.
* Adjusts the brightness of a connected device based on the hand gesture.

**Requirements:**

* OpenCV
* MediaPipe
* NumPy
* screen_brightness_control (external library)

**Installation:**

```bash
pip install opencv-python mediapipe numpy screen_brightness_control
```

**Usage:**

1. **Set up your environment:** Ensure you have a camera and a device with brightness control functionality (supported by the `screen_brightness_control` library).
2. **Run the script:** Execute the Python script.
3. **Interact with the system:** Open your eyes to maintain normal brightness. Pinch your thumb and index finger to decrease brightness, and spread them to increase brightness.
4. **Exit:** Press 'q' on your keyboard to stop the program.

**Note:**

* The effectiveness of the brightness control based on hand gestures may vary depending on factors like lighting conditions and camera placement.
