import pytest

from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def driver():
    """
    fixtura, ktora sluzy do setupowania drivera selenium, wykorzystuje webdriver managera, dzieki czemu nie trzeba
    podawac sciezki do chrome/geckodrivera
    """
    options = webdriver.ChromeOptions()
    browser.set_driver(webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options))
    browser.driver().maximize_window()
    yield browser
    browser.quit()


@pytest.fixture
def session_browser(driver):
    """
    fixtura, ktora sluzy do wywolywania metod zapisanych w driverze
    """
    yield driver
