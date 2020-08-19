import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
faceFound = "NOT FOUND"
res = []

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    fps = cap.get(cv2.CAP_PROP_FPS)
    dictD = {}
    if (len(faces) >= 1):
        dictD[cap.get(cv2.CAP_PROP_POS_MSEC)] = True
        faceFound = "Face detected!"
    else:
        dictD[cap.get(cv2.CAP_PROP_POS_MSEC)] = False
        faceFound = "NOT FOUND"

    res.append(dictD)

    cv2.putText(img, faceFound,
                (40, 40), font, 1, (255, 0, 0), 2)

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
print("Frames per second was: {0}".format(fps))
