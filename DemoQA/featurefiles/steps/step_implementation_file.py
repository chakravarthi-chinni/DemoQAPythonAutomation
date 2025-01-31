import time

from selenium.common import TimeoutException

from BaseFile.basefile import BaseFile
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



class DemoQAStepImplementation:

    def __init__(self,context):
        self.context=context
        self.base=context.base
        # self.base=BaseFile()

# element tab details
    def select_element_tab(self):
        self.base.implicity_wait(5)
        self.base.window_scroll(0,400)
        self.base.select_locator(value=By.XPATH,locator="//h5[text()='Elements']").click()

    def verify_element_tab(self):
        get_title=self.base.driver.title
        if get_title=='DEMOQA':
            print("Title of the web page is : ",get_title)
            assert True
        else:
            assert False

# textbox implementation methods

    def click_textbox(self):
       click_textbox= self.base.explicity_wait(5,value=By.XPATH,locator="//span[text()='Text Box']")
       click_textbox.click()

    def textbox_details(self):
        self.base.window_scroll(0,300)
        self.base.implicity_wait(4)
        first_name=self.base.select_locator(value=By.ID,locator="userName")
        first_name.send_keys("chakravarthi")
        email=self.base.select_locator(value=By.ID,locator="userEmail")
        email.send_keys("chakri@gmail.com")
        current_address=self.base.select_locator(value=By.ID,locator="currentAddress")
        current_address.send_keys("Telangana")
        permanent_address=self.base.select_locator(value=By.ID,locator="permanentAddress")
        permanent_address.send_keys("AndhraPradesh")

    def submit_textbox(self):
        self.base.window_scroll(0,500)
        submit=self.base.explicity_wait(5,value=By.ID,locator="submit")
        submit.click()

    def verify_textbox(self):
        verify_textbox=self.base.explicity_wait(10,value=By.XPATH,locator="//p[text()='chakravarthi']")
        if "chakravarthi" in verify_textbox.text.lower():
            assert True
        else:
            assert False
# checkbox stepimplementation methods

    def select_checkbox(self):
        self.base.window_scroll(0,250)
        checkbox=self.base.select_locator(value=By.XPATH,locator="//span[text()='Check Box']")
        checkbox.click()

    def choose_checkbox(self):
        self.base.implicity_wait(5)
        expand_checkboxes=self.base.select_locator(value=By.XPATH,locator="//button[@aria-label='Expand all']")
        expand_checkboxes.click()
        self.base.window_scroll(0,460)
        desktop_commands=self.base.explicity_wait(10,value=By.XPATH,locator="//label//span[.='Commands']")
        desktop_commands.click()

    def verify_checkbox(self):
        self.base.window_scroll(0,700)
        result_text=self.base.explicity_wait(10,value=By.XPATH,locator="//span[.='commands']").text.lower()
        if "commands" in result_text:
            assert True
        else:
            assert False
# Radio button step implementation methods

    def click_radio_button(self):
        self.base.window_scroll(0,460)
        self.base.explicity_wait(5,value=By.XPATH,locator="//span[.='Radio Button']").click()

    def select_radio_button(self):
        self.base.window_scroll(0,400)
        radio_button_selected=self.base.explicity_wait(5,value=By.XPATH,locator="//label[@for='yesRadio']")
        radio_button_selected.click()

    def verify_radio_button(self):
        self.base.window_scroll(0, 400)
        get_text=self.base.explicity_wait(5,value=By.XPATH,locator="//span[.='Yes']").text.lower()

        if "yes" in get_text:
            assert True
        else:
            assert False
# web tables step implementation methods

    def click_webtables(self):
        self.base.window_scroll(0,300)
        self.base.explicity_wait(10,value=By.XPATH,locator="//span[.='Web Tables']").click()

    def add_user(self):
        self.base.window_scroll(0,500)
        add_button = self.base.explicity_wait(10, value=By.ID, locator="addNewRecordButton")
        add_button.click()
        first_name=self.base.explicity_wait(10,value=By.XPATH,locator="//input[@id='firstName']")
        first_name.send_keys("chakravarthi")
        last_name=self.base.explicity_wait(10,value=By.XPATH,locator="//input[@id='lastName']")
        last_name.send_keys("chinni")
        email=self.base.explicity_wait(10,value=By.XPATH,locator="//input[@id='userEmail']")
        email.send_keys("chakri@gmail.com")
        age=self.base.explicity_wait(10,value=By.XPATH,locator="//input[@id='age']")
        age.send_keys("26")
        salary=self.base.explicity_wait(10,value=By.XPATH,locator="//input[@id='salary']")
        salary.send_keys("50000")
        department = self.base.explicity_wait(10, value=By.XPATH, locator="//input[@id='department']")
        department.send_keys("IT")
        submit=self.base.explicity_wait(10,value=By.XPATH,locator="//button[@id='submit']")
        submit.click()

    def verify_user(self):
        self.base.window_scroll(0,500)
        self.base.explicity_wait(15,value=By.XPATH,locator="//div[.='chakravarthi']").text.lower()

