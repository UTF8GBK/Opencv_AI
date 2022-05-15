# 裁剪 J 扑克出来 ，调整这个J扑克的大小

import cv2
import matplotlib.pyplot as plt     # pip install matplotlib
img = cv2.imread('./opcv-image/king.jpg')

# plt.imshow(img)
# plt.show()
imgcopy = img[320:550,210:390]
shape = imgcopy.shape

cpoy_img = cv2.resize(imgcopy,(shape[0]*12//10,shape[1]*2))

cv2.imshow("king",img)
cv2.imshow("imgcopy",cpoy_img)
cv2.waitKey(0)
cv2.destroyAllWindows()