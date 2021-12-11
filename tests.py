import time

from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class HostTest(LiveServerTestCase):

    def test_home_page(self):

        options = Options()
        options.headless = True

        driver = webdriver.Chrome('./chromedriver', chrome_options=options)
        # driver = webdriver.Chrome()
        # try driver = webdriver.Chrome('./chromedriver') with the driver in the project folder if you can't set to path

        driver.get("http://127.0.0.1:8000/")
        # try driver.get(self.live_server_url) if driver.get('http://127.0.0.1:8000/') does not work
        time.sleep(5)
        assert "Hello, world!" in driver.title


# class LoginFormTest(LiveServerTestCase):
#     def test_form(self):
#         driver = webdriver.Chrome()
#         driver.get("http://127.0.0.1:8000/accounts/login/")
#         time.sleep(3)
#         user_name = driver.find_element(By.NAME, 'username')
#         user_password = driver.find_element(By.NAME, 'password')
#         time.sleep(3)
#         submit_btn = driver.find_element(By.ID, 'submit')
#         user_name.send_keys('admin')
#         user_password.send_keys('admin')
#         time.sleep(3)
#         submit_btn.send_keys(Keys.RETURN)
#         assert 'admin' in driver.page_source

        """
        find_element_by_id
        find_element_by_name
        find_element_by_xpath
        find_element_by_link_text
        find_element_by_partial_link_text
        find_element_by_tag_name
        find_element_by_class_name
        find_element_by_css_selector
        """
