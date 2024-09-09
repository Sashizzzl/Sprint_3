from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators

class TestGoToPersonalAccount:
    def test_go_to_personal_account_click_on_button_account_appeared_page_of_account(self, driver, log_in):

        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, Locators.personal_account)))
        driver.find_element(By.XPATH, Locators.personal_account).click()

        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, Locators.personal_info_chandge)))
        element = driver.find_element(By.XPATH, Locators.personal_info_chandge).text
        assert 'В этом разделе вы можете изменить свои персональные данные' in element




