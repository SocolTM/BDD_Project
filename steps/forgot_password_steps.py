from behave import *

@Given("forgot_pass: I am a user on the forgot password page")
def step_impl(context):
    context.forgot_password_page.navigate_to_forgot_password_page()

@When('forgot_pass: I fill in my email "{e_mail}"')
def step_impl(context, e_mail):
    context.forgot_password_page.set_email(e_mail)

@When("forgot_pass: I click on the recover button")
def step_impl(context):
    context.forgot_password_page.click_recovery_button()

@Then('forgot_pass: I verify the invalid email validation message "{msg}"')
def step_impl(context, msg):
    context.forgot_password_page.verify_email_error_message(msg)

@Then('forgot_pass: I verify the notification "{notification}"')
def step_impl(context,notification):
    context.forgot_password_page.verify_notification_message(notification)

@When('forgot_pass: I make sure the email input is cleared')
def step_impl(context):
    context.forgot_password_page.clear_email_input()