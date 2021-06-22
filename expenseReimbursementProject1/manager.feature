Feature: Multiple Logins should be Supported

  Scenario: Manager is on Employee Home Page
    Given I navigate to the Manager Home Page
    When I  Login In
    Then I should be on Manager Login Page
    When I submit email
    When I submit password
    When I click on Enter

    When I click on Display
    Then I should be on Reimbursements Page

   Scenario: Manager is on Employee Home Page2
    Given I navigate to the Manager Home Page
    When I  Login In
    Then I should be on Manager Login Page
    When I submit email
    When I submit password
    When I click on Enter
    When I click on Statistics
    Then I should be on Statistics Page




 Scenario: Manager is on Employee Home Page1
    Given I navigate to the Manager Home Page
    When I  Login In
    Then I should be on Manager Login Page
    When I submit email1
    When I submit password
    When I click on Enter

