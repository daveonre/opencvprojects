import cv2
import numpy as np

captureVideo = cv2.VideoCapture(0)
hand_cascade = cv2.CascadeClassifier('hand.xml')

counterOfHands = 0

while True:
    ret, eachframe = captureVideo.read()
    gray = cv2.cvtColor(eachframe, cv2.COLOR_BGR2GRAY)
    #gray = cv2.GaussianBlur(gray, (5, 5), 0)  # Apply Gaussian blur
    hands = hand_cascade.detectMultiScale(gray, 1.5, 2)  # Adjusted parameters
    contour = hands
    contour = np.array(contour)

    if counterOfHands == 0:
        if len(contour) == 2:
            cv2.putText(img=eachframe, text='Your engine started',
                        org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX,
                        fontScale=1, color=(0, 255, 0))

            for (x, y, w, h) in hands:
                cv2.rectangle(eachframe, (x, y), (x + w, y + h), (0, 255, 0), 2)
            counterOfHands += 1

    if counterOfHands > 0:
        if len(contour) >= 2:
            cv2.putText(img=eachframe, text='You can take your car on long drive',
                        org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX,
                        fontScale=1, color=(255, 0, 0))

            for (x, y, w, h) in hands:
                cv2.rectangle(eachframe, (x, y), (x + w, y + h), (0, 255, 0), 2)

        elif len(contour) == 1:
            cv2.putText(img=eachframe, text='You can speed up to 80km/h',
                        org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX,
                        fontScale=1, color=(0, 255, 0))

            for (x, y, w, h) in hands:
                cv2.rectangle(eachframe, (x, y), (x + w, y + h), (0, 255, 0), 2)

        elif len(contour) == 0:
            cv2.putText(img=eachframe, text='Brake is applied slowly',
                        org=(int(100 / 2 - 20), int(100 / 2)),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX,
                        fontScale=1, color=(0, 0, 255))

        counterOfHands += 1

    cv2.imshow('Driver_eachframe', eachframe)
    k = cv2.waitKey(20) & 0xff
    if k == 27:
        break
