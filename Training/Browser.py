# from selenium import webdriver 
# import time
# options=webdriver.ChromeOptions()
# options.add_experimental_option(name="detach",value=True)
# driver=webdriver.Chrome(options)

# # Lauch the website
# driver.get('https://www.flipkart.com/?affid=affveve&affExtParam1=60827&affExtParam2=5571bf8edcf9677dad90fe03bb906677')
# time.sleep(2)
# driver.close

# # maximize window
# # c_driver.maximize_window
# # time.sleep(2)

# # # go back
# # c_driver.back

# # # go forward
# # c_driver.forward

# # # to refresh
# # c_driver.refresh

# # # fullscreen window
# # c_driver.fullscreen_window

# # take screenshot
# # c_driver.save_screenshot('day10.png')
# # c_driver.save_screenshot(r'C:\Users\someshk1\OneDrive - KPIT Technologies Ltd\Pictures\Screenshots\selenium.png')

# # c_driver.close

# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.options import Options

# options = Options()
# options.add_argument("--disable-background-networking")
# options.add_argument("--disable-sync")
# options.add_argument("--disable-notifications")
# options.add_argument("--disable-default-apps")
# options.add_argument("--disable-extensions")

# driver = webdriver.Edge(options=options)

# # driver.get('https://www.flipkart.com/?affid=affveve&affExtParam1=60827&affExtParam2=5571bf8edcf9677dad90fe03bb906677')
# # driver.maximize_window
# # title=driver.title
# # print(title)
# # driver.close

# driver.get('https://www.saucedemo.com')
# time.sleep(2)

# # driver.find_element(by=id, value="user-name").send_keys('standard_user')
# driver.find_element(By.ID, "user-name").send_keys("standard_user")
# time.sleep(1)
# driver.find_element(By.ID, "password").send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element(By.ID, 'login-button').click
# time.sleep(1)


# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# # Launch Edge browser
# driver = webdriver.Edge()

# # Open a website
# driver.get('https://www.saucedemo.com')
# time.sleep(5)

# # driver.find_element(by=id, value="user-name").send_keys('standard_user')
# # driver.find_element(By.ID, "user-name").send_keys("standard_user")

# driver.find_element(By.ID, "user-name").send_keys("standard_user")
# time.sleep(1)
# driver.find_element(By.ID, "password").send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element(By.ID, 'login-button').click()
# time.sleep(1)

# # Wait for a few seconds
# time.sleep(10)


# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# # Launch Edge browser
# driver = webdriver.Edge()
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
# driver.find_element(by='class name', value='ico-resgister').click()
# time.sleep(2)
# driver.find_element(by='class name', value='ico-login').click()
# time.sleep(2)
# driver.find_element(by='class name', value='ico-cart').click()

