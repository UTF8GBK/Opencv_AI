# opencv 是一个开源的计算机视觉库由C 与 C++ 所写
# pip install opencv-python -i https://pypi.douban.com/simple/
import cv2

# todo : 1. 读取图像
img = cv2.imread('./opcv-image/bg1.jpg',1)
print(img)
# todo 2. 显示图片
# winname: 窗体名字, mat ：需要显示图像值
cv2.imshow("girl",img)

# TODO： 保存图片
# filename:需要保存的文件名字或路径  ,img：图像
cv2.imwrite('./opcv-image/girl.jpg',img)

# todo : 3. 等待键盘输入 单位是毫秒 如果是0，无限等待
cv2.waitKey(0)

# todo : 4. opencv由C ++ 需要释放内存
cv2.destroyAllWindows()