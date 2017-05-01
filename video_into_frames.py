import cv2

cap = cv2.VideoCapture('/home/malovdmitrij/PycharmProjects/OpenCV_examples/output.avi')
ret,frame = cap.read()
count = 1
success = True
while success:
  ret,frame = cap.read()
  print 'Read a new frame: ', ret
  cv2.imwrite("frame%d.jpg" % count, frame)     # save frame as JPEG file
  count += 1
