import cv2
import matplotlib.pyplot as plt     # pip install matplotlib
img = cv2.imread('./opcv-image/king.jpg')

# plt.imshow(img)
# plt.show()
imgcopy = img[45:290,20:200]


cv2.imshow("king",img)
cv2.imshow("imgcopy",imgcopy)
cv2.waitKey(0)
cv2.destroyAllWindows()