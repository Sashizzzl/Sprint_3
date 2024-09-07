import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions



def test_registration_test_registration_with_valid_value_registration_successful_registration():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click()

    driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys("Alexandra")
    driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys("aleksandra_rusakova_10_503@gmail.com")
    driver.find_element(By.XPATH, ".//fieldset[3]//input").send_keys("404485")

    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()

    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//button[text()='Войти']")))

    driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys("aleksandra_rusakova_10_503@gmail.com")
    driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys("404485")
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
    element = driver.find_element(By.XPATH,".//button[text()='Оформить заказ']").text
    assert 'Оформить заказ' in element

    driver.quit()

def test_registration_registrate_with_invalid_password_length_message_of_fail_pops_up():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click()

    driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys("Alexandra")
    driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys("aleksandra_rusakova_10_504@gmail.com")
    driver.find_element(By.XPATH, ".//fieldset[3]//input").send_keys("404")

    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()

    element = driver.find_element(By.XPATH, ".//p[text()='Некорректный пароль']").text
    assert 'Некорректный пароль' in element

    driver.quit()

