from selenium.webdriver.common.by import By

from pages.basePage import BasePage


class JoinPage(BasePage):

    def getTextInTitle(self):
        title_header_element = self.driver.find_element(*JoinPageLocators.TITLE_HEADER)
        return str(title_header_element.text)


class JoinPageLocators(object):
    TITLE_HEADER = (By.XPATH, "//*[@class='setup-header setup-org']/h1")


