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

checkout_negative_data = ExcelUtils.get_all_data(
    path,
    "CheckoutNegativeData"
)


# =========================================================
# POSITIVE FLOW
# =========================================================

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

        home = HomePage(driver)

        macbook = MacBookPage(driver)

        cart = CartPage(driver)

        self.logger.info("Opening BestBuy")

        home.open_bestbuy()

        # WEBSITE VALIDATION
        assert "Best Buy" in home.get_title()

        self.logger.info("Selecting Country")

        home.click_country()

        # HOMEPAGE VALIDATION
        assert "bestbuy" in driver.current_url.lower()

        self.logger.info("Opening Top Deals")

        home.click_top_deals()

        self.logger.info("Opening Apple")

        home.click_apple()

        # APPLE PAGE VALIDATION
        assert "apple" in driver.page_source.lower()

        self.logger.info("Opening MacBook")

        macbook.click_macbook()

        # MACBOOK PAGE VALIDATION
        assert "macbook" in driver.page_source.lower()

        self.logger.info("Selecting Processor Filter")

        macbook.select_processor_filter()

        self.logger.info(
            f"Selecting Processor: {processor}"
        )

        processor_found = macbook.select_processor(
            processor
        )

        # PROCESSOR VALIDATION
        assert processor_found is True

        # ==========================================
        # ADD TO CART SCENARIO
        # ==========================================

        if scenario == "AddToCart":

            macbook.click_listing_add_to_cart(
                processor
            )

            macbook.click_go_to_cart()

            # CART VALIDATION
            assert "cart" in driver.current_url.lower()

            self.logger.info(
                "Add To Cart Passed"
            )

        # ==========================================
        # CHECKOUT SCENARIO
        # ==========================================

        elif scenario == "Checkout":

            macbook.click_listing_add_to_cart(
                processor
            )

            macbook.click_go_to_cart()

            # CART VALIDATION
            assert cart.verify_cart_item()

            cart.click_checkout()

            time.sleep(5)

            # CHECKOUT VALIDATION
            assert (
                    "checkout" in driver.current_url.lower()
                    or
                    "signin" in driver.current_url.lower()
            )

            self.logger.info(
                "Checkout Flow Passed"
            )

        # ==========================================
        # VALIDATE CART SCENARIO
        # ==========================================

        elif scenario == "ValidateCart":

            macbook.click_listing_add_to_cart(
                processor
            )

            macbook.click_go_to_cart()

            # CART VALIDATION
            assert cart.verify_cart_item()

            self.logger.info(
                "Cart Validation Passed"
            )

        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        driver.save_screenshot(
            f"screenshots/{tc_id}.png"
        )

        allure.attach.file(
            f"screenshots/{tc_id}.png",
            name=tc_id,
            attachment_type=allure.attachment_type.PNG
        )

        self.logger.info(
            "Positive Test Passed"
        )


# =========================================================
# NEGATIVE FLOW
# =========================================================

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

        home = HomePage(driver)

        macbook = MacBookPage(driver)

        self.logger.info("Opening BestBuy")

        home.open_bestbuy()

        # WEBSITE VALIDATION
        assert "Best Buy" in home.get_title()

        self.logger.info("Selecting Country")

        home.click_country()

        # HOMEPAGE VALIDATION
        assert "bestbuy" in driver.current_url.lower()

        self.logger.info("Opening Top Deals")

        home.click_top_deals()

        self.logger.info("Opening Apple")

        home.click_apple()

        # APPLE PAGE VALIDATION
        assert "apple" in driver.page_source.lower()

        self.logger.info("Opening MacBook")

        macbook.click_macbook()

        # MACBOOK PAGE VALIDATION
        assert "macbook" in driver.page_source.lower()

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

        allure.attach.file(
            f"screenshots/{tc_id}.png",
            name=tc_id,
            attachment_type=allure.attachment_type.PNG
        )

        self.logger.info(
            "Negative Test Passed"
        )


# =========================================================
# CHECKOUT NEGATIVE FLOW
# =========================================================

@allure.feature("Checkout Negative Automation")
class TestCheckoutNegativeFlow:

    logger = LogGen.loggen()

    @pytest.mark.parametrize(
        "tc_id, email, scenario",
        checkout_negative_data
    )

    @allure.title("Invalid Checkout Email")
    def test_invalid_checkout_email(
            self,
            setup,
            tc_id,
            email,
            scenario
    ):

        driver = setup

        home = HomePage(driver)

        macbook = MacBookPage(driver)

        cart = CartPage(driver)

        self.logger.info("Opening BestBuy")

        home.open_bestbuy()

        # WEBSITE VALIDATION
        assert "Best Buy" in home.get_title()

        self.logger.info("Selecting Country")

        home.click_country()

        # HOMEPAGE VALIDATION
        assert "bestbuy" in driver.current_url.lower()

        self.logger.info("Opening Top Deals")

        home.click_top_deals()

        self.logger.info("Opening Apple")

        home.click_apple()

        # APPLE PAGE VALIDATION
        assert "apple" in driver.page_source.lower()

        self.logger.info("Opening MacBook")

        macbook.click_macbook()

        # MACBOOK PAGE VALIDATION
        assert "macbook" in driver.page_source.lower()

        self.logger.info("Selecting Processor Filter")

        macbook.select_processor_filter()

        processor_found = macbook.select_processor(
            "Apple M4"
        )

        # PROCESSOR VALIDATION
        assert processor_found is True

        self.logger.info("Adding Product To Cart")

        macbook.click_listing_add_to_cart(
            "Apple M4"
        )

        macbook.click_go_to_cart()

        # CART VALIDATION
        assert cart.verify_cart_item()

        self.logger.info("Proceeding To Checkout")

        cart.click_checkout()

        # # CHECKOUT VALIDATION
        # assert (
        #         "checkout" in driver.current_url.lower()
        #         or
        #         "signin" in driver.current_url.lower()
        # )

        self.logger.info("Entering Invalid Email")

        cart.enter_invalid_email(email)

        cart.click_continue()

        # INVALID EMAIL VALIDATION
        assert cart.verify_invalid_email_error()

        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        driver.save_screenshot(
            f"screenshots/{tc_id}.png"
        )

        allure.attach.file(
            f"screenshots/{tc_id}.png",
            name=tc_id,
            attachment_type=allure.attachment_type.PNG
        )

        self.logger.info(
            "Invalid Checkout Email Test Passed"
        )