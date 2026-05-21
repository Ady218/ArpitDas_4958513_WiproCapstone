# =========================================================
# test_end_to_end_flow.py
# =========================================================

import os
import time

import allure
from selenium.webdriver.common.by import By

from pages.home_page import HomePage
from pages.macbook_page import MacBookPage
from pages.cart_page import CartPage

from utilities.logger import LogGen
from utilities.screenshot import Screenshot

from datetime import datetime


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

        # =====================================================
        # OPEN WEBSITE
        # =====================================================

        self.logger.info("Opening BestBuy")

        home.open_bestbuy()

        Screenshot.capture(
            driver,
            "01_Homepage_Opened"
        )

        assert "Best Buy" in home.get_title()

        # =====================================================
        # SELECT COUNTRY
        # =====================================================

        self.logger.info("Selecting Country")

        home.click_country()

        Screenshot.capture(
            driver,
            "02_Country_Selected"
        )

        assert "bestbuy" in driver.current_url.lower()

        # =====================================================
        # OPEN TOP DEALS
        # =====================================================

        self.logger.info("Opening Top Deals")

        home.click_top_deals()

        Screenshot.capture(
            driver,
            "03_Top_Deals_Page"
        )

        # =====================================================
        # OPEN APPLE
        # =====================================================

        self.logger.info("Opening Apple")

        home.click_apple()

        Screenshot.capture(
            driver,
            "04_Apple_Page"
        )

        assert "apple" in driver.page_source.lower()

        # =====================================================
        # OPEN MACBOOK
        # =====================================================

        self.logger.info("Opening MacBook")

        macbook.click_macbook()

        Screenshot.capture(
            driver,
            "05_MacBook_Page"
        )

        assert "macbook" in driver.page_source.lower()

        # =====================================================
        # OPEN PROCESSOR FILTER
        # =====================================================

        self.logger.info("Selecting Processor Filter")

        macbook.select_processor_filter()

        Screenshot.capture(
            driver,
            "06_Processor_Filter"
        )

        # =====================================================
        # SELECT PROCESSOR
        # =====================================================

        self.logger.info("Selecting Apple M4 Processor")

        processor_found = macbook.select_processor(
            "Apple M4"
        )

        Screenshot.capture(
            driver,
            "07_Processor_Selected"
        )

        assert processor_found is True

        # =====================================================
        # ADD TO CART
        # =====================================================

        self.logger.info("Adding Product To Cart")

        macbook.click_listing_add_to_cart(
            "Apple M4"
        )

        Screenshot.capture(
            driver,
            "08_Product_Added"
        )

        # =====================================================
        # GO TO CART
        # =====================================================

        macbook.click_go_to_cart()

        Screenshot.capture(
            driver,
            "09_Cart_Page"
        )

        assert cart.verify_cart_item()

        # =====================================================
        # CHECKOUT
        # =====================================================

        self.logger.info("Proceeding To Checkout")

        cart.click_checkout()

        Screenshot.capture(
            driver,
            "10_Checkout_Page"
        )

        assert driver.find_element(
            By.XPATH,
            "//input[@type='email']"
        ).is_displayed()

        self.logger.info(
            "End To End Flow Passed"
        )