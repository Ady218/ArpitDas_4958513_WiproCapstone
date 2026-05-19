import os
import time

import allure

from pages.home_page import HomePage
from pages.macbook_page import MacBookPage
from pages.cart_page import CartPage

from utilities.logger import LogGen


@allure.feature("BestBuy End To End Automation")
class TestEndToEndFlow:

    logger = LogGen.loggen()

    @allure.title("Complete Ecommerce Workflow")
    def test_complete_ecommerce_flow(
            self,
            setup
    ):

        driver = setup

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

        processor_found = macbook.select_processor(
            "Apple M4"
        )

        assert processor_found is True

        self.logger.info("Adding Product To Cart")

        macbook.click_listing_add_to_cart(
            "Apple M4"
        )

        macbook.click_go_to_cart()

        self.logger.info("Proceeding To Checkout")

        cart.click_checkout()

        time.sleep(3)

        assert (
                "checkout" in driver.current_url.lower()
                or
                "signin" in driver.current_url.lower()
        )

        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        driver.save_screenshot(
            "screenshots/end_to_end_flow.png"
        )

        self.logger.info(
            "End To End Flow Passed"
        )