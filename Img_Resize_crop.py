import cv2
import numpy as np

img = cv2.imread("Resources/lambo.PNG")
print(img.shape)

imgResize = cv2.resize(img,(300,200))
print(imgResize.shape)

imgCropped = img[0:200,0:500]

cv2.imshow("image",img)
cv2.imshow("Resize",imgResize)
cv2.imshow("Cropped",imgCropped)
cv2.waitKey(0)