from flask import (
    Flask, request, Response, make_response, g,
    render_template, jsonify, url_for, session,
    redirect
)

from database import db, User
from utils import md5, is_email, is_phone
from safe import login_required
from captcha import random_str, random_base64_image

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# SECRET(秘密) session 秘匙
app.config['SECRET_KEY'] = 'session'

@app.route('/')
@login_required
def view_index():
    return render_template('index.html')

@app.route('/login')
def view_login():
    not_in_g = not hasattr(g, 'login_user') or g.login_user is None
    not_in_s = 'login_user' not in session or session['login_user'] is None
    if not_in_g and not_in_s:
        return render_template('login.html')
    return redirect(url_for('view_index'))


@app.route('/logout')
def view_logout():
    session.pop('login_user', None)
    return redirect(url_for('view_login'))


@app.route('/ajax-login')
def ajax_login():
    # 获取前端传递的参数
    username = request.values.get('username')
    password = request.values.get('pass')
    # 验证前端参数
    # ***注意***：前端不可信（请求可伪造），后端必须要验证前端传递的内容（此步骤不可省略）
    if not bool(username):
        return jsonify({
            'error': 2,
            'desc': '请提供用户名'
        })
    else:
        if not is_user_exists(username):
            return jsonify({
                'error': 4,
                'desc': '用户名不存在'
            })
    if not bool(password):
        return jsonify({
            'error': 3,
            'desc': '请提供密码'
        })
    conditions = {
        'password': md5(password)
    }
    if is_email(username):
        conditions['email'] = username
    elif is_phone(username):
        conditions['phone'] = username
    else:
        conditions['username'] = username
    # 查询出来取第一条信息
    login_user = User.query.filter_by(**conditions).first()
    # 判断取到的数据类型是否相同 # 不同则证明没有取到数据
    is_ok = isinstance(login_user, User)
    if is_ok:
        session['login_user'] = login_user.to_dict()
        return jsonify({
            'error': 0,
            'desc': '登录成功',
            'url': url_for('view_index')

        })
    else:
        return jsonify({
            'error': 1,
            'desc': '用户名或密码错误'
        })

@app.route('/register')
def view_register():
    return render_template('register.html')

@app.route('/ajax-register')
def ajax_register():
    # 获取前端传递的参数
    username = request.values.get('username')
    password = request.values.get('pass')
    email = request.values.get('email')
    phone = request.values.get('phone')
    # 验证前端参数
    # ***注意***：前端不可信（请求可伪造），后端必须要验证前端传递的内容（此步骤不可省略）
    if not bool(username):
        return jsonify({
            'error': 1,
            'desc': '请提供用户名'
        })
    else:
        if is_user_exists(username):
            return jsonify({
                'error': 3,
                'desc': '好名字，可惜你来晚了'
            })
    if not bool(password):
        password = '123456'
    if not bool(email):
        email = None
    if not bool(phone):
        phone = None
    # 添加到数据库
    user = User(
        username=username,
        password=md5(password),
        email=email,
        phone=phone
    )
    db.session.add(user)
    db.session.commit()
    if is_user_exists(username):
        return jsonify({
            'error': 0,
            'desc': '注册成功快去登录吧',
            'url' : url_for('view_login')
        })
    else:
        return jsonify({
            'error': 2,
            'desc': '注册失败'
        })

@app.route('/retrieve')
def view_retrieve():
    return render_template('retrieve.html')

@app.route('/ajax-retrieve')
def ajax_retrieve():
    # 获取前端传递的参数
    username = request.values.get('username')
    password = request.values.get('pass')
    # 验证前端参数
    # ***注意***：前端不可信（请求可伪造），后端必须要验证前端传递的内容（此步骤不可省略）
    if not bool(username):
        return jsonify({
            'error': 1,
            'desc': '请提供用户名'
        })
    return jsonify({
        'error': 0,
        'desc': '找回来了，去登录吧'
    })

# verify /验证/
@app.route('/ajax-verify')
def ajax_verify():
    # 获取参数
    resp_captcha = request.values.get('captcha',None)
    sess_captcha = session.get('captcha', None)
    if bool(resp_captcha):
        if bool(sess_captcha):
            if resp_captcha.upper() == sess_captcha:
                    session.pop('captcha', None);
                    return jsonify({
                        'error' : 0,
                        'desc' : '验证成功'
                    })
            else:
                return jsonify({
                    'error' : 2,
                    'desc' : '验证失败'
                })
        else:
            return jsonify({
                'error': 3,
                'desc': '验证码已失效，请重新获取'
            })
    else:
        return jsonify({
            'error' : 1,
            'desc':'请填写验证码'
        })


@app.route('/captcha')
def view_captcha():
    '''生成验证码存储于session中'''
    rand_str = random_str(4)
    bs64img = random_base64_image(rand_str)
    session['captcha'] = rand_str
    return bs64img

def is_user_exists(username):
    return User.query.filter_by(username=username).count() > 0

def db_bind_app():
    db.init_app(app)
    with app.app_context() as context:
        db.create_all()

if __name__ == '__main__':
    db_bind_app()
    app.run(
        host='127.0.0.1',
        port='5656',
        debug=True
    )
