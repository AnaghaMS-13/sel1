
from selenium import webdriver





driver = webdriver.Chrome("/home/user/webdriver/chromedriver_linux64/chromedriver")
driver.get("https://skoolgo.pixelmindit.com:8000/#/")


m = driver.find_element_by_xpath("//span[@class='ml-1 mr-4 text-muted']")








