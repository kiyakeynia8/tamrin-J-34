import cv2
import numpy as np

image = cv2.imread("input/rgb.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def RGB_to_gray(image):
    s, c, _ = image.shape
    result = np.zeros((s,c),dtype= np.uint8)
    r, g, b = cv2.split(image)

    for i in range(s):
        for j in range(c):
            result[i,j] = (r[i,j] + g[i,j] + b[i,j]) // 3

    return result

image_gray = RGB_to_gray(image)

# image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite("output/1_result.png", image_gray)