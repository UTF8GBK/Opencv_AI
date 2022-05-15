import dlib
import cv2
from imutils import face_utils
from scipy.spatial import distance

def eye_aspect_ration(eye):
    # 计算欧式距离
    A = distance.euclidean(eye[1],eye[5])
    B = distance.euclidean(eye[2],eye[4])
    C = distance.euclidean(eye[0],eye[3])
    return (A + B) / (2.0 * C)


def work():
    # 获取人脸检测器。包含很多人脸检测算法
    detector = dlib.get_frontal_face_detector()
    print(detector)
    #加载68个人脸特征数据
    predictor = dlib.shape_predictor("data/shape_predictor_68_face_landmarks.dat")
    print(predictor)

    # 设置眼睛纵横比阈值
    EAR = 0.3
    # 假设连续3次帧以上EAR小于0.3
    EAR_eye = 3
    left_start = 37 -1
    left_end = 42 -1
    right_start = 43-1
    right_end = 48 -1

    frame_count = 0  # 连续帧的计数
    blink_count = 0  # 闭眼计数

    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    while True:
        flat , frame = cap.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        # 用人脸检测器读取人脸数据,参数1： 图像。参数2：读取图像像素并放大一倍，收集更多的细节
        rects = detector(gray,1)

        #如果有人脸数据
        if len(rects) > 0:
            #rects[0] ：眼睛部分的特征点
            shape = predictor(gray,rects[0])  # 检测特征点
            points = face_utils.shape_to_np(shape) # 将特征点转换成numpy数组
            # 取出左右眼的特征值
            lefteye = points[left_start:left_end + 1]
            righteye = points[right_start:right_end + 1]

            leftear = eye_aspect_ration(lefteye)
            rightear = eye_aspect_ration(righteye)

            # 求左右眼的EAR平均值
            ear = (leftear + rightear) / 2.0
            # 寻找左右眼的轮廓
            lefthull = cv2.convexHull(lefteye)
            righthull = cv2.convexHull(righteye)

            # 绘制轮廓
            # image, contours: 需要绘制轮廓, contourIdx：绘制轮廓的索引，-1：自己匹配, color, thickness=None,
            cv2.drawContours(frame,[lefthull],-1,(0,0,255),2)
            cv2.drawContours(frame,[righthull],-1,(0,0,255),2)

            # 如果ear 小于阈值，开始计算连续帧
            if ear < EAR:
                frame_count += 1
            else:
                if frame_count >= EAR_eye:
                    print("眨眼检测成功！已开门！")
                    blink_count +=1
                    break
                frame_count = 0

        cv2.imshow('eye',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()



if __name__ == '__main__':
    work()