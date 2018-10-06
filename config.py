# 创建redis存储对象，并在配置中填写相关配置
import redis

# 使用logging提供的模块级别的函数记录日志
import logging


class Config(object):
    """工程配置信息"""

    SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1:3306/Journal"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # flask_session的配置信息
    SESSION_TYPE = "redis"  # 指定 session 保存到redis 中
    SESSION_USE_SIGNER = True  # 让cookies 中的session_id 被加密签名处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    PERMANENT_SESSION_LIFETIME = 86400  # session 的有效期，秒

    # 默认日志等级
    LOG_LEVEL = logging.DEBUG


class DevelopmentConfig(Config):
    """开发模式的配置"""
    DEBUG = True


class ProductionConfig(Config):
    """生产模式下的配置"""
    LOG_LEVEL = logging.ERROR


# 定义配置字典
config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
