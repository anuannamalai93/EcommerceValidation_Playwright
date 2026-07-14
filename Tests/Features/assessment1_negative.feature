Feature: Assessment1_negative

  Scenario: Invalid search
    Given the user is on the products page
    When the user searches for junk value
    Then the search results should not fetch any product

  Scenario: Register with existing user
    Given the user is on the products page
    And the user searches for sleeveless adds first 2 products to the cart
    And proceeds to checkout
    When the user registers with an existing email
    Then the user should see an error message indicating that the email is already in use