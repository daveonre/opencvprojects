**Hand Paint - A Real-Time Drawing App using OpenCV and MediaPipe**

This code creates a real-time drawing application using hand gestures and fingertip detection with OpenCV and MediaPipe.*

**Features**:

Color Selection: Choose a drawing color from four pre-defined color rectangles displayed on the screen.
Drawing: Draw on a virtual canvas using your index finger.
Clearing: Connect your thumb and pinky finger to clear the entire canvas.

**How it Works**:

Color Rectangles: Four colored rectangles are displayed on the screen, representing the available drawing colors.
Hand Detection: MediaPipe is used to detect your hand landmarks in real-time.
Fingertip Detection: The index fingertip location is tracked.
Color Selection: When the index fingertip touches a color rectangle, that color becomes the current drawing color.
Drawing: As the index finger moves across the screen, a line is drawn on a virtual canvas using the current drawing color.
Clearing: Connecting your thumb and pinky finger clears the entire canvas.
Instructions:

**Run the script**.

Point your index finger at one of the colored rectangles to select your drawing color.
Move your index finger around the screen to draw.
Connect your thumb and pinky finger to clear the canvas.
Press 'q' to quit the application.




