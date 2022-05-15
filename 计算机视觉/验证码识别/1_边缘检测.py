import cv2

img = cv2.imread('./images/chair.jpg')

# image, : 需要识别的图像
# threshold1, 处理过程中第一个阈值
# threshold2, 处理过程中第二次阈值
# edges=None, 计算得到边缘图像
# apertureSize=None  孔径的大小
canny = cv2.Canny(img,threshold1=10,threshold2=240)
cv2.imshow("chair",img)
cv2.imshow("canny",canny)
cv2.waitKey(0)
cv2.destroyAllWindows()