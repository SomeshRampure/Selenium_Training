from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-background-networking")
options.add_argument("--disable-sync")
options.add_argument("--disable-notifications")
options.add_argument("--disable-default-apps")
options.add_argument("--disable-extensions")

driver = webdriver.Chrome(options=options)

driver.get('https://www.flipkart.com/?affid=affveve&affExtParam1=60827&affExtParam2=5571bf8edcf9677dad90fe03bb906677')
driver.maximize_window
title=driver.title
print(title)
driver.close
