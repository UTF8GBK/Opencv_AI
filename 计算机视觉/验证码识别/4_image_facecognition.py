import cv2
import numpy as np
img =cv2.imread('./images/nba.jpg')

# 彩色图像转黑白好识别
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(gray.shape)

# 创建级联器 ： 给人脸数据返回可以识别的人脸对象
detector = cv2.CascadeClassifier('./images/haarcascade_frontalface_default.xml')
# image, scaleFactor=None :缩放比例默认 1.1 , minNeighbors=None, 左右临近默认3
# flags=None: 特征标注, minSize=None,识别最小人脸范围 maxSize=None： 最大人脸范围
# 优化级联器默认参数
face_zone = detector.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=3,
                          minSize=(50,50),maxSize=(150,150))

print(face_zone)  # 返回二维数组 ，每一个列表数据代表一个人脸的坐标轴与宽高
for x,y,w,h in face_zone:
    cv2.rectangle(img,pt1=(x,y),pt2=(x+w,y+h),color=(0,0,255),thickness=2)

    color = np.random.randint(0,255,3)
    cv2.circle(img,center=(x+w//2,y+h//2),radius=w//2,color=color.tolist(),thickness=2)

cv2.imshow("nba",img)
# cv2.imshow("gray",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()