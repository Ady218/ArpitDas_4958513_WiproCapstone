
import pytest
import allure

from selenium.webdriver.common.by import By

from pages.home_page import HomePage
from pages.macbook_page import MacBookPage
from pages.cart_page import CartPage

from utilities.logger import LogGen
from utilities.excel_utils import ExcelUtils
from utilities.screenshot import Screenshot


# =========================================================
# EXCEL DATA
# =========================================================

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

navigation_data = ExcelUtils.get_all_data(
    path,
    "NavigationData"
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

        # =====================================================
        # OPEN WEBSITE
        # =====================================================

        self.logger.info("Opening BestBuy")

        home.open_bestbuy()

        Screenshot.capture(
            driver,
            f"{tc_id}_01_Homepage"
        )

        assert "Best Buy" in home.get_title()

        # =====================================================
        # COUNTRY
        # =====================================================

        self.logger.info("Selecting Country")

        home.click_country()

        assert "bestbuy" in driver.current_url.lower()

        # =====================================================
        # TOP DEALS
        # =====================================================

        self.logger.info("Opening Top Deals")

        home.click_top_deals()

        # =====================================================
        # APPLE
        # =====================================================

        self.logger.info("Opening Apple Section")

        home.click_apple()

        Screenshot.capture(
            driver,
            f"{tc_id}_02_Apple"
        )

        assert "apple" in driver.page_source.lower()

        # =====================================================
        # MACBOOK
        # =====================================================

        self.logger.info("Opening MacBook Section")

        macbook.click_macbook()

        Screenshot.capture(
            driver,
            f"{tc_id}_03_MacBook"
        )

        assert "macbook" in driver.page_source.lower()

        # =====================================================
        # FILTER
        # =====================================================

        self.logger.info(
            "Opening Processor Filter"
        )

        macbook.select_processor_filter()

        # =====================================================
        # PROCESSOR
        # =====================================================

        self.logger.info(
            f"Selecting Processor: {processor}"
        )

        processor_found = macbook.select_processor(
            processor
        )

        Screenshot.capture(
            driver,
            f"{tc_id}_04_Processor"
        )

        assert processor_found is True

        # =====================================================
        # ADD TO CART
        # =====================================================

        if scenario == "AddToCart":

            self.logger.info(
                "Adding Product To Cart"
            )

            macbook.click_listing_add_to_cart(
                processor
            )

            Screenshot.capture(
                driver,
                f"{tc_id}_05_AddToCart"
            )

            self.logger.info(
                "Opening Cart"
            )

            macbook.click_go_to_cart()

            Screenshot.capture(
                driver,
                f"{tc_id}_06_Cart"
            )

            assert "cart" in driver.current_url.lower()

            self.logger.info(
                "Add To Cart Validation Passed"
            )

        # =====================================================
        # CHECKOUT
        # =====================================================

        elif scenario == "Checkout":

            self.logger.info(
                "Adding Product To Cart"
            )

            macbook.click_listing_add_to_cart(
                processor
            )

            Screenshot.capture(
                driver,
                f"{tc_id}_05_AddToCart"
            )

            self.logger.info(
                "Opening Cart"
            )

            macbook.click_go_to_cart()

            Screenshot.capture(
                driver,
                f"{tc_id}_06_Cart"
            )

            assert cart.verify_cart_item()

            self.logger.info(
                "Proceeding To Checkout"
            )

            cart.click_checkout()

            Screenshot.capture(
                driver,
                f"{tc_id}_07_Checkout"
            )

            # BETTER ASSERTION

            assert driver.find_element(
                By.XPATH,
                "//input[@type='email']"
            ).is_displayed()

            self.logger.info(
                "Checkout Validation Passed"
            )

        # =====================================================
        # VALIDATE CART
        # =====================================================

        elif scenario == "ValidateCart":

            self.logger.info(
                "Adding Product To Cart"
            )

            macbook.click_listing_add_to_cart(
                processor
            )

            Screenshot.capture(
                driver,
                f"{tc_id}_05_AddToCart"
            )

            self.logger.info(
                "Opening Cart"
            )

            macbook.click_go_to_cart()

            Screenshot.capture(
                driver,
                f"{tc_id}_06_Cart"
            )

            assert cart.verify_cart_item()

            self.logger.info(
                "Cart Validation Passed"
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

        # =====================================================
        # HOMEPAGE
        # =====================================================

        self.logger.info("Opening BestBuy")

        home.open_bestbuy()

        Screenshot.capture(
            driver,
            f"{tc_id}_01_Homepage"
        )

        # =====================================================
        # COUNTRY
        # =====================================================

        home.click_country()

        Screenshot.capture(
            driver,
            f"{tc_id}_02_Country"
        )

        # =====================================================
        # TOP DEALS
        # =====================================================

        home.click_top_deals()

        Screenshot.capture(
            driver,
            f"{tc_id}_03_TopDeals"
        )

        # =====================================================
        # APPLE
        # =====================================================

        home.click_apple()

        Screenshot.capture(
            driver,
            f"{tc_id}_04_Apple"
        )

        # =====================================================
        # MACBOOK
        # =====================================================

        macbook.click_macbook()

        Screenshot.capture(
            driver,
            f"{tc_id}_05_MacBook"
        )

        # =====================================================
        # FILTER
        # =====================================================

        macbook.select_processor_filter()

        Screenshot.capture(
            driver,
            f"{tc_id}_06_Filter"
        )

        # =====================================================
        # INVALID PROCESSOR
        # =====================================================

        self.logger.info(
            f"Selecting Invalid Processor: {processor}"
        )

        processor_found = macbook.select_processor(
            processor
        )

        Screenshot.capture(
            driver,
            f"{tc_id}_07_InvalidProcessor"
        )

        assert processor_found is False

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

        # =====================================================
        # HOMEPAGE
        # =====================================================

        self.logger.info("Opening BestBuy")

        home.open_bestbuy()

        Screenshot.capture(
            driver,
            f"{tc_id}_01_Homepage"
        )

        # =====================================================
        # COUNTRY
        # =====================================================

        home.click_country()

        Screenshot.capture(
            driver,
            f"{tc_id}_02_Country"
        )

        # =====================================================
        # TOP DEALS
        # =====================================================

        home.click_top_deals()

        Screenshot.capture(
            driver,
            f"{tc_id}_03_TopDeals"
        )

        # =====================================================
        # APPLE
        # =====================================================

        home.click_apple()

        Screenshot.capture(
            driver,
            f"{tc_id}_04_Apple"
        )

        # =====================================================
        # MACBOOK
        # =====================================================

        macbook.click_macbook()

        Screenshot.capture(
            driver,
            f"{tc_id}_05_MacBook"
        )

        # =====================================================
        # FILTER
        # =====================================================

        macbook.select_processor_filter()

        Screenshot.capture(
            driver,
            f"{tc_id}_06_Filter"
        )

        # =====================================================
        # PROCESSOR
        # =====================================================

        processor_found = macbook.select_processor(
            "Apple M4"
        )

        Screenshot.capture(
            driver,
            f"{tc_id}_07_Processor"
        )

        assert processor_found is True

        # =====================================================
        # ADD TO CART
        # =====================================================

        macbook.click_listing_add_to_cart(
            "Apple M4"
        )

        Screenshot.capture(
            driver,
            f"{tc_id}_08_AddToCart"
        )

        # =====================================================
        # CART
        # =====================================================

        macbook.click_go_to_cart()

        Screenshot.capture(
            driver,
            f"{tc_id}_09_Cart"
        )

        assert cart.verify_cart_item()

        # =====================================================
        # CHECKOUT
        # =====================================================

        cart.click_checkout()

        Screenshot.capture(
            driver,
            f"{tc_id}_10_Checkout"
        )

        # =====================================================
        # INVALID EMAIL
        # =====================================================

        self.logger.info(
            "Entering Invalid Email"
        )

        cart.enter_invalid_email(email)

        Screenshot.capture(
            driver,
            f"{tc_id}_11_InvalidEmail"
        )

        # =====================================================
        # CONTINUE
        # =====================================================

        cart.click_continue()

        Screenshot.capture(
            driver,
            f"{tc_id}_12_Error"
        )

        assert cart.verify_invalid_email_error()

        self.logger.info(
            "Invalid Checkout Email Test Passed"
        )

# =========================================================
# NAVIGATION FLOW
# =========================================================

@allure.feature("BestBuy Navigation Automation")
class TestNavigationFlow:

    logger = LogGen.loggen()

    @pytest.mark.parametrize(
        "tc_id, scenario",
        navigation_data
    )

    @allure.title(
        "Validate Apple Navigation"
    )

    def test_navigation_flow(
            self,
            setup,
            tc_id,
            scenario
    ):

        driver = setup

        home = HomePage(driver)

        # =====================================================
        # OPEN WEBSITE
        # =====================================================

        self.logger.info(
            "Opening BestBuy"
        )

        home.open_bestbuy()

        Screenshot.capture(
            driver,
            f"{tc_id}_01_Homepage"
        )

        assert "Best Buy" in home.get_title()

        self.logger.info(
            "Homepage Validation Passed"
        )

        # =====================================================
        # SELECT COUNTRY
        # =====================================================

        self.logger.info(
            "Selecting Country"
        )

        home.click_country()

        Screenshot.capture(
            driver,
            f"{tc_id}_02_Country"
        )

        assert "bestbuy" in driver.current_url.lower()

        self.logger.info(
            "Country Validation Passed"
        )

        # =====================================================
        # TOP DEALS
        # =====================================================

        self.logger.info(
            "Opening Top Deals"
        )

        home.click_top_deals()

        Screenshot.capture(
            driver,
            f"{tc_id}_03_TopDeals"
        )

        assert "top deals" in driver.page_source.lower()

        self.logger.info(
            "Top Deals Validation Passed"
        )

        # =====================================================
        # APPLE
        # =====================================================

        self.logger.info(
            "Opening Apple Section"
        )

        home.click_apple()

        Screenshot.capture(
            driver,
            f"{tc_id}_04_Apple"
        )

        assert "apple" in driver.page_source.lower()

        self.logger.info(
            "Apple Navigation Validation Passed"
        )

        self.logger.info(
            "TC_08 Passed Successfully"
        )