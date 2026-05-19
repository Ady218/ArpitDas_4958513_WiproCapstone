import os
import time

import pytest
import allure

from pages.home_page import HomePage
from pages.macbook_page import MacBookPage
from pages.cart_page import CartPage

from utilities.logger import LogGen
from utilities.excel_utils import ExcelUtils


path = "data/testdata.xlsx"

test_data = ExcelUtils.get_all_data(
    path,
    "PositiveData"
)

negative_test_data = ExcelUtils.get_all_data(
    path,
    "NegativeData"
)


@allure.feature("BestBuy Positive Automation")
class TestPositiveFlow:

    logger = LogGen.loggen()

    @pytest.mark.parametrize(
        "tc_id, processor, scenario",
        test_data
    )

    @allure.title("Positive Ecommerce Flow")
    def test_positive_flow(
            self,
            setup,
            tc_id,
            processor,
            scenario
    ):

        driver = setup

        print(tc_id)
        print(processor)
        print(scenario)

        home = HomePage(driver)

        macbook = MacBookPage(driver)

        cart = CartPage(driver)

        self.logger.info("Opening BestBuy")

        home.open_bestbuy()

        self.logger.info("Selecting Country")

        home.click_country()

        self.logger.info("Opening Top Deals")

        home.click_top_deals()

        self.logger.info("Opening Apple")

        home.click_apple()

        self.logger.info("Opening MacBook")

        macbook.click_macbook()

        self.logger.info("Selecting Processor Filter")

        macbook.select_processor_filter()

        self.logger.info(f"Selecting Processor: {processor}")

        processor_found = macbook.select_processor(processor)

        assert processor_found is True

        # ==========================================
        # ADD TO CART SCENARIO
        # ==========================================

        if scenario == "AddToCart":

            macbook.click_listing_add_to_cart(processor)

            macbook.click_go_to_cart()

            assert "cart" in driver.current_url.lower()

            self.logger.info("Add To Cart Passed")

        # ==========================================
        # CHECKOUT SCENARIO
        # ==========================================

        elif scenario == "Checkout":

            macbook.click_listing_add_to_cart(processor)

            macbook.click_go_to_cart()

            cart.click_checkout()

            time.sleep(5)

            self.logger.info("Checkout Flow Passed")

        # ==========================================
        # VALIDATE CART SCENARIO
        # ==========================================

        elif scenario == "ValidateCart":

            macbook.click_listing_add_to_cart(processor)

            macbook.click_go_to_cart()

            assert cart.verify_cart_item()

            self.logger.info("Cart Validation Passed")

        driver.save_screenshot(
            f"screenshots/{tc_id}.png"
        )

        self.logger.info("Positive Test Passed")

@allure.feature("BestBuy Negative Automation")
class TestNegativeFlow:

    logger = LogGen.loggen()

    @pytest.mark.parametrize(
        "tc_id, processor, scenario",
        negative_test_data
    )

    @allure.title("Negative Ecommerce Flow")
    def test_negative_flow(
            self,
            setup,
            tc_id,
            processor,
            scenario
    ):

        driver = setup

        print(tc_id)
        print(processor)
        print(scenario)

        home = HomePage(driver)

        macbook = MacBookPage(driver)

        self.logger.info("Opening BestBuy")

        home.open_bestbuy()

        self.logger.info("Selecting Country")

        home.click_country()

        self.logger.info("Opening Top Deals")

        home.click_top_deals()

        self.logger.info("Opening Apple")

        home.click_apple()

        self.logger.info("Opening MacBook")

        macbook.click_macbook()

        self.logger.info("Selecting Processor Filter")

        macbook.select_processor_filter()

        self.logger.info(
            f"Selecting Invalid Processor: {processor}"
        )

        processor_found = macbook.select_processor(
            processor
        )

        # ==========================================
        # INVALID FILTER TEST
        # ==========================================

        if scenario == "InvalidFilter":

            assert processor_found is False

            self.logger.info(
                "Invalid Filter Handled Successfully"
            )

        # ==========================================
        # UNSUPPORTED FILTER TEST
        # ==========================================

        elif scenario == "UnsupportedFilter":

            assert processor_found is False

            self.logger.info(
                "Unsupported Filter Handled Successfully"
            )
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        driver.save_screenshot(
            f"screenshots/{tc_id}.png"
        )

        self.logger.info("Negative Test Passed")