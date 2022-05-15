import cv2

# 初始化摄像头
cap = cv2.VideoCapture(0)   # 摄像头的id
w = int(cap.get(propId=cv2.CAP_PROP_FRAME_WIDTH)) + 1
h = int(cap.get(propId=cv2.CAP_PROP_FRAME_HEIGHT)) + 1
# 写视频
video_write = cv2.VideoWriter('./liangzai.avi',cv2.VideoWriter_fourcc('M','P','4','2'),
                              24,(w,h))

# 创建级联器 : 给人脸特征数据 ,返回人脸可识别的人脸对象
detector = cv2.CascadeClassifier('./images/haarcascade_frontalface_default.xml')
# 死循环判断是否初始化成功
while cap.isOpened():
    # 捕获帧
    flag ,frame = cap.read()
    if flag == False:
        break
    # image:图像, scaleFactor=None：缩放比例, minNeighbors=None：近邻数,
    # flags=None：标注, minSize=None：最小人脸范围, maxSize=None 最大人脸范围
    face_zone = detector.detectMultiScale(frame,scaleFactor=1.3,minNeighbors=5,
                              minSize=(150,150),maxSize=(350,350))
    for x,y,w,h in face_zone:  # 可以识别的人脸数据 （x,y,w,h）
        #img, center:圆心, radius：半径, color, thickness=None：线条粗细, lineType=None ： 线条类型
        cv2.circle(frame,center=(x+w//2,y+h//2),radius=w//2,color=[0,0,255],thickness=2)
        video_write.write(frame)   # 写视频
        cv2.imshow("girl",frame)
        if ord('q') == cv2.waitKey(3):  # 正常帧数 30 -60  1秒24
            break
cv2.destroyAllWindows()
cap.release()  # 释放摄像头
video_write.release()   #释放写视频