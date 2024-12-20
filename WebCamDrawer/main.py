import cv2
import numpy as np
import math
import mediapipe as mp


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)
mp_draw = mp.solutions.drawing_utils
# Initialize the video capture object
videoCapturing  = cv2.VideoCapture(0)  # 0 for the default camera


rectangles = []
colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0),None]
x = 10  # Starting x-coordinate
y = 10  # Starting y-coordinate
width = 100  # Width of each rectangle
height = 50  # Height of each rectangle

def point_in_rectangle(point, rect):
    x, y = point
    rx, ry, rw, rh = rect
    return rx <= x <= rx + rw and ry <= y <= ry + rh

currentColor = None
# Check if the camera opened successfully
# Outside the main loop
last_point = None
canvas = None
while True:
    # Read a frame from the video capture
    ret, frame = videoCapturing.read()
    
    frame = cv2.flip(frame, 1)
    if canvas is None:
     canvas = np.zeros_like(frame)
    rectangles = []
    for i in range(len(colors)):
     cv2.rectangle(frame, (x, y), (x + width, y + height), colors[i], -1)
     if i == 3:
        cv2.putText(frame, "Clear",(x + 10, y + 30), cv2.FONT_HERSHEY_TRIPLEX,1,(255,255,255),2)
     rectangles.append((x, y, width, height))
     x += width + 10  # Adjust x-coordinate for the next rectangle


    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame and find hands
    results = hands.process(rgb_frame)


    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get index finger tip coordinates
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            h, w, _ = frame.shape
            cxi, cyi = int(index_finger_tip.x * w), int(index_finger_tip.y * h)
            # Get the thumb and pinky tip coordinates 
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            ctx, cty = int(thumb_tip.x * w), int(thumb_tip.y * h)
            pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
            cpx, cpy = int(pinky_tip.x * w), int(pinky_tip.y * h)


            # Draw a circle at the index finger tip
            cv2.circle(frame, (cxi, cyi), 10, (0, 255, 0), -1)
            cv2.circle(frame, (ctx, cty), 10, (0, 255, 0), -1)
            cv2.circle(frame, (cpx, cpy), 10, (0, 255, 0), -1)
            distance2 = math.sqrt((ctx - cpx)**2 + (cty - cpy)**2)
            distance2 = round(distance2, 2)

 # Check if index finger tip is in any rectangle
            insideRectangle = False
            for i, rect in enumerate(rectangles):
              rectangle_color = ["Red","Green","Blue","clear"]
              if point_in_rectangle((cxi, cyi), rect):
                 #cv2.putText(frame, f"In {rectangle_color[i]}", (400, 430), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                 insideRectangle = True
                 #if distance1 < 40:
                 if i == 3:
                    cv2.putText(frame,f"Connect your Pinky and thumb to clear the canvas", (10,440), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255,255,255),1)
                 else:
                    cv2.putText(frame,f"Connect your Pinky and thumb to select the color {rectangle_color[i]} ", (10, 440), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                 if distance2 < 40:
                        if i == 3:
                           canvas = np.zeros_like(frame)
                        currentColor = colors[i]
                        cv2.putText(frame,f"you have selected the color {rectangle_color[i]} and it will be your paint color",(10,400),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                        break

            if not any(point_in_rectangle((cxi, cyi), rect) for rect in rectangles):
                cv2.putText(frame,"your hand is outside",(20,410),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

            if distance2 < 40 and not any(point_in_rectangle((cxi, cyi), rect) for rect in rectangles):
                if last_point is not None:
                    cv2.line(canvas, last_point, (cxi, cyi), currentColor, thickness=5)
                    #cv2.circle(frame,(cxi,cyi),10,currentColor,-1)
                last_point = (cxi, cyi)
            else:
                last_point = None
            
                


    # Check if frame was read successfully
    if not ret:
        print("Error reading frame")
        break
    # Reset x coordinate for each frame
    x = 10  # Starting x-coordinate
    y = 10  # Starting y-coordinate
    # Display the frame and also collect the shape of the frame

    frame = cv2.addWeighted(frame, 0.5, canvas, 1.5, 0) 
    cv2.imshow("Camera Feed", frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
videoCapturing.release()
cv2.destroyAllWindows()
