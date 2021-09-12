from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 600)
driver.get("https://web.whatsapp.com")
target = '"Prateek"'
string = "hi"
x_arg = '//span[contains(@title, '+ target + ')]'
target=wait.until(presence_of_element_located((By.XPATH, x_arg)))
target.click()
sleep(5)
input_box = driver.find_element_by_class_name('_13mgZ')
# input_box.click()
for i in range(2):
    input_box.send_keys(string+Keys.ENTER)