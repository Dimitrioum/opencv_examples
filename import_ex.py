import OpenCV3
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
        ret, frame = cap.read()

        if ret == True:
            OpenCV3._video_writer(frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

cap.release()
out.release()
v2.destroyAllWindows()
