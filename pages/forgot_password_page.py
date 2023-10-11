from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from browser import Browser


class ForgotPasswordPage(Browser):
    EMAIL_INPUT = (By.ID, 'Email')
    RECOVERY_BUTTON = (By.NAME, 'send_email')
    NOTIFICATION_ERROR = (By.XPATH, "//p[@class='content']")
    MESSAGE_ERROR = (By.ID,'Email-error')

    def navigate_to_forgot_password_page(self):
        self.driver.get('https://demo.nopcommerce.com/passwordrecovery')

    def set_email(self,email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def recovery_button(self):
        self.driver.find_element(*self.RECOVERY_BUTTON).click()

    def verify_email_error_message(self, expected_message):
        try:
            actual_message = self.driver.find_element(*self.MESSAGE_ERROR).text
        except NoSuchElementException:
            actual_message = 'None' # nu s-a afisat elementul

        assert actual_message == expected_message, f'Error the message is incorect'

    def verify_notification_message(self, expected_notification):
        try:
            actual_notification = self.driver.find_element(*self.NOTIFICATION_ERROR).text
        except NoSuchElementException:
            actual_notification = 'None' # nu s-a afisat elementul

        assert actual_notification == expected_notification, f'Error the notification message is incorect'
        


