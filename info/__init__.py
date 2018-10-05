import redis
# 先在当前类中定义配置的类，并从中加载配置
from flask import Flask
from config import Config
# 导入数据库扩展，并在配置中填写相关配置
from flask_sqlalchemy import SQLAlchemy

# 包含请求体的请求都需要开启CSRF
from flask_wtf.csrf import CSRFProtect

# 利用 flask-session扩展，将 session 数据保存到 Redis 中
from flask_session import Session

# 传入配置字典
from config import config


db = SQLAlchemy()
redis_store = None


def create_app(config_name):
    """通过传入不同的配置名字，初始化其对应配置的应用实例"""

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

    return app


