from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
URL = 'https://www.saucedemo.com/'
LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'
#1
driver.get(URL)
#2
login_page_button = driver.find_element(By.ID, "login-button")
login_page_button.click()
pass
#3
input_login = driver.find_element(By.ID, "user-name")
input_password = driver.find_element(By.ID, "password")
input_login.send_keys(LOGIN)
input_password.send_keys(PASSWORD)
register_button = driver.find_element(By.ID, "login-button")
register_button.click()
pass