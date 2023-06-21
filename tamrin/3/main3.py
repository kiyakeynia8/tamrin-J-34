import cv2

image = cv2.imread("input/watermelon.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

r, g, b = cv2.split(image)
nr = g
ng = r

n_image = cv2.merge([b,ng,nr])

cv2.imwrite("output/3_result.png", n_image)