import cv2
import sys
import numpy
import os 
haar_file = 'haarcascade_frontalface_default.xml'

datasets = 'FacesData'

sub_data = 'dave'

path = os.path.join(datasets, sub_data) 
if not os.path.isdir(path): 
    os.mkdir(path)

#print(path)

(width, height) = (130, 100)


Cascadingface = cv2.CascadeClassifier(haar_file) 
frontCam = cv2.VideoCapture(0)

count = 1
while True:  
    (_, eachface) = frontCam.read() 
    gray = cv2.cvtColor(eachface, cv2.COLOR_BGR2GRAY) 
    faces = Cascadingface.detectMultiScale(gray, 1.3, 4) 
    items = os.listdir(path)
    for (x, y, w, h) in faces: 
        cv2.rectangle(eachface, (x, y), (x + w, y + h), (255, 0, 0), 2) 
        face = gray[y:y + h, x:x + w] 
        face_resize = cv2.resize(face, (width, height)) 
        cv2.imwrite('% s/% s.png' % (path, len(items)+1), face_resize) 
    
    #items = os.listdir(path)
    cv2.imshow('OpenCV', eachface) 
    key = cv2.waitKey(10) 

    if len(items) >29:
        break
    if key == 27: 
        break
