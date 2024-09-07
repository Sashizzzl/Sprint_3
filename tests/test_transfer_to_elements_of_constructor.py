import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
def test_tarnsfer_to_sauces_in_constructor_click_on_sauce_souce_active():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(By.XPATH, ".//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Соусы']").click()

    element = driver.find_element(By.XPATH,".//div[contains(@class,'current')]/span[text()='Соусы']").text
    assert 'Соусы' in element

    driver.quit()

def test_tarnsfer_to_stuffing_in_constructor_click_on_stuffing_stuffing_active():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(By.XPATH, ".//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Начинки']").click()

    element = driver.find_element(By.XPATH,".//div[contains(@class,'current')]/span[text()='Начинки']").text
    assert 'Начинки' in element

    driver.quit()

def test_tarnsfer_to_buns_in_constructor_click_on_buns_buns_active():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(By.XPATH,".//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Начинки']").click()
    driver.find_element(By.XPATH, ".//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Булки']").click()

    element = driver.find_element(By.XPATH,".//div[contains(@class,'current')]/span[text()='Булки']").text
    assert 'Булки' in element

    driver.quit()
