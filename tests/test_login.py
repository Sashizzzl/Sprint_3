from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from config import url
from data import Data

class TestLogin:
    def test_login_on_the_main_page_clicking_on_button_login_login_completed(self, driver):
        driver.get(url)

        driver.find_element(By.XPATH, Locators.log_in).click()
        driver.find_element(By.XPATH, Locators.emeil_log_in).send_keys(Data.email)
        driver.find_element(By.XPATH, Locators.password_log_in).send_keys(Data.password)
        driver.find_element(By.XPATH, Locators.log_in_button).click()

        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, Locators.order)))

        element = driver.find_element(By.XPATH,Locators.order).text
        assert 'Оформить заказ' in element

    def test_login_on_the_main_page_clicking_on_button_personal_cabinet_login_completed(self, driver):

        driver.get(url)

        driver.find_element(By.XPATH, Locators.personal_account).click()
        driver.find_element(By.XPATH, Locators.emeil_log_in).send_keys(Data.email)
        driver.find_element(By.XPATH, Locators.password_log_in).send_keys(Data.password)
        driver.find_element(By.XPATH, Locators.log_in_button).click()

        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, Locators.order)))
        element = driver.find_element(By.XPATH, Locators.order).text
        assert 'Оформить заказ' in element

    def test_login_on_the_main_page_clicking_on_button_login_in_registration_form_login_completed(self, driver):
        driver.get(url)

        driver.find_element(By.XPATH, Locators.personal_account).click()
        driver.find_element(By.XPATH, Locators.sign_up).click()
        driver.find_element(By.XPATH, Locators.log_in_sign_up).click()

        driver.find_element(By.XPATH, Locators.emeil_log_in).send_keys(Data.email)
        driver.find_element(By.XPATH, Locators.password_log_in).send_keys(Data.password)
        driver.find_element(By.XPATH, Locators.log_in_button).click()

        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, Locators.order)))
        element = driver.find_element(By.XPATH, Locators.order).text
        assert 'Оформить заказ' in element

    def test_login_on_the_main_page_clicking_on_button_login_in_restore_password_form_login_completed(self, driver):
        driver.get(url)

        driver.find_element(By.XPATH, Locators.personal_account).click()
        driver.find_element(By.XPATH, Locators.sign_up).click()
        driver.find_element(By.XPATH, Locators.log_in_restore_password).click()

        driver.find_element(By.XPATH, Locators.emeil_log_in).send_keys(Data.email)
        driver.find_element(By.XPATH, Locators.password_log_in).send_keys(Data.password)
        driver.find_element(By.XPATH, Locators.log_in_button).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, Locators.order)))
        element = driver.find_element(By.XPATH, Locators.order).text
        assert 'Оформить заказ' in element


