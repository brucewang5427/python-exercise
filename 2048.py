from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser=webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')
try:
   htmlelem=browser.find_element_by_tag_name('html')
   while True:
       htmlelem.send_keys(Keys.UP)
       htmlelem.send_keys(Keys.DOWN)
       htmlelem.send_keys(Keys.LEFT)
       htmlelem.send_keys(Keys.RIGHT)
except Exception as ex:
    print(ex)