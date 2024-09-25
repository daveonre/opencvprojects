Dominant Color Detector

This Python script utilizes OpenCV (cv2) and NumPy (np) to analyze a live video stream from your webcam and identify the dominant color (blue, green, or red) in each frame.

Requirements:

OpenCV (cv2): Install using pip install opencv-python
NumPy (np): Typically included with most scientific Python installations
How it Works:

Imports: The code starts by importing the necessary libraries:
cv2: For capturing video and displaying frames.
np: For numerical computations (calculating means).
Video Capture: It initializes a VideoCapture object from your webcam using index 0 (replace it with a specific video file path if needed).
Infinite Loop: A while loop is used to process each frame continuously:
Capture a frame using capture.read().
Extract the blue, green, and red channels using array slicing (frame[:, :, 0], frame[:, :, 1], and frame[:, :, 2]).
Calculate the mean values for each channel using np.mean(b), np.mean(g), and np.mean(r).
Determine the dominant color based on the highest mean value:
If b_mean is greater than both g_mean and r_mean, the dominant color is "Blue".
If g_mean is greater than both r_mean and b_mean, the dominant color is "Green".
Otherwise, the dominant color is "Red".
Print the dominant color to the console.
Display the frame using cv2.imshow('Vid', frame).
Wait for a key press with a delay of 1 millisecond using cv2.waitKey(1).
Check if the pressed key is 'q' (quit). If yes, break the loop.
Resource Release: After the loop exits, the script releases the video capture object and destroys all OpenCV windows using capture.release() and cv2.destroyAllWindows().
Usage:

Save the code as a Python file (e.g., dominant_color_detector.py).
Run the script from your terminal using python dominant_color_detector.py.
The live video feed from your webcam will start displaying, and the dominant color will be printed to the console for each frame.
Press 'q' on your keyboard to stop the program and close the video window.
