#get a photo with mulabue coins and return the number of coins

import numpy as np
import cv2
from PIL import Image, ImageEnhance


image_path = '/Users/USER/Desktop/photos for project/coin_temp.png'

def coin_num(image_path):
    img = cv2.imread(image_path)
    #cv2.imshow("coin", img)  #
    #cv2.waitKey(0) #
    #cv2.destroyAllWindows() #

    img = cv2.resize(img, (450, 800))
    image_copy = img.copy()
    img = cv2.GaussianBlur(img, (9, 9), 3)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v, 27)
    hsv_brightened = cv2.merge((h, s, v))
    img = cv2.cvtColor(hsv_brightened, cv2.COLOR_HSV2BGR)
    # cv2.imshow("coin", img)#
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # cv2.waitKey(0)#
    # cv2.destroyAllWindows()#

    ret, thresh = cv2.threshold(gray, 145, 255, cv2.THRESH_BINARY)
    #cv2.imshow("coin", thresh) #
    #cv2.waitKey(0) #
    #cv2.destroyAllWindows() #
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    area = {}
    for i in range(len(contours)):
        cnt = contours[i]
        ar = cv2.contourArea(cnt)
        area[i] = ar
    srt = sorted(area.items(), key=lambda x: x[1], reverse=True)
    results = np.array(srt).astype("int")
    num = np.argwhere(results[:, 1] > 500).shape[0]

    # for i in range(1, num):
    # image_copy = cv2.drawContours(image_copy, contours, results[i, 0],
    # (0, 255, 0), 3)
    # print("Number of coins is ", num - 1)
    # cv2.imshow("final", image_copy)#
    # cv2.waitKey(0)#
    # cv2.destroyAllWindows()#
    return num - 1

#print(coin_num(image_path))



