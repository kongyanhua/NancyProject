import unittest, time, traceback
from selenium.webdriver import Firefox


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver= Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://strzw058051/SMARTSolutions/')

    def tearDown(self):

        self.driver.find_element_by_xpath("//div[@id='divModuleActionTiles']//div[@class='btn-group pull-right preferenceContainer']").click()
        self.driver.find_element_by_id('aLogoff').click()
        self.driver.close()

    def test_001(self):
        self.driver.find_element_by_id('txtLoginid').send_keys('Admin')
        self.driver.find_element_by_id('txtPassword').send_keys('Admin')
        self.driver.find_element_by_id('btnloginText').click()
        time.sleep(30)




if __name__ == '__main__':
    unittest.main()
