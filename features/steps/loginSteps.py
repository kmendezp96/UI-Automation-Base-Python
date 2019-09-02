from behave import *

from pages.homePage import HomePage
from pages.joinPage import JoinPage


@given('the user is on the github page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.open()


@when('the user fills the sign up form with')
def step_impl(context):
    context.home_page.fill_user_info(context.table[0]['Username'],
                                     context.table[0]['Email'],
                                     context.table[0]['Password'])


@when('the user clicks on sign up button')
def step_impl(context):
    context.home_page.click_on_sign_up_button()


@then('the user should be on the join page')
def step_impl(context):
    context.join_page = JoinPage(context.driver)
    assert context.join_page.getTextInTitle().__contains__("Join GitHub"),\
        f'The expected is: Join GitHub, the obtained is {context.join_page.getTextInTitle()}'
