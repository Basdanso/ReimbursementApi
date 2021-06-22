Feature: Multiple Reimbursements Should be Supported


  Background: Employee is on Employee Home Page
    Given I navigate to the Employee Home Page
    When I click on Login
    Then I should be on Employee Login Page



    Scenario: Employee is on Create Reimbursements Page
     When I submit email as Employee
    When I submit password as Employee
    When I click on Enter
    Given I navigate to the Create Reimbursements Page
    When I submit an email
    When I submit amount
    When I submit reason
    When I enter on submit

   Scenario: Employee is on Create Reimbursements Page
     When I submit email1 as Employee
    When I submit password as Employee
    When I click on Enter
