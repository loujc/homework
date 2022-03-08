import cv2 as cv
def cv_demo():
    capture = cv.VideoCapture(0)
    # if not cap.isOpened():
    #     print("Cannot open camera")
    #     exit()
    while(True):
        ref,frame = capture.read()
        cv.putText(frame,"hi~halo~hello~",(500,150),cv.FONT_HERSHEY_COMPLEX,2.0,(100,200,200),5)
        cv.imshow("1",frame)
        
        c = cv.waitKey(30) & 0xff
        if c == 27:
            capture.release()
            break

cv_demo()
