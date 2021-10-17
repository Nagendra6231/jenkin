import webbrowser

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import pytest
class Testfacebook():
    @pytest.yield_fixture()
    def test_setup(self):
        global driver
        option1 = Options()
        option1.add_argument("--disable-notifications")
        driver = webdriver.Chrome(executable_path="C:/webdriver/chromedriver_win32/chromedriver.exe",chrome_options=option1)
        driver.implicitly_wait(5)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("test passed successfully")
    def test_fb_login(self,test_setup):

        driver.get("https://www.facebook.com/")

        driver.find_element_by_name("email").send_keys("gampanagendra6231@gmail.com")
        driver.find_element_by_name("pass").send_keys("gampasubbaraju")
        driver.find_element_by_name("login").click()
        time.sleep(10)

        x = driver.title
        print(x)
        #assert x == "Facebook – log in or sign up"

