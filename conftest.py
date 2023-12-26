import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def options():
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    yield options 

@pytest.fixture
def driver(options):
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit() 

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=5)
    yield wait
