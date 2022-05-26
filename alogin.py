import time
from selenium import webdriver
from getpass import getpass



username = raw_input("Enter in your username: ")
print(username)
password = getpass("Enter your password: ")

driver = webdriver.Chrome("/home/user/webdriver/chromedriver_linux64/chromedriver")
driver.get("https://skoolgo.pixelmindit.com:8000/#/")

username_textbox = driver.find_element_by_id("userName")
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_id("password")
password_textbox.send_keys(password)
time.sleep(1)




from selenium.webdriver.common.keys import Keys

driver.find_element_by_name('submit').send_keys(Keys.RETURN)
time.sleep(1)





