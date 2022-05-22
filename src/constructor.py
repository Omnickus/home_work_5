from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Find_el:
    """
    Вспомогательный класс для работы с элементами DOM
    """
    def __init__(self, path = None, browser = None, time = None):
        self._path = path
        self._browser = browser
        self._wtime = time
        
    @property
    def find_by_xpah(self):
        return WebDriverWait(self._browser, timeout=10).until(EC.presence_of_element_located((By.XPATH, self._path)))

    @property
    def find_by_id(self):
        return WebDriverWait(self._browser, timeout=10).until(EC.presence_of_element_located((By.ID, self._path)))

    @property
    def find_by_name(self):
        return WebDriverWait(self._browser, timeout=10).until(EC.presence_of_element_located((By.NAME, self._path)))
    
    @property
    def find_by_selector(self):
        return WebDriverWait(self._browser, timeout=10).until(EC.presence_of_element_located((By.CSS_SELECTOR, self._path)))

    @property
    def find_by_link_text(self):
        return WebDriverWait(self._browser, timeout=10).until(EC.presence_of_element_located((By.LINK_TEXT, self._path)))
