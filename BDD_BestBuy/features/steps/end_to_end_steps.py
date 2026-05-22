# =========================================================
# end_to_end_steps.py
# =========================================================

from behave import *

import allure

from selenium.webdriver.common.by import By

from pages.home_page import HomePage

from pages.macbook_page import MacBookPage

from pages.cart_page import CartPage

from utilities.logger import LogGen

from utilities.screenshot import Screenshot

from utilities.excel_utils import ExcelUtils

from utilities.allure_logs import AllureLogs


logger = LogGen.loggen()


# =========================================================
# LOAD END TO END TEST DATA
# =========================================================

@given(
    'user loads end to end test data'
)
@allure.step(
    "Load End To End Test Data"
)
def step_load_e2e_data(context):

    logger.info(
        "Loading End To End Test Data"
    )

    data = ExcelUtils.get_data_by_tc_id(
        "data/testdata.xlsx",
        "PositiveData",
        "TC_03"
    )

    assert (
        data is not None
    ), (
        "End To End Test Data Not Found"
    )

    context.tc_id = data[0]

    context.processor = data[1]

    context.test_scenario = data[2]

    logger.info(
        f"Loaded Test Data Successfully: "
        f"{context.tc_id}"
    )

    AllureLogs.attach_log(
        f"Loaded End To End Test Data: "
        f"{context.tc_id}"
    )


# =========================================================
# OPEN WEBSITE
# =========================================================

@given(
    'user opens BestBuy website'
)
@allure.step(
    "Open BestBuy Website"
)
def step_open_website(context):

    logger.info(
        "Opening BestBuy Website"
    )

    context.home = HomePage(
        context.driver
    )

    context.home.open_bestbuy()

    Screenshot.capture(
        context.driver,
        "01_Homepage"
    )

    assert (
        "Best Buy"
        in
        context.home.get_title()
    ), (
        "Homepage Title Validation Failed"
    )

    logger.info(
        "Homepage Opened Successfully"
    )

    AllureLogs.attach_log(
        "Homepage Opened Successfully"
    )


# =========================================================
# SELECT COUNTRY
# =========================================================

@when(
    'user selects country'
)
@allure.step(
    "Select Country"
)
def step_select_country(context):

    logger.info(
        "Selecting Country"
    )

    context.home.click_country()

    Screenshot.capture(
        context.driver,
        "02_Country_Selected"
    )

    assert (
        "bestbuy"
        in
        context.driver.current_url.lower()
    ), (
        "Country Selection Failed"
    )

    logger.info(
        "Country Selected Successfully"
    )

    AllureLogs.attach_log(
        "Country Selected Successfully"
    )


# =========================================================
# OPEN TOP DEALS
# =========================================================

@when(
    'user opens Top Deals'
)
@allure.step(
    "Open Top Deals"
)
def step_open_top_deals(context):

    logger.info(
        "Opening Top Deals"
    )

    context.home.click_top_deals()

    Screenshot.capture(
        context.driver,
        "03_Top_Deals"
    )

    assert (
        "deals"
        in
        context.driver.page_source.lower()
    ), (
        "Top Deals Validation Failed"
    )

    logger.info(
        "Top Deals Opened Successfully"
    )

    AllureLogs.attach_log(
        "Top Deals Opened Successfully"
    )


# =========================================================
# OPEN APPLE SECTION
# =========================================================

@when(
    'user opens Apple section'
)
@allure.step(
    "Open Apple Section"
)
def step_open_apple(context):

    logger.info(
        "Opening Apple Section"
    )

    context.home.click_apple()

    Screenshot.capture(
        context.driver,
        "04_Apple_Page"
    )

    assert (
        "apple"
        in
        context.driver.page_source.lower()
    ), (
        "Apple Page Validation Failed"
    )

    logger.info(
        "Apple Section Opened Successfully"
    )

    AllureLogs.attach_log(
        "Apple Section Opened Successfully"
    )


# =========================================================
# OPEN MACBOOK SECTION
# =========================================================

