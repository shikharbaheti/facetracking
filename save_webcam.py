import cv2

capture = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
videoWriter = cv2.VideoWriter('./test.avi', fourcc, 30.0, (640, 480))

while (True):

    ret, frame = capture.read()

    if ret:
        cv2.imshow('video', frame)
        videoWriter.write(frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

capture.release()
videoWriter.release()

cv2.destroyAllWindows()
