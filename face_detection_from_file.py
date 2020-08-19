import cv2
from plotly import graph_objects as go

dictD = {}


def processImage():
    cap = cv2.VideoCapture('video.avi')
    fps = cap.get(cv2.CAP_PROP_FPS)

    if not (cap.isOpened()):
        print("Error reading the video stream or file!")

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    font = cv2.FONT_HERSHEY_SIMPLEX
    faceFound = "NOT FOUND"
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(
        'M', 'J', 'P', 'G'), fps, (frame_width, frame_height))

    while(cap.isOpened()):

        frameExists, currentFrame = cap.read()

        if frameExists:
            gray = cv2.cvtColor(currentFrame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(currentFrame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = currentFrame[y:y+h, x:x+w]
            if (len(faces) >= 1):
                dictD[cap.get(cv2.CAP_PROP_POS_MSEC)] = True
                faceFound = "Face detected!"
            else:
                dictD[cap.get(cv2.CAP_PROP_POS_MSEC)] = False
                faceFound = "NOT FOUND"

            cv2.putText(currentFrame, faceFound,
                        (40, 40), font, 1, (255, 0, 0), 2)

            cv2.imshow('img', currentFrame)
            out.write(currentFrame)

            if cv2.waitKey(30) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()


t = 0
f = 0
for key, value in dictD.items():
    if (value == True):
        t += 1
    else:
        f += 1


processImage()


def pieGraph():
    labels = ['In picture', 'Not in picture']
    values = [t, f]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.show()


pieGraph()
