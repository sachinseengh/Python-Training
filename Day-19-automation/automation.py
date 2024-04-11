from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("http://www.google.com")

# Your automation code goes here

input_element = driver.find_element(By.CLASS_NAME, 'gLFyf')
input_element.send_keys("python tutorial")
input_element.send_keys(Keys.RETURN)

time.sleep(5)  # Adjust the sleep duration as needed

driver.close()
