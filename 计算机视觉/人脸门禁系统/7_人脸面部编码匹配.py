import face_recognition

# 加载合照 ： 判断迪丽热巴是否在照片里面
img1 = face_recognition.load_image_file('./images/setreba.jpg')
# 单人照片
img2 = face_recognition.load_image_file('./images/reba.jpg')
# 获取已经知道的人脸编码信息
known_face_encodings = face_recognition.face_encodings(img1)
# 编码信息返回列表
compare_face_encodings = face_recognition.face_encodings(img2)[0]

matches = face_recognition.compare_faces(known_face_encodings,compare_face_encodings,tolerance=0.5)
# 返回布尔值
print(matches)