@when(
    'user opens MacBook section'
)
@allure.step(
    "Open MacBook Section"
)
def step_open_macbook(context):

    logger.info(
        "Opening MacBook Section"
    )

    context.macbook = MacBookPage(
        context.driver
    )

    context.macbook.click_macbook()

    Screenshot.capture(
        context.driver,
        "05_MacBook_Page"
    )

    assert (
        "macbook"
        in
        context.driver.page_source.lower()
    ), (
        "MacBook Navigation Failed"
    )

    logger.info(
        "MacBook Page Opened Successfully"
    )

    AllureLogs.attach_log(
        "MacBook Page Opened Successfully"
    )


# =========================================================
# SELECT PROCESSOR FILTER
# =========================================================

@when(
    'user selects processor filter'
)
@allure.step(
    "Select Processor Filter"
)
def step_select_processor_filter(context):

    logger.info(
        "Selecting Processor Filter"
    )

    context.macbook.select_processor_filter()

    Screenshot.capture(
        context.driver,
        "06_Processor_Filter"
    )

    logger.info(
        "Processor Filter Expanded Successfully"
    )

    AllureLogs.attach_log(
        "Processor Filter Expanded Successfully"
    )


# =========================================================
# SELECT PROCESSOR FROM EXCEL
# =========================================================

@when(
    'user selects processor from excel data'
)
@allure.step(
    "Select Processor From Excel Data"
)
def step_select_processor(context):

    logger.info(
        f"Selecting Processor: "
        f"{context.processor}"
    )

    processor_found = (
        context.macbook.select_processor(
            context.processor
        )
    )

    Screenshot.capture(
        context.driver,
        "07_Processor_Selected"
    )

    assert (
        processor_found
        is
        True
    ), (
        f"Processor Selection Failed: "
        f"{context.processor}"
    )

    logger.info(
        f"Processor Selected Successfully: "
        f"{context.processor}"
    )

    AllureLogs.attach_log(
        f"Processor Selected Successfully: "
        f"{context.processor}"
    )


# =========================================================
# ADD PRODUCT TO CART
# =========================================================

@when(
    'user adds product to cart'
)
@allure.step(
    "Add Product To Cart"
)
def step_add_product_to_cart(context):

    logger.info(
        "Adding Product To Cart"
    )

    add_to_cart_status = (
        context.macbook.click_listing_add_to_cart(
            context.processor
        )
    )

    Screenshot.capture(
        context.driver,
        "08_Add_To_Cart"
    )

    assert (
        add_to_cart_status
        is
        True
    ), (
        "Add To Cart Failed"
    )

    logger.info(
        "Product Added To Cart Successfully"
    )

    AllureLogs.attach_log(
        "Product Added To Cart Successfully"
    )


# =========================================================
# OPEN CART
# =========================================================

@when(
    'user opens cart'
)
@allure.step(
    "Open Cart"
)
def step_open_cart(context):

    logger.info(
        "Opening Cart"
    )

    context.macbook.click_go_to_cart()

    context.cart = CartPage(
        context.driver
    )

    Screenshot.capture(
        context.driver,
        "09_Cart_Page"
    )

    cart_validation = (
        context.cart.verify_cart_item()
    )

    assert (
        cart_validation
        is
        True
    ), (
        "Cart Validation Failed"
    )

    logger.info(
        "Cart Validation Passed"
    )

    AllureLogs.attach_log(
        "Cart Validation Passed"
    )


# =========================================================
# PROCEED TO CHECKOUT
# =========================================================

@when(
    'user proceeds to checkout'
)
@allure.step(
    "Proceed To Checkout"
)
def step_proceed_checkout(context):

    logger.info(
        "Proceeding To Checkout"
    )

    context.cart.click_checkout()

    Screenshot.capture(
        context.driver,
        "10_Checkout_Page"
    )

    logger.info(
        "Checkout Page Opened Successfully"
    )

    AllureLogs.attach_log(
        "Checkout Page Opened Successfully"
    )


# =========================================================
# CHECKOUT VALIDATION
# =========================================================

@then(
    'checkout page should open successfully'
)
@allure.step(
    "Validate Checkout Page"
)
def step_validate_checkout(context):

    logger.info(
        "Validating Checkout Page"
    )

    email_box = context.driver.find_element(
        By.XPATH,
        "//input[@type='email']"
    )

    assert (
        email_box.is_displayed()
    ), (
        "Checkout Email Field Validation Failed"
    )

    logger.info(
        "Checkout Validation Passed"
    )

    AllureLogs.attach_log(
        "Checkout Validation Passed"
    )