from flask import Blueprint

hostadmin = Blueprint('hostadmin',__name__)

from apps.views.hostviews.views import *

hostadmin.add_url_rule('/host/list/', view_func=HostlistView.as_view('host_view'))
hostadmin.add_url_rule('/add/host/', view_func=HostAddView.as_view('add_host'))
hostadmin.add_url_rule('/host/del/<int:id>', view_func=HostDelView.as_view('host_del'))