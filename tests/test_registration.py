from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
import random
from config import url

class TestRegistration:
    def test_registration_test_registration_with_valid_value_registration_successful_registration(self, driver):
        driver.get(url)

        driver.find_element(By.XPATH, Locators.personal_account).click()
        driver.find_element(By.XPATH, Locators.sign_up).click()

        driver.find_element(By.XPATH, Locators.name).send_keys("Alexandra")
        new_email = f'aleksandra_rusakova_10_{random.randint(100,999)}@gmail.com'
        driver.find_element(By.XPATH, Locators.email_sign_up).send_keys(new_email)
        driver.find_element(By.XPATH, Locators.password_sign_up).send_keys("404485")
        driver.find_element(By.XPATH, Locators.sign_up_button).click()

        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, Locators.log_in_button)))

        driver.find_element(By.XPATH, Locators.emeil_log_in).send_keys(new_email)
        driver.find_element(By.XPATH, Locators.password_log_in).send_keys("404485")
        driver.find_element(By.XPATH, Locators.log_in_button).click()

        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, Locators.order)))
        element = driver.find_element(By.XPATH,Locators.order).text
        assert 'Оформить заказ' in element

    def test_registration_registrate_with_invalid_password_length_message_of_fail_pops_up(self, driver):
        driver.get(url)

        driver.find_element(By.XPATH, Locators.personal_account).click()
        driver.find_element(By.XPATH, Locators.sign_up).click()

        driver.find_element(By.XPATH, Locators.name).send_keys("Alexandra")
        new_email = f'aleksandra_rusakova_10_{random.randint(100,999)}@gmail.com'
        driver.find_element(By.XPATH, Locators.email_sign_up).send_keys(new_email)
        driver.find_element(By.XPATH, Locators.password_sign_up).send_keys("404")

        driver.find_element(By.XPATH, Locators.sign_up_button).click()

        element = driver.find_element(By.XPATH, Locators.sign_up_fail).text
        assert 'Некорректный пароль' in element

