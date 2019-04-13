# 使用蓝图
from flask import session
from . import passport_blue


# 若是jsonify返回的数据，content_type为application/json ,  字典转化为json对象
# 若是json.dumps()返回的数据，本质为字符串，所以content_type为text/html,  字典转化为字符串

@passport_blue.route('/image_code')
def generate_image_code():
    """生成图片验证码"""
    # 获取前端传入的图片验证码的编号uuid
    # image_code_id = request.args.get('image_code_id')
    pass