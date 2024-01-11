class AuthData:
    BASE_URL = 'https://www.saucedemo.com'
    LOGIN = 'standard_user'
    PASSWORD = 'secret_sauce'
    INVALID_LOGIN = ('locked_out_user', 'user')
    INVALID_PASSWORD = ('secret_sauce', 'user')
    AUTH_ERROR = ('Epic sadface: Sorry, this user has been locked out.',
    'Epic sadface: Username and password do not match any user in this service')

class InventoryData:
    item_id = '4'
    item = 'backpack'
