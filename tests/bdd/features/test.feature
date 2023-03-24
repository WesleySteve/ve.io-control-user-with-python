


Feature: Sum

    Scenario: Sum of positive integers
            """
            Being user i want to add two numbers and see the result
            """
        When sum "2" and "2"
        Then result must equal "4"
