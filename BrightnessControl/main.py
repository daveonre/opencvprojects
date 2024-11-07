import cv2 
import mediapipe as mp 
from math import hypot 
import screen_brightness_control as sbc 
import numpy as np 

mpHands = mp.solutions.hands 
handDetection = mpHands.Hands( 
    static_image_mode=False, 
    model_complexity=1, 
    min_detection_confidence=0.75, 
    min_tracking_confidence=0.75, 
    max_num_hands=2) 
  
DrawingOnHand = mp.solutions.drawing_utils

# Start capturing video from webcam 
capturingCamera = cv2.VideoCapture(0) 

while True: 
    # Read video frame by frame 
    _,frame = capturingCamera.read() 
      
    #Flip image  
    frame=cv2.flip(frame,1) 
      
    # Convert BGR image to RGB image 
    frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) 
      
    # Process the RGB image 
    Process = handDetection.process(frameRGB) 

    landMarksListCollected  = [] 
    # if hands are present in image(frame) 
    if Process.multi_hand_landmarks: 
        # detect handmarks 
        for oneHandWithLandMark in Process.multi_hand_landmarks: 
            for _id,landmarks in enumerate(oneHandWithLandMark.landmark): 
                # store height and width of image 
                height,width,color_channels = frame.shape 
                  
                # calculate and append x, y coordinates 
                # of handmarks from image(frame) to lmList 
                x,y = int(landmarks.x*width),int(landmarks.y*height)               
                landMarksListCollected.append([_id,x,y])  
              
            # draw Landmarks 
            DrawingOnHand.draw_landmarks(frame,oneHandWithLandMark,mpHands.HAND_CONNECTIONS) 
    if landMarksListCollected != []: 
        # store x,y coordinates of (tip of) thumb 
        thumbX, thumbY = landMarksListCollected[4][1], landMarksListCollected[4][2] 
  
        # store x,y coordinates of (tip of) index finger 
        indexX, indexY = landMarksListCollected[8][1], landMarksListCollected[8][2] 
  
        # draw circle on thumb and index finger tip 
        cv2.circle(frame, (thumbX, thumbY), 7, (0, 255, 0), cv2.FILLED) 
        cv2.circle(frame, (indexX, indexY), 7, (0, 255, 0), cv2.FILLED) 
  
        # draw line from tip of thumb to tip of index finger 
        cv2.line(frame, (thumbX, thumbY), (indexX, indexY), (0, 255, 0), 3) 
  
        # calculate square root of the sum of 
        # squares of the specified arguments. 
        LengthbetweenThumbAndIndex = hypot(indexX-thumbX, indexY-thumbY) 
  
        # 1-D linear interpolant to a function 
        # with given discrete data points 
        # (Hand range 15 - 220, Brightness 
        # range 0 - 100), evaluated at length. 
        brightnessLevel = np.interp(LengthbetweenThumbAndIndex, [15, 220], [0, 100]) 
  
        # set brightness 
        sbc.set_brightness(int(brightnessLevel)) 
  
    # Display Video and when 'q' is entered, destroy  
    # the window 
    cv2.imshow('Image', frame) 
    if cv2.waitKey(1) & 0xff == ord('q'): 
        break
