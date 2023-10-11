from selenium.webdriver.common.by import By
from browser import Browser

class LoginPage(Browser):

    EMAIL_INPUT = (By.ID, 'Email')
    PASSWORD_INPUT = (By.ID, 'Password')
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Log in']")
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT,'Forgot password?')

    def navigate_to_login_page(self):
        self.driver.get('https://demo.nopcommerce.com/login')

    def set_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys('email')

    def set_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys('password')

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def click_forgot_password_link(self):
        self.driver.find_element(*self.FORGOT_PASSWORD_LINK).click()




