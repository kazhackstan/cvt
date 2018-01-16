import cv2
import numpy as np

# img = cv2.imread("small.png")

# cv2.imshow("Window", img)
# k = cv2.waitKey(0)

# print img.shape
# print type(img)
# print type(img[0, 0, 0])

# print img[0:5,0:5,:]

car = cv2.imread("car.jpg")
gray_opencv = cv2.cvtColor(car, cv2.COLOR_BGR2GRAY)
# manual = np.dot(car[...,:3], [0.114, 0.587, 0.299])
# manual = np.asarray(manual, dtype = np.uint8)
# cv2.imshow("OpenCV", gray_opencv)
# cv2.imshow("Man", manual)
# cv2.waitKey(0)

# a = np.full((500,500), 255, dtype=np.uint8)
# a[200:300,200:300] = 0
# print cv2.imshow("Window", a)
# cv2.waitKey(0)

# kern = np.full((3,3), 1, dtype=np.float64) / 9
# out = cv2.filter2D(gray_opencv, -1, kern)
# cv2.imshow('blur filter', out)
# cv2.waitKey(0)

kern = np.full((5,5), 1, dtype=np.float64) / 25
out = cv2.GaussianBlur(gray_opencv, (25,25), 5)
cv2.imshow('blur filter', out)
cv2.waitKey(0)