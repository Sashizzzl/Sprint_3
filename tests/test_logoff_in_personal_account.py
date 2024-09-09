from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators

class TestLogoff:
    def test_click_log_off_account_signed_out(self, driver, log_in):

        WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH, Locators.personal_account)))
        driver.find_element(By.XPATH, Locators.personal_account).click()

        WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH, Locators.log_off)))
        driver.find_element(By.XPATH, Locators.log_off).click()

        element = driver.find_element(By.XPATH, Locators.log_off).text
        assert 'Выход' in element


