import pytest

from api.LoginApi import LoginApi
from untils.log_util import LogUtil


@pytest.fixture(scope="function")
def login():
    data = {"username": "18742186429", "password": "123456"}
    res = LoginApi.login(data)
    token = res.json()['token']
    yield token

@pytest.fixture(scope="class")
def get_logger():
    logger = LogUtil.get_logger()
    yield logger