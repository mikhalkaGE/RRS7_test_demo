import pytest
import time
from data import AuthData
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture
def inventory_page(driver):
    return InventoryPage(driver)

@pytest.fixture
def base_page(driver):
    return BasePage(driver)
    
@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

class TestAuth:

    def test_login_form(self, base_page, login_page, inventory_page):
        base_page.open_browser(AuthData.BASE_URL)
        login_page.login(AuthData.LOGIN, AuthData.PASSWORD)
        time.sleep(2)
        assert inventory_page.driver.current_url == f'{AuthData.BASE_URL}/inventory.html'

    @pytest.mark.parametrize("username, password, error", [
        (AuthData.INVALID_LOGIN[0], AuthData.INVALID_PASSWORD[0], AuthData.AUTH_ERROR[0]),
        (AuthData.INVALID_LOGIN[1], AuthData.INVALID_PASSWORD[1], AuthData.AUTH_ERROR[1])
        ])
    def test_login_form_validation(self, base_page, login_page, username, password, error):
        base_page.open_browser(AuthData.BASE_URL)
        login_page.login(username, password)
        time.sleep(2)
        assert login_page.validation_error().is_displayed(), 'Validation error is not presented!'
        assert error in login_page.validation_error().text
        
