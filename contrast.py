from imports import *

cont_img = cv2.addWeighted(img, 2.5, np.zeros(img.shape, img.dtype), 0, 0)
Hori = np.concatenate((img, cont_img), axis=1)
cv2.imshow('constrast image', Hori)
cv2.waitKey(0)