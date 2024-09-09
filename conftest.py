import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import Locators
from data import Data
from config import url

def browser_settings ():
    chrome_options = webdriver.ChromeOptions()
    return chrome_options

@pytest.fixture
def driver():
    chrome = webdriver.Chrome(options=browser_settings())
    chrome.maximize_window()
    yield chrome
    chrome.quit()

@pytest.fixture
def log_in (driver):
    driver.get(url)

    driver.find_element(By.XPATH, Locators.personal_account).click()
    driver.find_element(By.XPATH, Locators.emeil_log_in).send_keys(Data.email)
    driver.find_element(By.XPATH, Locators.password_log_in).send_keys(Data.password)
    driver.find_element(By.XPATH, Locators.log_in_button).click()

    yield driver