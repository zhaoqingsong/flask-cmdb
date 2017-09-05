from flask import Blueprint

logview = Blueprint('logview',__name__)

from apps.views.logsystem.views import *

logview.add_url_rule('/log/list/', view_func=LoglistView.as_view('log_view'))