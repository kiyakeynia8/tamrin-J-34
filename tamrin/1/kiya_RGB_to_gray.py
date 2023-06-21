import cv2
import numpy as np

def RGB_to_gray(image):
    s, c, _ = image.shape
    result = np.zeros((s,c),dtype= np.uint8)
    r, g, b = cv2.split(image)

    for i in range(s):
        for j in range(c):
            result[i,j] = (r[i,j]/ 3) + (g[i,j]/ 3) + (b[i,j]/ 3)

    return result