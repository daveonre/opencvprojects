
# It helps in identifying the faces 
import cv2, sys, numpy, os 
size = 4
haar_file = 'haarcascade_frontalface_default.xml'
datasets = 'FacesData'

webcam = cv2.VideoCapture(0)

print('Recognizing Face Please Be in sufficient Lights...') 
  
# Create a list of images and a list of corresponding names 
(images, labels, names, id) = ([], [], {}, 0) 
for (subdirs, dirs, files) in os.walk(datasets): 
    for subdir in dirs: 
        names[id] = subdir 
        subjectpath = os.path.join(datasets, subdir) 
        for filename in os.listdir(subjectpath): 
            path = subjectpath + '/' + filename 
            label = id
            images.append(cv2.imread(path, 0)) 
            labels.append(int(label)) 
        id += 1

(width, height) = (130, 100)



Cascadingface = cv2.CascadeClassifier(haar_file) 
# Create a Numpy array from the two lists above 
(images, labels) = [numpy.array(lis) for lis in [images, labels]]

# print(images)
# print(labels)

# OpenCV trains a model from the images
# NOTE FOR OpenCV2: remove '.face' 
model = cv2.face.LBPHFaceRecognizer_create() 
model.train(images, labels) 
model.save("my_face_model.yml")
model = cv2.face.LBPHFaceRecognizer_create()
model.read("my_face_model.yml")

# print(model)

while True: 
    (_, facefromcam) = webcam.read() 
    gray = cv2.cvtColor(facefromcam, cv2.COLOR_BGR2GRAY) 
    faces = Cascadingface.detectMultiScale(gray, 1.3, 5) 
    #cv2.rectangle(facefromcam,(50,50),(100,100),(255, 0, 0),2)
    #cv2.imshow("facefromcam",facefromcam)
    #cv2.rectangle(facefromcam,(50,50),(100,100),(255, 0, 0),2)
    #cv2.waitKey(10)

    for (x, y, w, h) in faces: 
        cv2.rectangle(facefromcam, (x, y), (x + w, y + h), (255, 0, 0), 10) 
        #cv2.rectangle(facefromcam,(50,50),(100,100),(243, 17, 17),10)
        face = gray[y:y + h, x:x + w] 
        print(face)
        face_resize = cv2.resize(face, (width, height)) 
        # Try to recognize the face 
        prediction = model.predict(face_resize) 
        #print(prediction)
        cv2.rectangle(facefromcam, (x, y), (x + w, y + h), (0, 255, 0), 3) 
        
        if prediction[1]<500: 
           cv2.putText(facefromcam, '% s - %.0f' % 
(names[prediction[0]], prediction[1]), (x-10, y-10),  
cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
    cv2.imshow("facefromcam",facefromcam)
    key = cv2.waitKey(10)
    if key == 27:
        break;
        
    



