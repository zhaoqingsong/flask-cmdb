import requests


class Salt():
    __headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    __session = requests.Session()

    def __init__(self, app=None):
        '''初始化对象
        :param app:
        '''
        if app:
            self.init_app(app)

    def init_app(self, app):
        '''初始化对象
        :param app:
        '''
        salt_domain = app.config.get('SALT_DOMAIN')
        salt_port = app.config.get('SALT_PORT')
        salt_is_ssl = app.config.get('SALT_IS_SSL')
        self.__salt_user = app.config.get('SALT_USER')
        self.__salt_pass = app.config.get('SALT_PASS')
        self.__salt_auth = app.config.get('SALT_AUTH')
        self.__app = app
        assert isinstance(salt_is_ssl, bool), "is_ssl should be Bool"

        if not salt_port:
            salt_port = 80

        if salt_is_ssl:
            self.__salt_url = "https://{domain}:{port}".format(domain=salt_domain, port=salt_port)
        else:
            self.__salt_url = "http://{domain}:{port}".format(domain=salt_domain, port=salt_port)

        self.__login()

    def __get(self, uri):
        '''GET方法调用,如果结果状态码为200,则直接返回json信息,否则返回报错信息
        '''
        url = "{domain}/{uri}".format(domain=self.__salt_url, uri=uri)
        resp = self.__session.get(url, headers=self.__headers)
        if resp.status_code == 200:
            return resp.json()
        return resp.text

    def __post(self, data, uri=None):
        '''POST方法调用,如果结果状态码为200,则直接返回json信息,否则返回报错信息
        '''
        if uri == None:
            url = "{domain}/".format(domain=self.__salt_url)
        else:
            url = "{domain}/{uri}".format(domain=self.__salt_url, uri=uri)
        resp = self.__session.post(url, data=data, headers=self.__headers)
        if resp.status_code == 200:
            return resp.json()
        return resp.text

    def __login(self):
        '''登录接口,初始化APP时直接调用
        :var g.salt_token：只是为了后续存储saltapi_token,可通过current_app.salt_token来获取token值（如果有需要可以的话可以将token存储值redis中）
        :var expirse：为token的过期时间,单位为秒.
        '''
        data = {
            "username": self.__salt_user,
            "password": self.__salt_pass,
            "eauth": self.__salt_auth
        }
        uri = 'login'
        resp = self.__post(uri, data)
        if not isinstance(resp, str):
            return resp
        data = resp['return'][0]
        token = data['token']
        expirse = int(data['expire'] - data['start'])
        self.__app.g.salt_token = token
        self.__headers['X-Auth-Token'] = token

        return True

    def minions(self, mid=None):
        return self.__get('/minions/{mid}'.format(mid=mid))

    def run(self, method, tgt, module,args):
        '''

        :param method:  执行模块的方法可访问saltapi的地址来获取
        :param tgt: 一台minion或者一组minions
        :param module: 执行的模块
        :param args: 模块的可选参数例如cmd.run 模块的参数为ls
        :return:
        '''
        data = [{'client': method, 'tgt': tgt, 'fun': module, 'arg': args, 'expr_form': 'list'}]
        return self.__post(data=data)
