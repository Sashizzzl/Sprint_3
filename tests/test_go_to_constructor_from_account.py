from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators

class TestGoToConstructorFromAccount:
    def test_go_to_constructor_from_account_click_on_button_consructor_main_page_opened(self, driver, log_in):

        driver.find_element(By.XPATH, Locators.personal_account).click()
        driver.find_element(By.XPATH, Locators.constructor).click()

        WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH, Locators.order)))
        element = driver.find_element(By.XPATH, Locators.order).text
        assert 'Оформить заказ' in element

    def test_go_to_constructor_from_account_click_on_logo_main_page_opened(self, driver, log_in):

        driver.find_element(By.XPATH, Locators.personal_account).click()
        driver.find_element(By.XPATH, Locators.logo).click()

        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, Locators.order)))
        element = driver.find_element(By.XPATH, Locators.order).text
        assert 'Оформить заказ' in element




