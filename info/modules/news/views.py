# 使用蓝图
from flask import session, render_template, current_app
from . import news_blue

from werkzeug.security import generate_password_hash, check_password_hash


@news_blue.route('/')
def index():
    session['python14'] = '2018'
    return render_template('news/index.html')


# 图标favicon 的加载
@news_blue.route('/favicon.ico')
def favicon():
    """
    发送/favicon.ico路径下的图标加载
    """
    # 使用current_app调用flask内置的函数, 发送静态文件给浏览器, 实现logo图标的加载
    return current_app.send_static_file('news/favicon.ico')
