from tracemalloc import start
import cv2
import numpy as np
import time
     
     
def main():
     img = cv2.imread("cboard.jpg")
     img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
     
     starttime = time.time()
     sift = cv2.xfeatures2d.SIFT_create()          
     kp, des = sift.detectAndCompute(img_gray, None)
     outImage = cv2.drawKeypoints(img,kp,(255,0,0))
     endtime = time.time()

     print(round(endtime - starttime,3))
     print(len(kp))
     
     cv2.imshow("sift",outImage)
     cv2.imwrite("siftpoint.jpg",outImage)
     cv2.waitKey(0)
     cv2.destroyAllWindows()

     

if __name__ == "__main__":
     main()

