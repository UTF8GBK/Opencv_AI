import cv2
import matplotlib.pyplot as plt
image_1 = cv2.imread('./opcv-image/bg1.jpg')
image_2 = cv2.imread('./opcv-image/bg2.jpg')

# plt.imshow(image_1)
# plt.imshow(image_2)
# plt.show()
face = image_2[100:280,180:320]  # 高 宽
image_1[150:330,180:320]  = face

cv2.imshow('face',face)
cv2.imshow('image_1',image_1)
cv2.waitKey(0)
cv2.destroyAllWindows()