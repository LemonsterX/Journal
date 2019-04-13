from flask import Blueprint


news_blue = Blueprint('news_blue', __name__)

# 把使用蓝图对象的文件导入

from . import views

