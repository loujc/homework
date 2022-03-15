from unittest import result
import cv2
import os
import numpy as np

filename = "finger.jpeg"
img_size = (640, 640)


def autoDetectPoints(img):

    # RGB to GRAY 并且二值化
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, img_b = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

    # 图像structure element，即刷子的粗细
    kernel = np.ones((5, 5), np.uint8)

    # 图像预处理——图像膨胀、图像腐蚀、寻找轮廓
    img_dilate = cv2.dilate(img_b, kernel, iterations=8)
    img_erode = cv2.erode(img_dilate, kernel, iterations=3)
    contours, hierarchy = cv2.findContours(img_erode, cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)

    # 提取出最大轮廓
    contour = contours
    docCnt = None
    if len(contour) > 0:
        contour = sorted(contour, key=cv2.contourArea,      # 根据轮廓面积从大到小排序
                         reverse=True)  
        for c in contour:
            peri = cv2.arcLength(c, True)  # 计算轮廓周长
            approx = cv2.approxPolyDP(c, 0.04 * peri, True)  # 轮廓多边形拟合
            # 轮廓为4个点表示找到纸张
            if len(approx) == 4:
                docCnt = approx
                break
            
    return docCnt


if __name__ == '__main__':
    img = cv2.imread(filename)
    approx = autoDetectPoints(img)

    # 映射变换
    src = np.float32(approx)
    dst = np.float32([[0, 0], [0, img_size[1]], [img_size[0], img_size[1]],
                      [img_size[0], 0]])
    print(src,"\n", dst)
    M = cv2.getPerspectiveTransform(src, dst)
    result = cv2.warpPerspective(img, M, img_size)

    cv2.imshow('result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()