# from selenium import webdriver
# import time
# c_driver=webdriver.Chrome()
# time.sleep(30)

# from selenium import webdriver
# options=webdriver.ChromeOptions()
# options.add_experimental_option(name="detach",value=True)
# c_driver=webdriver.Chrome(options)

from selenium import webdriver 
import time
options=webdriver.ChromeOptions()
options.add_experimental_option(name="detach",value=True)
driver=webdriver.Chrome(options)

# Lauch the website
driver.get('https://www.flipkart.com/?affid=affveve&affExtParam1=60827&affExtParam2=5571bf8edcf9677dad90fe03bb906677')
time.sleep(2)