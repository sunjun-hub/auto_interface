
import os

import allure
import pytest
import requests
from api.LoginApi import LoginApi
from config import datas_path
from untils.read_excel import ReadExcel
from untils.str_dict import StuDict
datas = ReadExcel().read_excel(os.path.join(datas_path, 'autointerface.xlsx'),'Sheet1')
print(datas)
@allure.feature("登录模块")
@allure.story("登录成功")
class TestLogin:
    @pytest.mark.parametrize("title,login_data,status_code,code,msg", datas)
    @allure.title("{title}")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_success(self,title,login_data,status_code,code,msg,get_logger):
        get_logger.info(f"开始执行用例：{title}")
        with allure.step("登录成功"):
            result_dict = StuDict.str_to_dict(login_data)
            res = LoginApi.login(result_dict)
            print(res.json())
        with allure.step("断言结果"):
            assert res.status_code == status_code
            assert res.json()['code'] == code
            assert msg in res.json()['msg']


    # def test_login_none_username_fail(self):
    #     login_data = {
    #         "username": "",
    #         "password": "123456"
    #     }
    #     res = LoginApi.login(login_data)
    #     print(res.json())
    #
    # def test_login_none_password_fail(self):
    #     login_data = {
    #         "username": "18742186429",
    #         "password": ""
    #     }
    #     res = LoginApi.login(login_data)
    #     print(res.json())
    #
    # def test_login_none_wrong_password_username_fail(self):
    #     login_data = {
    #         "username": "18742186429",
    #         "password": "123455"
    #     }
    #     res = LoginApi.login(login_data)
    #     print(res.json())
