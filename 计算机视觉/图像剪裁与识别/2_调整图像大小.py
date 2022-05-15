import cv2

img = cv2.imread('./opcv-image/bg1.jpg')
# 调整图片的大小  -》 硬编码
# src :图像, dsize ：你需要修改的图像大小
big_resize = cv2.resize(img,(800,800))  # 增大图片
small_resize = cv2.resize(img,(500,500))  # 缩小图片

# 如果不想对宽度和高度进行硬编码，也可以使用形状的索引来增加宽度和高度
shape = img.shape
print(shape)
resize1 = cv2.resize(img,(shape[0]//2,shape[1]//2))
resize2 = cv2.resize(img,(shape[0]*2,shape[1]*2))

# 显示原图
cv2.imshow('img',img)
cv2.imshow('resize1',resize1)
cv2.imshow('resize2',resize2)
# cv2.imshow('big_resize',big_resize)   # 显示增大后图像
# cv2.imshow('small_resize',small_resize) # 显示缩小后图像

cv2.waitKey(0)

cv2.destroyAllWindows()