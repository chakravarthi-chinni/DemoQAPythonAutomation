from BaseFile.basefile import BaseFile
from featurefiles.steps.step_implementation_file import DemoQAStepImplementation
from behave import *
import logging

# class DemoQAStepDefination:
#     # logger = logging.getLogger(__name__)
#     # logging.basicConfig(level=logging.INFO)
#     # def __init__(self,context):
#     #     self.step_impl = DemoQAStepImplementation(context)
#     def __init__(self):
#         self.impl=DemoQAStepImplementation()


# element tab in web page
@given(u'click element tab')
def select_element(context):
    select = DemoQAStepImplementation(context)
    # context.base.select_element_tab()
    select.select_element_tab()
    print("it ia  select element method!!!!!!!")


@then(u'verify the element tab')
def verify_element(context):
    verify = DemoQAStepImplementation(context)
    verify.verify_element_tab()


# textbox step defination methods
@given(u'select the textbox')
def select_textbox(context):
    selct = DemoQAStepImplementation(context)
    selct.click_textbox()


@when(u'enter the textbox fields')
def enter_textbox_fields(context):
    details = DemoQAStepImplementation(context)
    details.textbox_details()


@when(u'submit the textbox')
def submit_textbox(context):
    submit = DemoQAStepImplementation(context)
    submit.submit_textbox()


@then(u'verify the textbox')
def verify_textbox(context):
    verify = DemoQAStepImplementation(context)
    verify.verify_textbox()


# checkbox stepdefination methods

@given(u'select the checkbox')
def select_checkbox(context):
    select = DemoQAStepImplementation(context)
    select.select_checkbox()


@when(u'choose the checkboxes')
def choose_checkboxes(context):
    choose = DemoQAStepImplementation(context)
    choose.choose_checkbox()


@then(u'verify the checkboxes')
def verify_checkboxes(context):
    verify = DemoQAStepImplementation(context)
    verify.verify_checkbox()


# Radio buttons stepdefination methods
@given(u'click the radio button option')
def click_radio_button(context):
    click = DemoQAStepImplementation(context)
    click.click_radio_button()


@when(u'select the radio button')
def choose_radio_button(context):
    choose = DemoQAStepImplementation(context)
    choose.select_radio_button()


@then(u'verify the radio button')
def verify_radio_button(context):
    verify = DemoQAStepImplementation(context)
    verify.verify_radio_button()


# web tables stepdefination methods

@given(u'click the webtables option')
def click_webtables(context):
    click = DemoQAStepImplementation(context)
    click.click_webtables()


@when(u'add user details in webtable')
def add_user(context):
    add_user = DemoQAStepImplementation(context)
    add_user.add_user()


@then(u'verify user details added or not')
def verify_user(context):
    verify = DemoQAStepImplementation(context)
    verify.verify_user()


# button stepdefination methods
@given(u'click the button option')
def click_button(context):
    click = DemoQAStepImplementation(context)
    click.click_button_option()


@when(u'double click the button')
def check_double_click(context):
    double_click = DemoQAStepImplementation(context)
    double_click.double_click_button()


@then(u'verify the button is double clicked or not')
def verify_double_click(context):
    verify_double_click = DemoQAStepImplementation(context)
    verify_double_click.verify_double_click()


@when(u'right click the button')
def right_click_button(context):
    right_click = DemoQAStepImplementation(context)
    right_click.right_click()


@then(u'verify the right click button')
def verify_right_click(context):
    verify_right_click = DemoQAStepImplementation(context)
    verify_right_click.verify_right_click()


@when(u'clik the button')
def click_me_button(context):
    click_me_button = DemoQAStepImplementation(context)
    click_me_button.dynamic_click_button()


@then(u'verify the click button')
def step_impl(context):
    verify_dynamic_button = DemoQAStepImplementation(context)
    verify_dynamic_button.verify_dynamic_click_button()


# link step defination methods

@given(u'click the link option')
def click_link_option(context):
    link = DemoQAStepImplementation(context)
    link.click_link_option_tab()


@when(u'click the link that direct to new tab')
def click_link_new_tab(context):
    click_new_link = DemoQAStepImplementation(context)
    click_new_link.open_newtab_link()


@then(u'verify the page are open or not')
def verify_new_tab_link(context):
    verify_new_link_tab = DemoQAStepImplementation(context)
    verify_new_link_tab.verify_newtab_link()


@when(u'open the api call links')
def click_api_link(context):
    click_api_link = DemoQAStepImplementation(context)
    click_api_link.click_api_link()


@then(u'verify api links')
def verify_api_link(context):
    verify_apilink = DemoQAStepImplementation(context)
    verify_apilink.verify_api_link()


# broken link step defination methods

@given(u'click the broken link tab')
def click_broken_link(context):
    click = DemoQAStepImplementation(context)
    click.click_brokenlink_tab()


@when(u'open the valid link')
def click_valid_link(context):
    valid_link = DemoQAStepImplementation(context)
    valid_link.open_valid_link_tab()


@then(u'verify the vallid link')
def verify_valid_link(context):
    verify_valid_link = DemoQAStepImplementation(context)
    verify_valid_link.verify_valid_link()


@given(u'open the broken link')
def click_broken_link(context):
    broken_link = DemoQAStepImplementation(context)
    broken_link.open_broken_link()


@then(u'verify the broken link')
def verify_broken_link(context):
    verify_broken_link = DemoQAStepImplementation(context)
    verify_broken_link.verify_broken_link()


# clario stepdefination files

@given(u'open the url')
def open_support_tab(context):
    context.impl.open_the_clario()


@when(u'click on the support button')
def click_call_tab(context):
    context.impl.click_call_us()


@then(u'cpature the text')
def verify_call_tab(context):
    context.impl.verify_call_us()
