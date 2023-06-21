import cv2
import numpy as np

r = np.ones((240,480), np.uint8)* 85
r[80:118, 80:118] = 255
r[123:160, 123:160] = 255

g = np.ones((240,480), np.uint8)* 85
g[80:118, 123:160] = 255
g[123:160, 123:160] = 255

b = np.ones((240,480), np.uint8)* 85
b[123: 160, 80:118] = 255

image = cv2.merge([b,g,r])

cv2.putText(image, 'Microsoft', (160, 140), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)

cv2.imwrite("output/5_result.png", image)