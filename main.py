from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'https://accounts.google.com/v3/signin/identifier?dsh=S-2129886921%3A1679515066994624&continue=https%3A%2F%2Fclassroom.google.com&ifkv=AWnogHesaZZ6G_DVemhbuzYBrd5vZx5-2YPa9RsF5AC9oNeV8_2KHVrQ9rDoR2lzCDnhXcSaQGmC6g&passive=true&flowName=GlifWebSignIn&flowEntry=ServiceLogin'

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(
    executable_path='сhromedriver')

try:
        driver.get(url)
        login = driver.find_element(By.ID, 'identifierId')
        login.clear()
        login.send_keys('your email')
        login.send_keys(Keys.ENTER)
        time.sleep(5)
        password = driver.find_element(By.NAME, 'Passwd')
        password.send_keys('your password')
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        input('ENTER which exit')

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()

