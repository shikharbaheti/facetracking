import cv2

cap = cv2.VideoCapture('video.avi')
fps = cap.get(cv2.CAP_PROP_FPS)

timestamps = [cap.get(cv2.CAP_PROP_POS_MSEC)]
choose = [True, False]
calc_timestamps = [0.0]
res = []

while(cap.isOpened()):
    frame_exists, curr_frame = cap.read()
    if frame_exists:
        dictD = {}
        dictD[cap.get(cv2.CAP_PROP_POS_MSEC)] = True
        timestamps.append(cap.get(cv2.CAP_PROP_POS_MSEC))
        calc_timestamps.append(calc_timestamps[-1] + 1000/fps)
        res.append(dictD)
    else:
        break

cap.release()

for i, (ts, cts) in enumerate(zip(timestamps, calc_timestamps)):
    print('Frame %d difference:' % i, abs(ts - cts))

print(res)
