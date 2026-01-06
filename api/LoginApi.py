import requests

from config import project_url

#
# class LoginApi:
#     @classmethod
#     def login(cls, login_data):
#         login_url=project_url + "api/user/login"
#         res = requests.post(login_url, data=login_data)
#         return res
class LoginApi:
    @classmethod
    def login(cls, login_data):
        login_url = project_url + "/api/user/login"

        res = requests.post(login_url, data=login_data)
        return res