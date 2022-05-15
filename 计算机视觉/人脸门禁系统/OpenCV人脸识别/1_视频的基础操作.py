import cv2

# 读取视频
cap = cv2.VideoCapture('./images/girl.mp4')
print(cap)   # 是否获取到视频

# 获取视频的帧数   1秒24帧
print(f"视频的帧数：{cap.get(propId=cv2.CAP_PROP_FPS)}")

# 获取总帧数  : 多少张图片
print(f"视频的总帧数：{cap.get(propId=cv2.CAP_PROP_FRAME_COUNT)}")

# 获取视频的宽度
print(f"视频的宽度:{cap.get(propId=cv2.CAP_PROP_FRAME_WIDTH)}")

# 获取视频的高度
print(f"视频的高度：{cap.get(propId=cv2.CAP_PROP_FRAME_HEIGHT)}")
# 读取视频第一帧   flag: true false ,frame：返回图像
flag ,frame = cap.read()
cv2.imshow("girl",frame)
cv2.waitKey(0)
cv2.destroyAllWindows()