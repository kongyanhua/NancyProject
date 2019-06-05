import unittest
from selenium.webdriver import Firefox
import time
import HtmlTestRunner
from SampleProject.POMProject.Pages.LoginPage import LoginPage
from SampleProject.POMProject.Pages.Homepage import Homepage
from Common.CommonMethod import read_excel

class LoginTests(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = Firefox()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_ValidUserName(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        valid_data = read_excel(r'C:\Users\nkong009\PycharmProjects\NancyProject\Data\TestExcel.xlsx',1)
        login = LoginPage(self.driver)
        home = Homepage(self.driver)
        login.enter_username(valid_data[0])
        login.enter_password(valid_data[1])
        login.click_login()
        self.driver.get_screenshot_as_file("C:\TestScreenshots\ABC.png")
        time.sleep(5)
        home.click_welcome()
        home.click_logout()

    def test_02_EmptyUserName(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        for i in range(2,6):
            invalid_data = read_excel(r'C:\Users\nkong009\PycharmProjects\NancyProject\Data\TestExcel.xlsx', i)
            login = LoginPage(self.driver)
            login.enter_username(invalid_data [0])
            login.enter_password(invalid_data [1])
            login.click_login()
            error_msg = login.check_invalid_username_msg()
            self.assertEqual(error_msg.strip(), invalid_data[2].strip())
        time.sleep(3)

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':


    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/nkong009/PycharmProjects/NancyProject/Reports'),verbosity=2)
    # 装载测试用例
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/nkong009/PycharmProjects/NancyProject/Reports'),verbosity=2)

    # suit = unittest.TestSuite()
    # suit.addTest(LoginTests("test_01_ValidUserName"))
    # suit.addTest(LoginTests("test_02_InvalidUserName"))
    # smoke_tests = unittest.TestSuite(suit)
    # result_dir = 'C:/Users/nkong009/PycharmProjects/NancyProject/Reports'
    # runner = HtmlTestRunner.HTMLTestRunner(output=result_dir)
    # runner.run(suit)


