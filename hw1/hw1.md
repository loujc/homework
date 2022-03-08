# 计算机视觉与增强现实技术-HW1
2101210612 楼锦程 

## 一、代码
```python
import cv2 as cv
def cv_demo():
    capture = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while(True):
        ref,frame = capture.read()
        cv.putText(frame,"hi~halo~hello~",(500,150),cv.FONT_HERSHEY_COMPLEX,2.0,(100,200,200),5)
        cv.imshow("1",frame)
        
        c = cv.waitKey(30) & 0xff
        if c == 27:
            capture.release()
            break

cv_demo()
```

## 二、效果图

<img src="1.jpg" alt="调用电脑摄像头" title="调用摄像头 " style="zoom:50%;" />

<img src="2.jpg" alt="在调用摄像头中插入字符" title="插入字符" style="zoom:50%;" />
