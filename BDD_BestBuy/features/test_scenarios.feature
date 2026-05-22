# =========================================================
# test_scenarios.feature
# =========================================================

Feature: BestBuy Scenario Validations


    # =====================================================
    # POSITIVE FLOW TEST CASES
    # =====================================================

    Scenario: TC_01 Validate Apple M4 Add To Cart Flow

        Given user loads positive test data "TC_01"

        When user opens BestBuy website for positive flow

        And user selects country for positive flow

        And user opens Top Deals for positive flow

        And user opens Apple section for positive flow

        And user opens MacBook section for positive flow

        And user selects processor filter for positive flow

        And user selects processor for positive flow

        Then positive ecommerce validation should pass


    Scenario: TC_02 Validate Apple M3 Add To Cart Flow

        Given user loads positive test data "TC_02"

        When user opens BestBuy website for positive flow

        And user selects country for positive flow

        And user opens Top Deals for positive flow

        And user opens Apple section for positive flow

        And user opens MacBook section for positive flow

        And user selects processor filter for positive flow

        And user selects processor for positive flow

        Then positive ecommerce validation should pass


    Scenario: TC_03 Validate Apple M4 Checkout Flow

        Given user loads positive test data "TC_03"

        When user opens BestBuy website for positive flow

        And user selects country for positive flow

        And user opens Top Deals for positive flow

        And user opens Apple section for positive flow

        And user opens MacBook section for positive flow

        And user selects processor filter for positive flow

        And user selects processor for positive flow

        Then positive ecommerce validation should pass


    Scenario: TC_04 Validate Apple M3 Cart Validation Flow

        Given user loads positive test data "TC_04"

        When user opens BestBuy website for positive flow

        And user selects country for positive flow

        And user opens Top Deals for positive flow

        And user opens Apple section for positive flow

        And user opens MacBook section for positive flow

        And user selects processor filter for positive flow

        And user selects processor for positive flow

        Then positive ecommerce validation should pass


    # =====================================================
    # NEGATIVE FLOW TEST CASES
    # =====================================================

    Scenario: TC_05 Validate Invalid Processor Filter

        Given user loads negative test data "TC_05"

        When user opens BestBuy website for negative flow

        And user selects country for negative flow

        And user opens Top Deals for negative flow

        And user opens Apple section for negative flow

        And user opens MacBook section for negative flow

        And user selects processor filter for negative flow

        And user selects invalid processor

        Then negative ecommerce validation should pass


    Scenario: TC_06 Validate Unsupported Processor Filter

        Given user loads negative test data "TC_06"

        When user opens BestBuy website for negative flow

        And user selects country for negative flow

        And user opens Top Deals for negative flow

        And user opens Apple section for negative flow

        And user opens MacBook section for negative flow

        And user selects processor filter for negative flow

        And user selects invalid processor

        Then negative ecommerce validation should pass


    # =====================================================
    # CHECKOUT NEGATIVE FLOW
    # =====================================================

    Scenario: TC_07 Validate Invalid Checkout Email

        Given user loads checkout negative data "TC_07"

        When user opens BestBuy website for checkout flow

        And user selects country for checkout flow

        And user opens Top Deals for checkout flow

        And user opens Apple section for checkout flow

        And user opens MacBook section for checkout flow

        And user selects processor filter for checkout flow

        And user selects processor for checkout flow

        And user adds product to cart for checkout flow

        And user opens cart for checkout flow

        And user proceeds to checkout for checkout flow

        And user enters invalid email

        Then checkout negative validation should pass


    # =====================================================
    # NAVIGATION FLOW
    # =====================================================

    Scenario: TC_08 Validate Apple Navigation Flow

        Given user loads navigation data "TC_08"

        When user opens BestBuy website for navigation flow

        And user selects country for navigation flow

        And user opens Top Deals for navigation flow

        And user opens Apple section for navigation flow

        Then navigation validation should pass