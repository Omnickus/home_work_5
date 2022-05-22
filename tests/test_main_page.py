import pytest
from src.constructor import Find_el

@pytest.mark.main_page
def test_check_slider(browser):
    Find_el( path = '//*[@id="slideshow0"]', browser=browser, time = 7 ).find_by_xpah

@pytest.mark.main_page
def test_check_shopping_cart(browser):
    Find_el( path = '//*[@id="cart"]', browser=browser, time = 7 ).find_by_xpah

@pytest.mark.main_page
def test_main_page_menu(browser):
    menu_items = browser.find_elements_by_css_selector("ul.navbar-nav > li")
    assert len(menu_items) == 8, "Неверное количество элементов меню"

@pytest.mark.main_page
def test_main_page_fetured_items(browser):
    fetured_items = browser.find_elements_by_class_name("product-thumb")
    assert len(fetured_items) == 4, "Неверное количество продуктов в блоке featured"

@pytest.mark.main_page
def test_main_page_footer_blocks(browser):
    footer_blocks = browser.find_elements_by_xpath("//footer//ul")
    result = footer_blocks[0].location_once_scrolled_into_view
    assert len(footer_blocks) == 4, "Неверное количество списков ссылок в футере"

@pytest.mark.main_page
def test_main_page_open_product(browser):
    fetured_items = browser.find_elements_by_class_name("product-thumb")
    fetured_items[2].location_once_scrolled_into_view
    fetured_items[2].click()
    browser.find_elements_by_link_text("Apple Cinema")
