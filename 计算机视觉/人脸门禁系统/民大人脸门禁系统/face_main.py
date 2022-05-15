import face_recognition
import cv2
import os
import time
import threading
from queue import Queue
from PIL import Image,ImageDraw,ImageFont
import numpy as np




def load_image(path,q):
    print("正在加载已知人员图片.....")
    facelib  = []   # 定义空列表，用来存储所有的面部编码信息
    # 文件的路径，文件夹名字，图像名字
    for dirpath,dirname,filenames in os.walk(path):
        print((dirpath,dirname,filenames))
        # 把路径与名字拼接起来
        for filename in filenames:
            # 将列表中的元素按照相对于平台的路径分隔符拼接起来
            filepath = os.sep.join([dirpath,filename])
            # print(filepath)
            # 加载所有员工的图片
            face_image = face_recognition.load_image_file(filepath)
            # 获取对应的面部编码信息
            face_encoding = face_recognition.face_encodings(face_image)[0]
            facelib.append(face_encoding)
        # return facelib,filenames
        while True:
            q.put((facelib,filenames))
            if q.empty() == False:
                break

def start_camera(q):
    facelib ,facenames = q.get()
    # print(facelib,facenames)
    video_cap = cv2.VideoCapture(0)    #初始化摄像头参数0表示默认为笔记本的内置第一个摄像头，如果需要读取已有的视频则参数改为视频所在路径路径，例如：cap=cv2.VideoCapture(‘video.mp4’)

    # 调用摄像头
    while True:
        # 捕获帧
        ret,frame = video_cap.read()
        # 把图片缩小1/4 ,提高识别效率 ,参数 ：识别图片,输出图片的尺寸，fx,fy-> x轴y轴
        small_image = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
        rbg_image = small_image[:,:,::-1]   # BGR  ->  RBG

        # 获取摄像头人脸位置
        face_locations = face_recognition.face_locations(rbg_image)   # 获取人脸位置信息
        face_encodings = face_recognition.face_encodings(rbg_image,face_locations)  # 获取人脸面部编码

        face_names = []   # 定义空列表存储所有的匹配成功人员名字
        # 遍历多张人脸
        for face_encoding in face_encodings:
            # 匹配人脸 ，matches true  false
            matches = face_recognition.compare_faces(facelib,face_encoding,tolerance=0.39)
            name = '未知人员'

            if True in matches:
                #取出已知人员的未知索引
                first_match_index = matches.index(True)
                name = facenames[first_match_index][:-4]
            face_names.append(name)

        for (top,right,bottom,left),name in zip(face_locations,face_names):
            top *= 4
            right *= 4
            bottom *= 4.


            left *= 4
            # 绘制矩形
            # img, pt1, pt2, color, thickness=None, lineType=None
            cv2.rectangle(img=frame,pt1=(left,top),pt2=(right,bottom),color=(0,0,255),thickness=2)
            # 转换类似于numpy 格式
            img_PIL = Image.fromarray(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
            # 设置字体
            font = ImageFont.truetype('msyh.ttc',40)
            # 生成一张PIL图像
            draw = ImageDraw.Draw(img_PIL)
            draw.text((left + 6 ,bottom -6),name,font=font,fill=(255,255,255))
            frame = cv2.cvtColor(np.asarray(img_PIL),cv2.COLOR_RGB2BGR)

        cv2.imshow('video',frame)
        if cv2.waitKey(3) & 0xFF == ord('q'):
            break
    video_cap.release()
    cv2.destroyAllWindows()



if __name__ == '__main__':
    start_time =  time.time()
    # facelib,filenames = load_image('image')
    # print(facelib,filenames)
    q = Queue(4)
    t1 = threading.Thread(target=load_image,args=('image',q))
    t2 = threading.Thread(target=start_camera,args=(q,))
    t1.start()
    t2.start()
    end_time  = time.time()
    print(end_time- start_time)