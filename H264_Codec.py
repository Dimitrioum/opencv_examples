# -*- coding: utf-8 -*-
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
_FRAME_WIDTH = 640
_FRAME_HEIGHT = 480
_FRAME_FPS = 30
out = cv2.VideoWriter('Video_from_Camera.avi', cv2.VideoWriter_fourcc(*'X264'), _FRAME_FPS, (_FRAME_WIDTH,_FRAME_HEIGHT))

def _video_writer(frame):
    cv2.imshow('OpenCV_Training', frame)
    return out.write(frame)

def macroblock(i,j):

    for x in range(_FRAME_WIDTH):
        for y in range(_FRAME_HEIGHT):
            f.write(str(Y[x][y]))

    for x in range(_FRAME_WIDTH):
        for y in range(_FRAME_HEIGHT):
            f.write(str(U[x][y]))

    for x in range(_FRAME_WIDTH):
        for y in range(_FRAME_HEIGHT):
            f.write(str(V[x][y]))

f = open('frame_data.txt', 'w')

ret, frame = cap.read()
# считывание компонент R G B в кадре
B = [[frame[i][j][0] for i in range(_FRAME_HEIGHT)] for j in range(_FRAME_WIDTH)]
G = [[frame[i][j][1] for i in range(_FRAME_HEIGHT)] for j in range(_FRAME_WIDTH)]
R = [[frame[i][j][2] for i in range(_FRAME_HEIGHT)] for j in range(_FRAME_WIDTH)]

#RGB to YUV
Y = [[int(frame[i][j][2]*0.299 + frame[i][j][1]*0.587 + frame[i][j][0]*0.114) for i in range(_FRAME_HEIGHT)] for j in range(_FRAME_WIDTH)]
U = [[int(-frame[i][j][2]*0.14713 - frame[i][j][1]*0.28886 + frame[i][j][0]*0.436 + 128) for j in range(_FRAME_HEIGHT)] for j in range(_FRAME_WIDTH)]
V = [[int(frame[i][j][2]*0.615 - frame[i][j][1]*0.51499 - frame[i][j][0]*0.10001 + 128) for j in range(_FRAME_HEIGHT)] for j in range(_FRAME_WIDTH)]

if __name__ == "__main__":

    if ret == True:
        while not f.closed:

            for i in range(_FRAME_WIDTH):
                for j in range(_FRAME_HEIGHT):
                    macroblock(i,j)
            f.close()

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

cap.release()
out.release()
cv2.destroyAllWindows()


