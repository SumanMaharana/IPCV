from imports import *

blur_filter1 = np.ones((3, 3), np.float32)/30
blur_filter2 = np.ones((5, 5), np.float32)/30
blur_filter3 = np.ones((7, 7), np.float32)/30

img_blur1 = cv2.filter2D(src=img, ddepth=-1, kernel=blur_filter1)
img_blur2 = cv2.filter2D(src=img, ddepth=-5, kernel=blur_filter2)
img_blur3 = cv2.filter2D(src=img, ddepth=-15, kernel=blur_filter3)

Hori = np.concatenate((img_blur1, img_blur2, img_blur3), axis=1)
cv2.imshow('blurred images', Hori)
cv2.waitKey(0)