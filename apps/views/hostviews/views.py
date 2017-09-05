from flask import request, render_template, redirect, url_for
from flask.views import MethodView

from index import db
from .models import Hostviews, EnvViews


class HostlistView(MethodView):
    def get(self):
        items = db.session.query(Hostviews).all()
        return render_template('host-list.html', items = items)
class HostAddView(MethodView):
    def get(self):
        envs = db.session.query(EnvViews).all()
        return render_template('add-host.html', envs = envs)
    def post(self):
        Hostname = request.form.get('Hostname')
        Netip = request.form.get('Netip')
        Wnetip = request.form.get('Wnetip')
        Cpus = request.form.get('Cpus')
        Memtotal = request.form.get('Memtotal')
        env_id = int(request.form.get('env_id'))
        Service = None
        addhost = Hostviews(Hostname, Netip, Wnetip, Cpus, Memtotal, Service, env_id)
        try:
            db.session.add(addhost)
            db.session.commit()
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close()
        return redirect(url_for('hostadmin.host_view'))

class HostDelView(MethodView):
    def get(self,id=None):
        if id:
            host = db.session.query(Hostviews).get(id)
            if host:
                db.session.delete(host)
                db.session.commit()
        return redirect(url_for('hostadmin.host_view'))

