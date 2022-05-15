import cv2
import matplotlib.pyplot as plt
img = cv2.imread("./images/reba.jpg")  # BGR
recolor = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# plt.imshow(img[:,:,::-1]) # rgb
# plt.imshow(recolor)
# plt.show()

# img, 识别的图像
# pt1, 左上角的x,y 轴坐标
# pt2,  右下角的x,y，轴坐标
# color, 颜色
# thickness=None, 粗细
# lineType=None  线条的类型 默认4，8
cv2.rectangle(img,pt1=(130,120),pt2=(280,280),color=(0,0,255),thickness=2)
# img, center:圆点位置, radius：半径, color, thickness=None, lineType=None
cv2.circle(img,center=(200,200),radius=75,color=(255,255,0),thickness=2)
# img, pt1, pt2, color, thickness=None, lineType=None
cv2.line(img,pt1=(140,250),pt2=(260,250),color=(0,255,0),thickness=3)
# img, text:需要显示文本, org 文字显示在哪个坐标里面 , fontFace： 字体的类型, fontScale字体的大小,
# color, thickness=None
cv2.putText(img,'reba',org=(180,280),fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=1,color=(255,255,255),thickness=2)

cv2.imshow("reba",img)
cv2.waitKey(0)
cv2.destroyAllWindows()