**Project: Interactive Image Segmentation**

This code demonstrates interactive image segmentation using the Watershed algorithm. It allows you to:

- **Mark regions** on an image (e.g., 'road.jpg') by clicking with the left mouse button.
- **Assign colors** (0-9) to each marked region using keyboard input.
- **Segment the image** based on your markings, applying the chosen colors to distinct segments.
- **Reset the segmentation** by pressing 'c'.

**Instructions:**

1. **Place the code** in the same directory as your image (`road.jpg`).
2. **Run the code.**
3. **Click** on the image to define regions.
4. **Press a number key (0-9)** to assign a color to the clicked region.
5. **Observe** the segmentation update on the image.

**Functionality:**

- The code first imports necessary libraries (`cv2`, `numpy`, `matplotlib`).
- It reads the image (`road.jpg`) and creates copies for segmentation.
- A callback function (`mouse_callback`) handles mouse clicks, marking regions with chosen colors.
- Users can switch colors by pressing number keys.
- The `watershed` function segments the image based on the markings.
- Colored segments are displayed based on assigned colors.
- Pressing 'c' clears the markings and resets the segmentation.

**Note:**

- Ensure the image (`road.jpg`) is in the same directory as the code.

**Disclaimer:**

This code is for educational purposes and may require modifications for specific use cases.
