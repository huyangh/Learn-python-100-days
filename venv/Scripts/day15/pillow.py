"""
Time   : 2020/6/19 17:10
Author : huyangh
演示使用pillow模块进行图片操作
"""
from PIL import Image, ImageFilter, ImageGrab


img = Image.open('images/1.png')
print(img.size, img.format, img.mode)
# 高斯模糊滤镜
img2 = img.filter(ImageFilter.GaussianBlur)
img2.save('images/1_blur.png')
# 锐化滤镜
img3 = img.filter(ImageFilter.SHARPEN)
img3.save('images/1_sharpen.png')
# 转换为黑白图片
img4= img.convert('L')
img4.save('images/1_black.png')
# 屏幕截图
# ImageGrab.grab((0, 0, 1920, 1080)).show()

"""下面演示图片变换"""
# 调整图像大小
# img.resize((1280,720)).show()
# 图片旋转90度，但图片部分被切除
# img.rotate(90).show()
# 图片左右镜像
# img.transpose(Image.FLIP_LEFT_RIGHT).show()
# 图片旋转90度，保留完整图片
# img.transpose(Image.ROTATE_90).show()

