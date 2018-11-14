from . import views
app = views.app
# 配置session
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/test?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# SECRET(秘密) session 秘匙
app.config['SECRET_KEY'] = 'session'
def start_server():
    # 数据库创建
    views.db_bind_app()
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    app.run(
        host='0.0.0.0',
        port='5656',
        debug=True
    )
    