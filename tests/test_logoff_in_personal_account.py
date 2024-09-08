import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
def test_go_to_personal_account_click_on_button_account_appeared_page_of_account():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys("aleksandra_rusakova_10_502@gmail.com")
    driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys("404485")
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH, ".//p[text()='Личный Кабинет']")))
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()

    WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Выход']")))
    driver.find_element(By.XPATH, ".//button[text()='Выход']").click()

    element = driver.find_element(By.XPATH, ".//button[text()='Выход']").text
    assert 'Выход' in element

    driver.quit()


