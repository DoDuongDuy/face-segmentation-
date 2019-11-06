import cv2
import numpy as np
while  True:
    image = cv2.imread('image2.png')
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    low = np.array([5, 50, 50],np.uint8)
    up = np.array([15, 255, 255],np.uint8)
    mask = cv2.inRange(hsv, low, up)
    res = cv2.bitwise_and(image,image,mask = mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()