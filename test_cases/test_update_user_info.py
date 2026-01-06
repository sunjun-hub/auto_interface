import os

import allure
import pytest

from api.LoginApi import LoginApi
from api.update_user_info import Update_User_Info
from config import datas_path
from untils.assert_util import AssertUtil
from untils.read_excel import ReadExcel
from untils.str_dict import StuDict

datas = ReadExcel().read_excel(os.path.join(datas_path, 'autointerface.xlsx'),'Sheet2')
@allure.feature("更新用户信息")
@allure.story("更新用户")
class TestUpdateUserInfo:
    # def setup_class(self):
    #     data = {"username": "18742186429", "password": "123456"}
    #     res = LoginApi.login(data)
    #     self.token=res.json()['token']
    @pytest.mark.parametrize("title,data,status_code,code,msg",datas)
    def test_update_user_info(self,title,data,status_code,code,msg,login):
        result_dict = StuDict.str_to_dict(data)
        res=Update_User_Info().update_user_info(data=data,token=login)
        AssertUtil.assert_result(res,status_code,code,msg)

