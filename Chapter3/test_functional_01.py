import unittest
import json
import sys
from Chapter2.flask_basic import app as _app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = _app

    def test_help(self):
        # app과 연동하기 위해 FlaskClient 인스턴스를 생성한다.
        app = self.app.test_client()

        # /api 엔드포인트를 호출한다.
        hello = app.get("/api")

        # 응답을 검사한다.
        body = json.loads(str(hello.data, 'utf8'))

        self.assertEqual(body['test'], 'test')


if __name__ == "__main__":
    unittest.main()