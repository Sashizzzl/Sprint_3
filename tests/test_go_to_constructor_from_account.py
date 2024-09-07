import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
def test_go_to_constructor_from_account_click_on_button_consructor_main_page_opened():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys("aleksandra_rusakova_10_502@gmail.com")
    driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys("404485")
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()

    driver.find_element(By.XPATH, ".//p[text()='Конструктор']").click()

    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
    element = driver.find_element(By.XPATH, ".//button[text()='Оформить заказ']").text
    assert 'Оформить заказ' in element

    driver.quit()

def test_go_to_constructor_from_account_click_on_logo_main_page_opened():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys("aleksandra_rusakova_10_502@gmail.com")
    driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys("404485")
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()

    driver.find_element(By.XPATH, ".//div/header/nav/div/a/*").click()

    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
    element = driver.find_element(By.XPATH, ".//button[text()='Оформить заказ']").text
    assert 'Оформить заказ' in element

    driver.quit()



