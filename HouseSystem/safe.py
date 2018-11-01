# -*- coding:utf-8 -*-
'''
    账户安全
    tools 工具
    wraps 外衣 (方法装饰器)
    current 当前
'''
from functools import wraps


from flask import (
    g,          # global
    session,    
    request,
    redirect,
    url_for,
    current_app,
    abort
)

def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        # 判断login_user有没有在g中
        # hasattr(g, 'login_user') 存在返回True 再前面加上not 取反
        # or 用法 如果左边为True 那么右边就不会执行, 
        not_in_g = not hasattr(g, 'login_user') or g.login_user is None
        # login_user 不存在session中
        not_in_s = 'login_user' not in session or session['login_user'] is None
        # import pdb;pdb.set_trace()
        if not_in_g and not_in_s: # 若过两边都为True
            # 给他赋值一个路由
            _route = 'view_login'
            # 跳转
            # import pdb;pdb.set_trace()
            return redirect(url_for(_route, next=request.url))
        if not_in_g: # 如果 login_user 不存在全局中 但是session中存在的话
            # 设置到g中
            g.login_user = session['login_user']
        return func(*args,**kwargs)
    return decorated_function



    