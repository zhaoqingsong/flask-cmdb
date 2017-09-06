class Config(object):
    DEBUG = True # 测试环境DEBUG

    # DB
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./db/fqdev_cmdb.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # SALT
    SALT_API = "https://118.190.22.229:8088/"
    SALT_USER = "saltadmin"
    SALT_PASS = "124%wer0514"

    # File Upload Settings
    UPLOAD_FOLDER = r'./uploads/'
    ALLOWED_EXTENSIONS = ['.log']