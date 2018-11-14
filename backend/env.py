'''
    目录文件
'''

import os

# 后端目录(带文件名的)
DIR_BACKEND = os.path.dirname(os.path.abspath(__file__))

# 项目目录(不带文件名)
DIR_PROJ = os.path.dirname(DIR_BACKEND)

# 前端目录
DIR_FRONTEND = os.path.join(DIR_PROJ,'frontend')

# 前端模板目录
DIR_TEMPLATES = os.path.join(DIR_FRONTEND,'templates')

# 前端静态目录
DIR_STATIC = os.path.join(DIR_FRONTEND,'static')
