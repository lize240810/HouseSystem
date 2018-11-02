# -*- coding:utf-8 -*-
'''
https://docs.python.org/3/library/base64.html
https://docs.python.org/3/library/io.html#io.StringIO
https://docs.python.org/3/library/io.html#io.BytesIO
https://developer.mozilla.org/zh-CN/docs/Web/HTTP/data_URIs
'''
# 图片处理第三方库
from PIL import (
    Image,  # 打开图像
    ImageDraw, # 提供了简单的2D绘画 , 圆,点,线
    ImageFont, # 提供字体
    ImageFilter # 滤镜模块
                )
# 随机数
import random
# 编码解码模块
import base64
# 文件流
from io import BytesIO

def rndChar():
    '''随机字母(大写)随机返回ASCII值'''
    # chr转换
    return chr(random.randint(65,90))

# 随机颜色
def rndColor():
    '''背景颜色'''
    # 三原色 
    return (random.randint(150,255),random.randint(150,255),random.randint(150,255))

# 模拟查看
# Image.new('RGB', (100, 100), rndColor()).show()

def rndColor2():
    '''字体颜色'''
    return (random.randint(1, 108),random.randint(1, 109),random.randint(1, 120))

def random_str(length):
    '''生成随机长度的字符串'''
    ret = [] # 存放每个字符
    for i in range(length):
        char = rndChar() # 随机字符穿
        ret.append(char) # 添加到列表中
        # 返回一个整体字符串
    return ''.join(ret)

def random_image(rand_str):
    '''生成随机图片'''
    # 图片大小:132 *60
    width = 33*4
    height = 60
    # 创建Image对象,背景为白色
    image = Image.new('RGB', (width,height),(255, 255, 255))
    # 创建Draw对象
    draw = ImageDraw.Draw(image)
    # 字体选择
    font = ImageFont.truetype(r'C:\windows\Fonts\SIMYOU.TTF', 39)
    # 用随机颜色填充每个像素 随机画点
    for x in range(width):
        for y in range(height):
            # 随机坐标点
            px = random.randint(0, width +1)
            py = random.randint(0, height +1)
            point =(px ,py)
            # 随机画点
            draw.point(point, fill=rndColor())
            # 随机画线
            if px % (x % 9+1) == 0 and py % (y % 7 + 1) == 0:
                lw = random.randint(x + 1, width)
                ls = [x // lw, py, px, py // lw]
                if x % 2 == 0:
                    ls = [px, py, x // lw, y]
                draw.line(
                    ls,
                    fill=rndColor(),
                    width=1)
    # 输出4个字母，字母颜色随机
    for t, char in enumerate(rand_str):
        draw.text((30 * t + 10, 10), char, font=font, fill=rndColor2())

    # 对图像模糊
    image = image.filter(ImageFilter.BLUR)

    return image       

def image2base64(image):
    '''图片转换Wiebase64'''
    buffer = BytesIO()
    # 保存图片的格式
    image.save(buffer, 'PNG')
    # 释放资源
    image.close()
    # 图片转换为二进制
    data = buffer.getvalue()
    buffer.close()
    # 转换为base必须设置两次才可以完成
    # b64encode 编码
    # b64decode 解码
    encoded = base64.b64encode(data).decode('utf-8','ignore')
    # 设置base64显示图片的格式
    uri = 'data:image/png;base64,{0}'.format(encoded)
    return uri

# 整合的方法 使用了随机生成图片和图片转换为base64的图片
def random_base64_image(rand_str):
    '''随机生成base格式的图片'''
    image = random_image(rand_str)
    return image2base64(image)

if __name__ == '__main__':
    random_str = random_str(4)
    image = random_image(random_str)
    # print(random_base64_image(random_str))
    image.show()
