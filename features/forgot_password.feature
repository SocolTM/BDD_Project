Feature: Check the forgot password functionality

  @regression
  Scenario: Check validation error message when email is invalid format
    Given forgot_pass: I am a user on the forgot password page
    When forgot_pass: I fill in my email "my_email@"
    When forgot_pass: I click on the recover button
    Then forgot_pass: I verify the invalid email validation message "Wrong email"

  @regression
  Scenario:  Check validation error message when email is empty
    Given forgot_pass: I am a user on the forgot password page
    When forgot_pass: I make sure the email input is cleared
    When forgot_pass: I click on the recover button
    Then forgot_pass: I verify the invalid email validation message "Enter your email"

  @bat
  Scenario Outline: Check various email validation
    Given forgot_pass: I am a user on the forgot password page
    When forgot_pass: I fill in my email "<email>"
    When forgot_pass: I click on the recover button
    Then forgot_pass: I verify the invalid email validation message "<expected_error>"
    Then forgot_pass: I verify the notification "<expected_notification>"

  Examples:
    |email        |expected_error  |expected_notification     |
    |test         |Wrong email     |None                      |
    |test@        |Wrong email     |None                      |
    |test@mail.com|None            |Email not found.          |