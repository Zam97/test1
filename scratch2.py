from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
URL = 'https://www.saucedemo.com/'
LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'
def get_driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver


def open_page(driver, url):
    driver.get(url)


def get_element_by_id(xpath, driver):
    element = driver.find_element(By.ID, xpath)
    return element

def element_click(xpath, driver):
    element = get_element_by_id(xpath=xpath, driver=driver)
    element.click()

def element_send_keys(xpath, driver, text):
    element = get_element_by_id(xpath=xpath, driver=driver)
    element.clear()
    element.send_keys(text)

# 1
driver = get_driver()
open_page(driver, URL)
element_click(xpath='login-link', driver=driver)
element_send_keys(xpath="user-name", driver=driver, text=LOGIN)
element_send_keys(xpath="password", driver=driver, text=PASSWORD)
element_click(xpath='login-button', driver=driver)