import pytest
from src.constructor import Find_el

@pytest.mark.admin
def test_login_page_admin(browser):
    browser.get(browser.url + "/admin")
    Find_el(path = 'input-username', browser = browser, time = 5).find_by_id
    Find_el(path = 'password', browser = browser, time = 5).find_by_name
    Find_el(path = "button[type='submit']", browser = browser, time = 5).find_by_selector
    Find_el(path = "Forgotten Password", browser = browser, time = 5).find_by_link_text
    Find_el(path = "//*[text()='OpenCart']", browser = browser, time = 5).find_by_xpah
