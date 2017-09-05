from index import db

class EnvViews(db.Model):
    __tablename__ = 'envviews'
    id = db.Column(db.INTEGER,primary_key = True)
    Envname = db.Column(db.String)
    def __init__(self, id, Envname):
        self.Envname = Envname

    def __repr__(self):
        return '<环境信息：{}>'.format(self.Envname)

class Hostviews(db.Model):
    __tablename__ = 'hostviews'
    id = db.Column(db.INTEGER,primary_key = True)
    Hostname = db.Column(db.String(50))
    Netip = db.Column(db.String(50),unique=True)
    Wnetip = db.Column(db.String(50),unique=True)
    Cpus = db.Column(db.INTEGER)
    Memtotal = db.Column(db.INTEGER)
    Service = db.Column(db.String)
    env_id = db.Column(db.INTEGER, db.ForeignKey('envviews.id'))
    envviews = db.relationship('EnvViews', backref=db.backref('hostviews', lazy='dynamic'))
    def __init__(self, Hostname, Netip, Wnetip, Cpus, Memtotal, Service, env_id):
        self.Hostname = Hostname
        self.Netip = Netip
        self.Wnetip = Wnetip
        self.Cpus = Cpus
        self.Memtotal = Memtotal
        self.Service = Service
        self.env_id = env_id

    def __repr__(self):
        return '<主机信息：{} {}>'.format(self.Hostname, self.Netip)
