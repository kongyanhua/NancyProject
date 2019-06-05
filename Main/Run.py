import unittest
import HtmlTestRunner
from SampleProject.POMProject.Tests.Login import LoginTests




if __name__ == '__main__':


    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/nkong009/PycharmProjects/NancyProject/Reports'))
    # 装载测试用例
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/nkong009/PycharmProjects/NancyProject/Reports'),verbosity=2)

    suite = unittest.TestSuite()
    suite.addTest(LoginTests("test_01_ValidUserName"))
    suite.addTest(LoginTests("test_02_InvalidUserName"))
    smoke_tests = unittest.TestSuite(suite)
    result_dir = 'C:/Users/nkong009/PycharmProjects/NancyProject/Reports'
    runner = HtmlTestRunner.HTMLTestRunner(output=result_dir)
    runner.run(suite)


