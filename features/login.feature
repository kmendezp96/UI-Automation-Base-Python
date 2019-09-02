Feature: Github login

    Scenario: Trying to sign up
        Given the user is on the github page
        When the user fills the sign up form with
            | Username               | Email                              | Password          |
            | fakeUserThatIsLearning | fakeUserThatIsLearning34@gmail.com | VALIDpassword3434 |
        And the user clicks on sign up button
        Then the user should be on the join page
