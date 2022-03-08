# 第二次作业
2101210612 楼锦程

## 代码

```python
import cv2
import numpy as np
import random
 
def white_balance_1(img):
    '''
    第一种简单的求均值白平衡法
    :param img: cv2.imread读取的图片数据
    :return: 返回的白平衡结果图片数据
    '''
    # 读取图像
    r, g, b = cv2.split(img)
    r_avg = cv2.mean(r)[0]
    g_avg = cv2.mean(g)[0]
    b_avg = cv2.mean(b)[0]
    # 求各个通道所占增益
    k = (r_avg + g_avg + b_avg) / 3
    kr = k / r_avg
    kg = k / g_avg
    kb = k / b_avg
    r = cv2.addWeighted(src1=r, alpha=kr, src2=0, beta=0, gamma=0)
    g = cv2.addWeighted(src1=g, alpha=kg, src2=0, beta=0, gamma=0)
    b = cv2.addWeighted(src1=b, alpha=kb, src2=0, beta=0, gamma=0)
    balance_img = cv2.merge([b, g, r])
    return balance_img

'''
img : 原图
img1：均值白平衡法

'''
img = cv2.imread('/Users/nikolas_loujc/Documents/个人/study_work/rw_course/second_sem/cv_ar/hw2/blue.jpeg')
img1 = white_balance_1(img)


cv2.imshow('origin',img)
cv2.imshow('result',img1)
cv2.waitKey(0)
```



## 结果

![result](/Users/nikolas_loujc/Documents/个人/study_work/rw_course/second_sem/cv_ar/hw2/result.jpg)
