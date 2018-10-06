import redis
# 先在当前类中定义配置的类，并从中加载配置
from flask import Flask

# 导入数据库扩展，并在配置中填写相关配置
from flask_sqlalchemy import SQLAlchemy

# 包含请求体的请求都需要开启CSRF
from flask_wtf.csrf import CSRFProtect

# 利用 flask-session扩展，将 session 数据保存到 Redis 中
from flask_session import Session

# 传入配置字典
from config import config
# 加载配置
from config import Config

# 导入标准模块
import logging
from logging.handlers import RotatingFileHandler

db = SQLAlchemy()
redis_store = None


def create_app(config_name):
    """通过传入不同的配置名字，初始化其对应配置的应用实例"""

    # 配置项目日志
    setup_log(config_name)

    app = Flask(__name__)

    # 配置
    app.config.from_object(config[config_name])
    # 配制数据库
    db.init_app(app)
    # 配置redis
    redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
    # 开启csrf保护
    CSRFProtect(app)
    # 配置session保存位置
    Session(app)

    # 注册蓝图
    from info.modules.index import index_blu
    app.register_blueprint(index_blu)

    return app


def setup_log(config_name):
    # 设置日志的记录等级
    logging.basicConfig(level=config[config_name].LOG_LEVEL)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小100、保存的日志文件个数上限10
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式               日志等级 输入日志信息的文件名 行数    日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')

    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）  添加日志记录器
    logging.getLogger().addHandler(file_log_handler)
