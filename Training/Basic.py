# from selenium import webdriver
# import time
# c_driver=webdriver.Chrome()
# time.sleep(30)

from selenium import webdriver
options=webdriver.ChromeOptions()
options.add_experimental_option(name="detach",value=True)
c_driver=webdriver.Chrome(options)