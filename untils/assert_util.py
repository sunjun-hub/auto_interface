class AssertUtil:
    @staticmethod
    def assert_result(res,status_code,code,msg):
        if status_code is not None:
            assert res.status_code == status_code
        if code is not None:
            assert res.json()['code'] == code
        if msg is not None:
            assert msg in res.json()['msg']