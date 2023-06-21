import cv2
import numpy as np

image = np.ones([600, 1100, 3], np.uint8)*255
cv2.circle(image, (500, 600), 150, (130,000,140), 50)
cv2.circle(image, (500, 600), 200, (255,000,000), 50)
cv2.circle(image, (500, 600), 250, (250,250,000), 50)
cv2.circle(image, (500, 600), 300, (000,130,000), 50)
cv2.circle(image, (500, 600), 350, (000,255,255), 50)
cv2.circle(image, (500, 600), 400, (000,160,255), 50)
cv2.circle(image, (500, 600), 450, (000,000,255), 50)
image[600:, :, :] = 255
cv2.imwrite("output/2_result.png", image)