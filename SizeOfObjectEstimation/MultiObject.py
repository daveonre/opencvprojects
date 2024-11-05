import cv2 
import numpy as np 


# Load the image 
capturedImg = cv2.imread('C:\\Users\\C291519\\Documents\\computervision_projects\\SizeOfObject\\polygons.jpeg') 

# Convert the image to grayscale 
grayed = cv2.cvtColor(capturedImg, cv2.COLOR_BGR2GRAY) 


# Apply a threshold to the image to 
# separate the objects from the background 
ret, thresh = cv2.threshold( 
    grayed, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Find the contours of the objects in the image 
contours, hierarchy = cv2.findContours( 
    thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 

for eachcnt in contours: 
    area = cv2.contourArea(eachcnt) 
    # Draw a bounding box around each 
    # object and display the area on the image 
    x, y, w, h = cv2.boundingRect(eachcnt) 
    cv2.rectangle(capturedImg, (x, y), (x+w, y+h), (0, 255, 0), 2) 
    cv2.putText(capturedImg, str(area), (x, y), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2) 
    
# Show the final image with the bounding boxes 
# and areas of the objects overlaid on top 
cv2.imshow('image', capturedImg) 
cv2.waitKey(0) 
cv2.destroyAllWindows()
