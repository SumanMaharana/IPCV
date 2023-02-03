from imports import *

cv2.imshow('original image' , img)
cv2.waitKey(1000)
cv2.destroyWindow('original image')
scale_percent = int(input("Enter a number to scale the image by : "))
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
newlmg = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
print('Resized Dimensions : ', newlmg)
cv2.imshow('Resized Image : ' ,newlmg)
cv2.waitKey(0)
cv2.destroyAllWindows()