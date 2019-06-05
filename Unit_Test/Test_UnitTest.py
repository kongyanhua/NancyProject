# coding:utf-8


import unittest
from Util import test_get_post


class MyTestCase(unittest.TestCase):
   def test_case01(self):
        for i in range(0, 5):
            #response = requests.put('https://10.133.33.99:8090/ingestionagent/errorRetry',verify=False)
            response=test_get_post.RunMain.send_put(self,'https://10.133.33.99:8090/ingestionagent/errorRetry',None,None)
            self.assertEqual(response.status_code, 200, '返回状态错误，不是200')
            print('接口正常')
            response1=test_get_post.RunMain.send_put


if __name__ == '__main__':
        unittest.main()
