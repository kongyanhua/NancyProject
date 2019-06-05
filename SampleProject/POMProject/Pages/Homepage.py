from SampleProject.POMProject.Locators.Locators import Locators


class Homepage:

    def __init__(self, driver):
        self.driver = driver

    def click_welcome(self):
        self.driver.find_element_by_id(Locators.welcome_link_id).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(Locators.logout_link_text).click()




