import face_recognition

img = face_recognition.load_image_file('./images/reba.jpg')

# 获取人脸面部编码信息
face_encodings  = face_recognition.face_encodings(img)
print(face_encodings)

"""
返回一个编码列表，都是我们需要识别的对象，如果我们需要
访问面部编码信息，需要添加索引或者遍历进行访问，共有人脸编码信息128向量
"""
for face_encoding in face_encodings:
    print(f"编码信息的长度：{len(face_encoding)}，编码信息为：{face_encoding}")