# button step implementation methods

    def click_button_option(self):
        self.base.window_scroll(0,325)
        clicck_button=self.base.explicity_wait(6,value=By.XPATH,locator="//span[.='Buttons']").click()

    def double_click_button(self):
        self.base.window_scroll(0,400)
        double_click=self.base.select_locator(value=By.ID,locator="doubleClickBtn")
        self.base.actions.double_click(double_click).perform()

    def verify_double_click(self):
        # self.base.window_scroll(0,500)
        double_click_message=self.base.explicity_wait(5,value=By.ID,locator="doubleClickMessage").text.lower()

        if "double" in double_click_message:
            assert True
        else:
            assert False

    def right_click(self):

        self.base.window_scroll(0, 384)
        self.base.implicity_wait(7)
        try:
            right_clicks = self.base.explicity_wait(5, value=By.XPATH, locator="//button[.='Right Click Me']")
            self.base.actions.context_click(right_clicks).release().perform()
        except TimeoutException:
            # Handle the case where the element is not found within the timeout
            print("Element 'rightClickBtn' not found")


    def verify_right_click(self):
        self.base.window_scroll(0,500)
        print("***********************************")
        right_click_message=self.base.explicity_wait(5,value=By.ID,locator="rightClickMessage").text.lower()

        if "right" in right_click_message:
            assert True
        else:
            assert  False

    def dynamic_click_button(self):
        self.base.window_scroll(0,500)
        just_click_me=self.base.explicity_wait(5,value=By.XPATH,locator="//button[.='Click Me']").click()

    def verify_dynamic_click_button(self):
        self.base.window_scroll(0,500)
        gettext_click_me=self.base.explicity_wait(5,value=By.ID,locator="dynamicClickMessage").text.lower()

        if "dynamic" in gettext_click_me:
            assert True
        else:
            assert False
# link step Implementation methods

    def click_link_option_tab(self):
        self.base.window_scroll(0,500)
        click_link_tab=self.base.explicity_wait(5,value=By.XPATH,locator="//span[.='Links']").click()

    def open_newtab_link(self):
        self.base.window_scroll(0,400)
        new_tab_link=self.base.explicity_wait(5,value=By.ID,locator="simpleLink").click()

    def verify_newtab_link(self):

        current_window=self.base.driver.current_window_handle

        handles=self.base.driver.window_handles

        for handle in handles:
            self.base.implicity_wait(5)
            if handle != current_window:
                self.base.driver.switch_to.window(handle)
                self.base.implicity_wait(10)
                # get_text=self.base.driver.title.lower()
                self.base.window_scroll(0,403.20001220703125)
                get_text=self.base.explicity_wait(5,value=By.XPATH,locator="//h5[.='Elements']").text.lower()

                if "ele" in get_text:
                    assert True
                else:
                    assert False
                self.base.driver.close()

        self.base.implicity_wait(10)
        self.base.driver.switch_to.window(current_window)

    def click_api_link(self):
        self.base.window_scroll(0,602.4000244140625)
        api_link=self.base.explicity_wait(5,value=By.XPATH,locator="//a[@id='created']").click()

    def verify_api_link(self):
        self.base.window_scroll(0,735.2000122070312)
        get_api_text=self.base.explicity_wait(5,value=By.XPATH,locator="//b[.='Created']").text.lower()

        if "created" in get_api_text:
            assert True
        else:
            assert False

# broken links step implementation methods

    def click_brokenlink_tab(self):
        self.base.window_scroll(0,500)
        broken_link_tab=self.base.explicity_wait(5,value=By.XPATH,locator="//span[.='Broken Links - Images']").click()

    def open_valid_link_tab(self):
        self.base.window_scroll(0,724)
        valid_link=self.base.explicity_wait(10,value=By.XPATH,locator="//a[.='Click Here for Valid Link']").click()

    def verify_valid_link(self):
        self.base.implicity_wait(10)
        text=self.base.driver.title.lower()
        if "demo" in text:
            assert True
        else:
            assert False
        self.base.driver.back()

    def open_broken_link(self):
        self.base.window_scroll(0,824)
        broken_link=self.base.explicity_wait(5,value=By.XPATH,locator="//a[.='Click Here for Broken Link']").click()

    def verify_broken_link(self):
        self.base.implicity_wait(10)
        text=self.base.explicity_wait(5,value=By.XPATH,locator="//h3[.='Status Codes']").text.lower()
        if "status" in text:
            assert True
        else:
            assert False







