import face_recognition
from PIL import Image,ImageDraw
img = face_recognition.load_image_file('./images/reba.jpg')

# 获取人脸关键特征点
face_landmarks_list  = face_recognition.face_landmarks(img)
print(face_landmarks_list)

"""
chin  : 下巴
left_eyebrow ： 左眉毛
right_eyebrow：右眉毛
nose_bridge : 鼻梁
nose_tip ： 鼻尖
left_eye ： 左眼
right_eye ： 右眼
top_lip ： 上嘴唇
bottom_lip  ： 下嘴唇
"""
# 转换成类似于numpy数组的格式
pil_image = Image.fromarray(img)
# 生成PIL图片
d = ImageDraw.Draw(pil_image)

# 获取所有面部信息名称
for x in range(len(face_landmarks_list)):
    print(list(face_landmarks_list[x].keys()))

# 遍历所有的人脸特征点
for face_landmarks in face_landmarks_list:
    # 构建人脸面部信息的名称
    face_features = ['chin', 'left_eyebrow', 'right_eyebrow', 'nose_bridge',
                     'nose_tip', 'left_eye', 'right_eye', 'top_lip', 'bottom_lip']

    for face_feature in face_features:
        print(f"{face_feature}每个人脸面部特征显示的位置如下 ： "
              f"{face_landmarks[face_feature]}")
        d.line(face_landmarks[face_feature],width=5)
pil_image.show()



