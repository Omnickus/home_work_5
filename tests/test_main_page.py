import pytest
from src.constructor import Find_el

@pytest.mark.main_page
class Test_main_page:

    def test_check_slider(self, browser):
        Find_el( path = '//*[@id="slideshow0"]', browser=browser, time = 7 ).find_by_xpah

    def test_check_shopping_cart(self, browser):
        Find_el( path = '//*[@id="cart"]', browser=browser, time = 7 ).find_by_xpah

    def test_main_page_menu(self, browser):
        menu_items = browser.find_elements_by_css_selector("ul.navbar-nav > li")
        assert len(menu_items) == 8, "Неверное количество элементов меню"

    def test_main_page_fetured_items(self, browser):
        fetured_items = browser.find_elements_by_class_name("product-thumb")
        assert len(fetured_items) == 4, "Неверное количество продуктов в блоке featured"

    def test_main_page_footer_blocks(self, browser):
        footer_blocks = browser.find_elements_by_xpath("//footer//ul")
        result = footer_blocks[0].location_once_scrolled_into_view
        assert len(footer_blocks) == 4, "Неверное количество списков ссылок в футере"

    def test_main_page_open_product(self, browser):
        fetured_items = browser.find_elements_by_class_name("product-thumb")
        fetured_items[2].location_once_scrolled_into_view
        fetured_items[2].click()
        browser.find_elements_by_link_text("Apple Cinema")
