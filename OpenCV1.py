import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('/home/malovdmitrij/PycharmProjects/OpenCV_examples/bird.jpg')

img = img[1,1:160]
cv2.imshow('bird',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

