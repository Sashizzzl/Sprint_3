from selenium.webdriver.common.by import By
from locators import Locators
from config import url

class TestElementsOfConstructor:
    def test_tarnsfer_to_sauces_in_constructor_click_on_sauce_souce_active(self, driver):
        driver.get(url)

        driver.find_element(By.XPATH, Locators.sauces_non_active).click()

        element = driver.find_element(By.XPATH,Locators.sauces_active).text
        assert 'Соусы' in element

    def test_tarnsfer_to_stuffing_in_constructor_click_on_stuffing_stuffing_active(self, driver):
        driver.get(url)

        driver.find_element(By.XPATH, Locators.stuffing_non_active).click()

        element = driver.find_element(By.XPATH,Locators.stuffing_active).text
        assert 'Начинки' in element
    def test_tarnsfer_to_buns_in_constructor_click_on_buns_buns_active(self, driver):
        driver.get(url)

        driver.find_element(By.XPATH,Locators.stuffing_non_active).click()
        driver.find_element(By.XPATH, Locators.buns_non_active).click()

        element = driver.find_element(By.XPATH,Locators.buns_active).text
        assert 'Булки' in element

