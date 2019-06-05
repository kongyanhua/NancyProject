from SampleProject.POMProject.Locators.Locators import Locators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element_by_id(Locators.username_textbox_id).clear()
        self.driver.find_element_by_id(Locators.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(Locators.password_textbox_id).clear()
        self.driver.find_element_by_id(Locators.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(Locators.login_button).click()

    def check_invalid_username_msg(self):
        msg = self.driver.find_element_by_xpath(Locators.invalid_username_msg_xpath).text
        return msg









