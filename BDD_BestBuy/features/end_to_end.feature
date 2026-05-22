Feature: BestBuy End To End Automation

    Scenario: Complete Ecommerce Workflow

        Given user loads end to end test data

        And user opens BestBuy website

        When user selects country

        And user opens Top Deals

        And user opens Apple section

        And user opens MacBook section

        And user selects processor filter

        And user selects processor from excel data

        And user adds product to cart

        And user opens cart

        And user proceeds to checkout

        Then checkout page should open successfully