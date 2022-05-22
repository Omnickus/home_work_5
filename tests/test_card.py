import pytest
from elements import El_main_page
from src.constructor import Find_el
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.card
@pytest.mark.parametrize("path", El_main_page.featured)
def test_main_page_featured(path, browser):
    Find_el(path = path, browser = browser, time = 5).find_by_xpah.click()
    Find_el(path = 'button-cart', browser = browser, time = 5).find_by_id
    Find_el(path = 'Tweet', browser = browser, time = 5).find_by_link_text
    Find_el(path = 'Description', browser = browser, time = 5).find_by_link_text
    Find_el(path = '//*[contains(text(), "Reviews")]', browser = browser, time = 5).find_by_xpah
