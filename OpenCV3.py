import cv2

cap = cv2.VideoCapture(0)



_FRAME_WIDTH = 640
_FRAME_HEIGHT = 480
_FRAME_FPS = 30

out1 = cv2.VideoWriter('/home/malov/test-image_h264.avi', cv2.VideoWriter_fourcc(*'H264'), _FRAME_FPS, (_FRAME_WIDTH,_FRAME_HEIGHT))
out2 = cv2.VideoWriter('/home/malov/test-image_mjpeg.avi', cv2.VideoWriter_fourcc(*'MJPG'), _FRAME_FPS, (_FRAME_WIDTH,_FRAME_HEIGHT))
out3 = cv2.VideoWriter('/home/malov/test-image.avi', cv2.VideoWriter_fourcc(*'VP80'), _FRAME_FPS, (_FRAME_WIDTH,_FRAME_HEIGHT))

def _video_writer(frame):
    return out1.write(frame), out2.write(frame), out3.write(frame)


if __name__ == '__main__':
    ret, frame = cap.read()

#     while cap.isOpened():
#
#         if ret:
    _video_writer(frame)
            # cv2.imshow('OpenCV_Training', frame)
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break


cap.release()
out1.release()
out2.release()
out3.release()
cv2.destroyAllWindows()
