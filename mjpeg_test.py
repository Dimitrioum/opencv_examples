import cv2
import subprocess as sp
import pandas as pd

cap = cv2.VideoCapture(0)

_WIDTH = 640
_HEIGHT = 480
_FPS = 30
_FFMPEG_BIN = 'ffmpeg'
file_path = '/home/malov/test_frame.jpg'

# while True:
ret, frame = cap.read()
if ret:
    cv2.imwrite('/home/malov/test_frame.jpg', frame)

    fourcc1 = cv2.VideoWriter_fourcc(*'MJPG')
    fourcc2 = cv2.VideoWriter_fourcc(*'H264')

    stream1 = cv2.VideoWriter('/home/malov/mjpeg_test_frame.jpg', fourcc1, _FPS, (_WIDTH, _HEIGHT))
    stream2 = cv2.VideoWriter('/home/malov/h264_test_frame.avi', fourcc2, _FPS, (_WIDTH, _HEIGHT))

    stream1.write(frame)
    stream2.write(frame)

    command = [_FFMPEG_BIN, '-i', file_path, '-']
    pipe = sp.Popen(command, stdout=sp.PIPE, stderr=sp.PIPE)
    pipe.terminate()
    infos = pipe.stderr.read().decode()

    # duration = int(infos[infos.find('Duration') + 19 : infos.find('Duration') + 21])
    # bitrate = int(infos[infos.find('bitrate') + 8 : infos.find('kb/s')])

print(infos, 'test')
cap.release()

