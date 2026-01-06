import os

import requests

from config import project_url



class Update_User_Info:
    @classmethod
    def update_user_info(cls, token, data):
        url = project_url + "/api/user/user_change"
        header = {"token":token}
        res = requests.post(url=url,data=data,headers=header)
        return res