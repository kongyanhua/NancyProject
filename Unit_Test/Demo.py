# coding:utf-8
"""
基本的自动化测试脚本 basic_demo.py
"""
__author__ = 'nancy'
import unittest


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        print('init by setUp...')

    def tearDown(self):
        print('end by tearDown...')

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
       #self.assertTrue('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
    # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
        #unittest.main()
# unittest.main()
# 装载测试用例
    test_cases = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    # 使用测试套件并打包测试用例
    test_suit = unittest.TestSuite()
    test_suit.addTests(test_cases)
    # 运行测试套件，并返回测试结果
    test_result = unittest.TextTestRunner(verbosity=2).run(test_suit)
    #生成测试报告
    print("testsRun:%s" % test_result.testsRun)
    print("failures:%s" % len(test_result.failures))
    print("errors:%s" % len(test_result.errors))
    print("skipped:%s" % len(test_result.skipped))
