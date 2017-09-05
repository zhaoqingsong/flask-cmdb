#!/usr/bin/env python
# _*_ coding:utf-8 _*_


# TODO: SaltApi 做为工具类使用




__author__ = 'jason'

salt_api = "https://118.190.22.229:8088/"
username = "saltadmin"
password = "124%wer0514"

import requests
import json
try:
    import cookielib
except:
    import http.cookiejar as cookielib

# 使用urllib2请求https出错，做的设置
import ssl
context = ssl._create_unverified_context()

# 使用requests请求https出现警告，做的设置
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class SaltApi:
    """
    定义salt api接口的类
    初始化获得token
    """
    def __init__(self, url, username, password):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
            "Content-type": "application/json"
            # "Content-type": "application/x-yaml"
        }
        self.url = url
        self.username = username
        self.password = password
        self.login_url = url + "login"
        self.params = {'client': 'local', 'fun': '', 'tgt': ''}
        # self.params = {'client': 'local', 'fun': '', 'tgt': '', 'arg': ''}
        self.login_params = {'username': self.username, 'password': self.password, 'eauth': 'pam'}
        self.token = self.get_data(self.login_url, self.login_params)['token']
        self.headers['X-Auth-Token'] = self.token

    def get_data(self, url, params):
        send_data = json.dumps(params)
        request = requests.post(url, data=send_data, headers=self.headers, verify=False)
        # response = request.text
        # response = eval(response)     使用x-yaml格式时使用这个命令把回应的内容转换成字典
        # print response
        print(request)
        # print type(request)
        response = request.json()
        result = dict(response)
        print(result)
        return result['return'][0]

    def salt_command(self, tgt, method, arg=None):
        """远程执行命令，相当于salt 'client1' cmd.run 'free -m'"""
        if arg:
            params = {'client': 'local', 'fun': method, 'tgt': tgt, 'arg': arg}
        else:
            params = {'client': 'local', 'fun': method, 'tgt': tgt}
        print('命令参数: ', params)
        result = self.get_data(self.url, params)
        return result
