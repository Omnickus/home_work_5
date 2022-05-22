import pytest
from elements import El_catalog
from src.constructor import Find_el

@pytest.mark.catalog
@pytest.mark.parametrize("url", El_catalog.common_url)
def test_catalogs_page(url, browser):
    """
    Проверяет общие элементы для разных категорий
    """
    browser.get(browser.url + url)
    Find_el(path = El_catalog.common_elements['элементы_сеткой'], browser = browser, time = 5).find_by_xpah
    Find_el(path = El_catalog.common_elements['элементы_списком'], browser = browser, time = 5).find_by_xpah
    Find_el(path = El_catalog.common_elements['сортирвка_товара'], browser = browser, time = 5).find_by_xpah
    Find_el(path = El_catalog.common_elements['количество_товаров_на_странице'], browser = browser, time = 5).find_by_xpah

