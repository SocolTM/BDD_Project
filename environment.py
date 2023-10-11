from browser import Browser
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage

def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.forgot_password_page = ForgotPasswordPage()

def after_all(context):
    context.browser.close()
