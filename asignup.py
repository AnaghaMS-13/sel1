
from selenium import webdriver
from getpass import getpass


import time
def slow_typing(element, text):
   for character in text:
      element.send_keys(character)
      time.sleep(0.3)



name		=	"Anagha"
email		=	"abc@smail.iitpkd.ac.in"
number  	=	 "9876543210"
nationality  	=	 "India"
pnumber 	=	 "3278"
gender  	=	 "Female"
weight		=	 "12"
height		=	 "34"
emergency1  	=	 "0000000000"
emergency2  	=	 "1111111111"
password	=	"qwerty123"


driver  = webdriver.Chrome("/home/user/webdriver/chromedriver_linux64/chromedriver")
driver.get("https://skoolgo.pixelmindit.com:8000/#/sign-up")







driver.maximize_window()

name_textbox = driver.find_element_by_id('fullName')
slow_typing(name_textbox, name)
time.sleep(1)

email_textbox = driver.find_element_by_id('email')
slow_typing(email_textbox, email)
time.sleep(1)

number_textbox = driver.find_element_by_id('mobile')
slow_typing(number_textbox, number)
time.sleep(1)

pnumber_textbox = driver.find_element_by_id('personalId')
slow_typing(pnumber_textbox, pnumber)
time.sleep(1)


#enter date 


nationality_textbox = driver.find_element_by_id('nationality')
slow_typing(nationality_textbox, nationality)
time.sleep(1)

height_textbox = driver.find_element_by_id('height')
slow_typing(height_textbox, height)
time.sleep(1)

weight_textbox = driver.find_element_by_id('weight')
slow_typing(weight_textbox, weight)
time.sleep(1)

gender_textbox = driver.find_element_by_id('gender')
slow_typing(gender_textbox, gender)
time.sleep(1)

emergency1_textbox = driver.find_element_by_id('emergencyNumber')
slow_typing(emergency1_textbox, emergency1)
time.sleep(1)

emergency2_textbox = driver.find_element_by_id('relationship')
slow_typing(emergency2_textbox, emergency2)
time.sleep(1)


image_textbox = driver.find_element_by_id('uploadPhoto')
image_textbox.send_keys("/home/user/automaticlogintry/image.jpeg")

password_textbox = driver.find_element_by_id('password')
slow_typing(password_textbox, password)
time.sleep(1)

confirm_textbox = driver.find_element_by_id('confirmPassword')
slow_typing(confirm_textbox, password)
time.sleep(1)

driver.find_element_by_id('Accept').submit()
time.sleep(1)
driver.find_element_by_id('create-account').click()
time.sleep(1)

