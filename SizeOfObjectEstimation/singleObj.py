import cv2 

# Load the image 
cameraImg = cv2.imread('C:\\Users\\C291519\\Documents\\computervision_projects\\SizeOfObject\\geekforgeek.jpeg') 
# cv2.imshow("photo",cameraImg)
# 

# Convert to grayscale 
grayedImg = cv2.cvtColor(cameraImg, cv2.COLOR_BGR2GRAY) 

# #to separate the object from the background 
ret, thresh = cv2.threshold(grayedImg, 127, 255, 0) 

# # # Find the contours of the object 
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 

# # # Draw the contours on the original image 
cv2.drawContours(cameraImg, contours, -1, (0,0,255), 6) 

# cv2.imshow("contours",cameraImg)
# cv2.waitKey(0)

# # # Get the area of the object in pixels 
areaInPixel = cv2.contourArea(contours[0]) 

# # Convert the area from pixels to a real-world unit of measurement (e.g. cm^2) 
scale_factor = 0.1 # 1 pixel = 0.1 cm 
size = areaInPixel * scale_factor ** 2

# # Print the size of the object 
print('Size:', size) 

# # Display the image with the contours drawn 
cv2.imwrite('Object.jpeg', cameraImg) 
cv2.waitKey(0) 

# # Save the image with the contours drawn to a file 
cv2.imwrite('object_with_contours.jpg', cameraImg)
