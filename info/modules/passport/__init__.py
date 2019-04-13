from flask import Blueprint


passport_blue = Blueprint('passport_blue', __name__)

# 把使用蓝图对象的文件导入

from . import views

