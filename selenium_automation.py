from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
#
browser=webdriver.Chrome('chromedriver_win32\\chromedriver.exe')
browser.maximize_window()
browser.get("https://youtu.be/VRJ1qPTApzE")
#time.sleep(10)
# input=browser.find_element_by_name('q')
# input.send_keys('Python Learning')
# input.click()
# button=browser.find_element_by_name('btnK')
# button.click()
# opr=browser.find_element_by_id('btn-hamburger')
# opr.click()
# sr=browser.find_element_by_link_text('data-csa-c-slot-id="nav_cs_1"')
# sr.click()
#browser.find_element_by_xpath('//*[@id="nav-xshop"]/a[2]').click()

# browser.find_element_by_name('identifier').send_keys('pythonweekday22@gmail.com')
wait=WebDriverWait(browser,10)
wait.until()
browser.find_element_by_class_name("ytp-large-play-button ytp-button").click()
# browser.find_element_by_id('password').send_keys('password')
# browser.find_element_by_class_name("VfPpkd-RLmnJb").click()
