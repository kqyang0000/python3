import random

from PIL import Image, ImageDraw, ImageFont, ImageFilter


# 随机字母
def mdchar():
    return chr(random.randint(65, 90))


# 随机颜色1
def mdcolor1():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 随机颜色2
def mdcolor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


# 240*40
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象
font = ImageFont.truetype('Arial.ttf', 36)
# 创建Draw对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=mdcolor1())
# 输出文字
for i in range(4):
    draw.text((60 * i + 10, 10), mdchar(), font=font, fill=mdcolor2())
# 模糊
image = image.filter(ImageFilter.BLUR)
image.save('/Users/yangkaiqiang/Desktop/images/code_2.jpeg', 'jpeg')
