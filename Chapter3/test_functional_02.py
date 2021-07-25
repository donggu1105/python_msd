import unittest
import json
from Chapter2.flask_error import app as _app
import sys
_404 = "The requested URL was not found on the server. "\
 " If you entered the URL manually please check your "\
 "spelling and try again."

class TestApp(unittest.TestCase):
    def setUp(self):
        # app과 연동하기 위해 FlaskClient 인스턴스를 생성한다.
        self.app = _app.test_client()


    def test_raise(self):
        hello = self.app.get("/api")
        if (sys.version_info > (3, 0)):
            body = json.loads(str(hello.data, 'utf8'))
        else:
            body = json.loads(str(hello.data).encode('utf8'))

        self.assertEqual(body['code'], 500)


    def test_proper_404(self):

        hello = self.app.get("/asdfsdf")
        if (sys.version_info > (3, 0)):
            body = json.loads(str(hello.data, 'utf8'))
        else:
            body = json.loads(str(hello.data).encode("utf8"))

        self.assertEqual(body['code'], 404)
        self.assertEqual(body['message'], '404 Not Found')
        self.assertEqual(body['description'], _404)



if __name__ == "__main__":
    unittest.main()
