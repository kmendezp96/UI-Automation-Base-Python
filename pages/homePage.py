from selenium.webdriver.common.by import By

from pages.basePage import BasePage


class HomePage(BasePage):

    def open(self):
        self.driver.get("http://www.github.com/")

    def fill_user_info(self, name, email, password):
        user_name_input_element = self.driver.find_element(*HomePageLocators.USERNAME_INPUT_FIELD)
        user_name_input_element.send_keys(name)
        email_input_element = self.driver.find_element(*HomePageLocators.EMAIL_INPUT_FIELD)
        email_input_element.send_keys(email)
        password_input_element = self.driver.find_element(*HomePageLocators.PASSWORD_INPUT_FIELD)
        password_input_element.send_keys(password)

    def click_on_sign_up_button(self):
        sign_up_button = self.driver.find_element(*HomePageLocators.SIGN_UP_BUTTON)
        sign_up_button.click()


class HomePageLocators(object):

    USERNAME_INPUT_FIELD = (By.ID,"user[login]")
    EMAIL_INPUT_FIELD = (By.XPATH,"//input[@name='user[email]']")
    PASSWORD_INPUT_FIELD = (By.NAME,"user[password]")
    SIGN_UP_BUTTON = (By.XPATH,"//button[@type='submit']")