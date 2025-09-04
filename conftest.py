import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    """Фикстура для создания браузера"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()