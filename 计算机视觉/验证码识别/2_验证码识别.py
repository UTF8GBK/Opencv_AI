# pip install pytesseract
import cv2
import pytesseract

img = cv2.imread('./images/code.png',0)

# 过滤阈值
# src:需要处理图像, thresh：127, maxval:255, type：怎么处理阈值
# 小于等于阈值 127 为 0 ，大于阈值127 为255
t,res = cv2.threshold(img,thresh=127,maxval=255,type=cv2.THRESH_BINARY)
print(t)

# pytesseract.pytesseract.TesseractNotFoundError: tesseract is not installed or it's not in your PATH.
# 找到pytesseract.py 文件修改  tesseract——cmd 指向你安装的 tesseract.exe 执行文件
# 使用pytesseract识别验证码图像
result = pytesseract.image_to_string(res)
print(result)

cv2.imshow("code",img)
cv2.imshow("res",res)
cv2.waitKey(0)
cv2.destroyAllWindows()
