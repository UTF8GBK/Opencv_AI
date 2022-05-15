# pip install scikit-image
# pip install cmake
# pip install openv-python
# pip install dlib==19.7     # Python3.6
# pip install face_recognition
# face_recognition : 基于dlib 进行二次封装 ，号称世界上最简洁的人脸识别库
import face_recognition
import cv2
from  PIL import Image   # pip install pillow
# 加载图像，返回numpy数组，记录所有图像像素的位置
img = face_recognition.load_image_file('./images/reba.jpg')
print(img)
# 获取图像中所有人脸的位置
face_locations = face_recognition.face_locations(img)
print(f"人脸信息位置{face_locations}")


print(f"已经识别到人脸：{len(face_locations)}")
for face_location in face_locations:   # 遍历人脸信息位置
    top ,right,bottom,left = face_location
    print("已经识别到人脸部位,像素区域 : top{},right{},bottom{},left{}".format(top ,right,bottom,left))
    face_image = img[top:bottom,left:right]  # 切片获取识别部分的图像
    pil_image = Image.fromarray(face_image)  # 转换成类似numpy 数组的格式
    pil_image.show()   # 显示图像
    # 绘制矩形框
    start = (left,top)
    end = (right,bottom)
    cv2.rectangle(img,start,end,(0,0,255),thickness=2)
    cv2.imshow("img",img[:,:,::-1])  # BGR -> RGB
    cv2.waitKey(0)

cv2.destroyAllWindows()