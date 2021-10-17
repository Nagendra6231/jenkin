from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="C:\webdriver\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.google.com/")
time.sleep(5)
driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").send_keys("github")
driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").send_keys(Keys.ENTER)
driver.find_element_by_xpath("//img[@class='rISBZc M4dUYb']").click()
driver.save_screenshot("page2.png")
time.sleep(8)
driver.close()