from redis import StrictRedis
import pymysql
pymysql.install_as_MySQLdb()


class Config(object):
    DEBUG = None
    # 设置密钥
    # import os, base64  a = os.urandom(50)  base64.b64encode(a)
    # Session, Cookies以及一些第三方扩展都会用到SECRET_KEY值，这是一个比较重要的配置值，应该尽可能设置为一个很难猜到的值，随机值更佳。
    SECRET_KEY = 'cYaRoiV/yG7qq6L2/nPHKOgqGspSjkBDJ02iWrhQFJaz8002cI3GbjsZnP5tEV3vad8='

    # 配置mysql数据库的连接信息
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost/info'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 追踪对象的修改并且发送信号

    # 配置状态保持中的session信息，存储在redis数据库中
    SESSION_TYPE = 'redis'
    SESSION_REDIS = StrictRedis(host='127.0.0.1', port=6379)  # session连接的redis数据库实例
    SESSION_USE_SIGNER = True  # session签名
    PERMANENT_SESSION_LIFETIME = 86400  # session有效期


# 实现开发模式下的配置信息
class DevelopmentConfig(Config):
    DEBUG = True


# 实现生产模式下的配置信息
class ProductionConfig(Config):
    DEBUG = False


# 定义字典，实现配置对象的映射
config_dict = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
