import cv2
from kiya_RGB_to_gray import RGB_to_gray


image = cv2.imread("input/rgb.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

image_gray = RGB_to_gray(image)

# image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite("output/1_result.png", image_gray)