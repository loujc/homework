from quopri import encodestring
import numpy as np
import cv2
from matplotlib import pyplot as plt
import time

img = cv2.imread('cboard.jpg',0)

starttime = time.time()
orb = cv2.ORB_create()
kp = orb.detect(img,None)
kp, des = orb.compute(img, kp)
endtime = time.time()

print(round(endtime - starttime,3))
print(len(kp))
img = cv2.drawKeypoints(img,kp,img,color=(0,255,0), flags=0)

cv2.imshow('p',img)

cv2.waitKey()