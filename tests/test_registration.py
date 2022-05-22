import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.registration
def test_registration_page(browser):
    el = WebDriverWait(browser, timeout=5).until(EC.presence_of_element_located((By.LINK_TEXT, 'My Account')))
    el.click()
    el = WebDriverWait(browser, timeout=5).until(EC.presence_of_element_located((By.LINK_TEXT, 'Register')))
    el.click()
    el = WebDriverWait(browser, timeout=5).until(EC.presence_of_element_located((By.NAME, 'firstname')))
    el = WebDriverWait(browser, timeout=5).until(EC.presence_of_element_located((By.NAME, 'lastname')))
    el = WebDriverWait(browser, timeout=5).until(EC.presence_of_element_located((By.NAME, 'email')))
    el = WebDriverWait(browser, timeout=5).until(EC.presence_of_element_located((By.NAME, 'telephone')))
    el = WebDriverWait(browser, timeout=5).until(EC.presence_of_element_located((By.NAME, 'password')))
    el = WebDriverWait(browser, timeout=5).until(EC.presence_of_element_located((By.NAME, 'confirm')))
    el = WebDriverWait(browser, timeout=5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/form/fieldset[3]/div/div/label[1]/input'))).click()
    el = WebDriverWait(browser, timeout=5).until(EC.presence_of_element_located((By.NAME, 'agree'))).click()
    el = WebDriverWait(browser, timeout=5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/form/div/div/input[2]'))).click()
