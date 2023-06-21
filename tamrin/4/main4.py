import cv2
import numpy as np

image = cv2.imread("input/rubik.png")
s, c, _ = image.shape

for i in range(s):
    for j in range(c):
        b, g, r = image[i][j]
        if b > 150 and g > 150 and r > 150:
            continue
        elif b > 150 and g > 150:
            image[i][j] = np.array((0, 0, 255))
        elif b > 150 and r > 150:
            image[i][j] = np.array((0, 255, 0))
        elif g > 150 and r > 150:
            image[i][j] = np.array((255, 0, 0))

cv2.imwrite("output/4_result.png", image)