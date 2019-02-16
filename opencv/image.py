import cv2
import numpy as np
import os

absolute_path = os.path.join(os.getcwd(), 'opencv', 'image.jpg');
#print(absolute_path)
img = cv2.imread(absolute_path)
cv2.imshow('test',img)
cv2.waitKey(0)