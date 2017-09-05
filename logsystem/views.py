from flask import Blueprint,render_template,request
from hostviews.models import Hostviews,EnvViews
from index import db
from logsystem import logview
from api.saltapi import SaltApi

salt_api = "https://118.190.22.229:8088/"
username = "saltadmin"
password = "124%wer0514"

from flask.views import MethodView

class LoglistView(MethodView):
    def get(self):
        salt = SaltApi(salt_api, username, password)
        salt_clients = 'T-DOCKER-8-4.qd' #request.form.get('name')
        salt_method = 'cmd.run'
        bef_log_path = '/var/cache/salt/master/minions'
        salt_params = 'user-service'  # request.form.get('service')
        back_log_path = '/home/admin/logs/' + salt_params + '/error/'
        #logname = request.form.get('logname')

        log_path = bef_log_path + "/" + salt_clients + back_log_path
        #items = salt.salt_command(salt_clients, salt_method, 'ls' + ' ' + back_log_path)
        # for item in items.values():
        #     print(item)
        items = db.session.query(Hostviews).all()
        itams2 = db.session.query(EnvViews).all()
        return render_template('log-view.html', items = items,itams2=itams2)


# @logview.route('/logget/',methods=['POST'])
# def logget():
#     # salt = SaltApi(salt_api, username, password)
#     salt_clients = request.form.get('hostname')
#     salt_method = 'cp.push'
#     salt_params = request.form.get('service')
#     bef_log_path = '/var/cache/salt/master/minions'
#     back_log_path = '/home/admin/' + salt_params + '/logs/error/'
#     logname = request.form.get('logname')
#     log_path = bef_log_path + "/" + salt_clients + back_log_path
#     # return '{} {} {}'.format(salt_clients, log_path, logname)
