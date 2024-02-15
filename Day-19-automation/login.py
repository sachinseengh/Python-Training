from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time





# driver = webdriver.Chrome()


# to hide the button click shown while filling form
chrome_option=webdriver.ChromeOptions()

chrome_option.add_argument('--headless')

driver = webdriver.Chrome(options=chrome_option)

driver.get("http://the-internet.herokuapp.com/login")





input_username = driver.find_element(By.ID,'username')
input_username.send_keys("tomsmith")


input_password = driver.find_element(By.ID,'password')
input_password.send_keys("SuperSecretPassword!")


input_submit = driver.find_element(By.CLASS_NAME,'radius')
input_submit.send_keys(Keys.RETURN)



message_element = driver.find_element(By.CLASS_NAME,'subheader')
print(message_element.text)

time.sleep(122)  # Adjust the sleep duration as needed

driver.close()
