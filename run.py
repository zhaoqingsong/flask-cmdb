# -*- coding:utf-8 -*-
# TODO： 建议待完成SaltApi 工具类后再进行下一步开发

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from apps.api.saltapi import SaltApi

# UPLOAD_FOLDER = r'./uploads/'
# ALLOWED_EXTENSIONS = ['.log']

app = Flask(__name__, static_url_path='')
# app.debug = True
# app.config['SQLALCHEMY_DATABASE_URI'] =
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)  # 创建数据库核心对象


# db.init_app(app)     #初始化绑定app

# 检查文件是否允许上传
def allowed_file(filename):
    _, ext = os.path.splitext(filename)  # splitext可以实现文件名和后缀分离，_表示忽略名字
    return ext.lower() in ALLOWED_EXTENSIONS


@app.route('/db_sync/')
# TODO： 根据功能来进行划分
def host_sync():
    salt = SaltApi(salt_api, username, password)
    salt_clients = '*'
    salt_method = 'grains.items'
    items = salt.salt_command(salt_clients, salt_method)

    for (key, value) in items.items():
        Hostname = value['fqdn']
        Netip = value['ip_interfaces']['eth0'][0]
        Wnetip = value['ip_interfaces']['eth0'][0]
        Cpus = value['num_cpus']
        Memtotal = value['mem_total']
        sql = Hostviews(Hostname, Netip, Wnetip, Cpus, Memtotal, Service=None)
        db.session.add(sql)
    db.session.commit()
    return '同步完成'


# @app.route('/viewlog/')
# def viewlog():

# @app.route('/post_viewlog/', methods=['POST'])
# def post_viewslog():
#     salt = SaltApi(salt_api, username, password)
#     salt_clients = '*'
#     salt_method = 'cp.push'
#     salt_params = request.form.get('Hostname')
#     items = salt.salt_command(salt_clients, salt_method, salt_params)

# def object_as_dict(obj):
#     return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}
#
# @app.route('/hostlist/')
# def listviews():
#     items = db.session.query(Hostviews).all()
#     return render_template('host-list.html', items = items)
# return render_template('host-list.html', items = items)
# return render_template('host-list.html', items = items)
# clients = items.keys()
# Master = items[salt_client]['master']
# Hostname = items[salt_client]['fqdn']
# Net_ip = items[salt_client]['ip_interfaces']['eth0'][0]
# Wnet_ip = items[salt_client]['ip_interfaces']['eth1'][0]
# Num_cpus = items[salt_client]['num_cpus']
# return 'master:{}, 主机名:{}, 内网IP:{}, 外网IP:{}, CPU数{}'.format(Master,Hostname,Net_ip,Wnet_ip,Num_cpus,)
# return render_template('host-list.html', items = items)
# return ''

# def main():
#
#     print('==================')
#     print('同步执行命令')
#     salt = SaltApi(salt_api,username,password)
#     print(salt.token)
#     salt_client = 'T-DOCKER-8*'
#     #salt_test = 'test.ping'
#     #salt_method = 'cmd.run'
#     # salt_method = 'grains.get'
#     salt_method = 'grains.items'
#     net_ip = "ip a | grep eth0 | grep inet | awk '{print $2}'"
#     wnet_ip = "ip a | grep eth0 | grep inet | awk '{print $2}'"
#     # salt_params = 'ip_interfaces:eth0'
#
#     # print salt.salt_command(salt_client, salt_method, salt_params)
#     # 下面只是为了打印结果好看点
#     result1 = salt.salt_command(salt_client, salt_method)
#     for i in result1.keys():
#         return result1[i]
# result2 = salt.salt_command(salt_client, salt_method, salt_params)
# for i in result2.keys():
#     print(i)
#     print(result2[i])
# @app.route('/hostlist/')
# def host_list():
#     items = db.session.query(Hostviews)
#     return render_template('host-list.html', items = items)
@app.route('/')
def base():
    return render_template('index.html')


# 倒入主机列表视图
from apps.views.hostviews.views import hostadmin

app.register_blueprint(hostadmin)

# 倒入日志查看模版
from apps.views.logsystem.views import logview

app.register_blueprint(logview)

if __name__ == '__main__':
    app.run()
