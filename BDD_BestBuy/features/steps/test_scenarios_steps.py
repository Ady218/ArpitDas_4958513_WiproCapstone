# =========================================================
# test_scenarios_steps.py
# =========================================================

from behave import *

import allure

from pages.home_page import HomePage
from pages.macbook_page import MacBookPage
from pages.cart_page import CartPage

from utilities.logger import LogGen
from utilities.screenshot import Screenshot
from utilities.excel_utils import ExcelUtils
from utilities.allure_logs import AllureLogs


logger = LogGen.loggen()


# =========================================================
# LOAD POSITIVE DATA
# =========================================================

@given(
    'user loads positive test data "{tc_id}"'
)
@allure.step(
    "Load Positive Test Data"
)
def step_load_positive_data(
        context,
        tc_id
):

    logger.info(
        f"Loading Positive Data: {tc_id}"
    )

    data = ExcelUtils.get_data_by_tc_id(
        "data/testdata.xlsx",
        "PositiveData",
        tc_id
    )

    assert data is not None, (
        f"No Positive Data Found For: {tc_id}"
    )

    context.tc_id = data[0]
    context.processor = data[1]
    context.test_scenario = data[2]

    logger.info(
        f"Positive Data Loaded Successfully: "
        f"{context.tc_id}"
    )

    AllureLogs.attach_log(
        f"Positive Data Loaded Successfully: "
        f"{context.tc_id}"
    )


# =========================================================
# POSITIVE FLOW - OPEN WEBSITE
# =========================================================

@when(
    'user opens BestBuy website for positive flow'
)
@allure.step(
    "Open BestBuy Website For Positive Flow"
)
def step_open_website_positive(context):

    logger.info(
        "Opening BestBuy Website"
    )

    AllureLogs.attach_log(
        "Opening BestBuy Website"
    )

    context.home = HomePage(
        context.driver
    )

    context.home.open_bestbuy()

    Screenshot.capture(
        context.driver,
        f"{context.tc_id}_Homepage"
    )

    assert (
        "Best Buy"
        in
        context.driver.title
    ), (
        "Homepage Validation Failed"
    )

    logger.info(
        "Homepage Opened Successfully"
    )


# =========================================================
# POSITIVE FLOW - SELECT COUNTRY
# =========================================================

@when(
    'user selects country for positive flow'
)
@allure.step(
    "Select Country For Positive Flow"
)
def step_select_country_positive(context):

    logger.info(
        "Selecting Country"
    )

    AllureLogs.attach_log(
        "Selecting Country"
    )

    context.home.click_country()

    Screenshot.capture(
        context.driver,
        f"{context.tc_id}_Country"
    )

    logger.info(
        "Country Selected Successfully"
    )


# =========================================================
# POSITIVE FLOW - TOP DEALS
# =========================================================

@when(
    'user opens Top Deals for positive flow'
)
@allure.step(
    "Open Top Deals For Positive Flow"
)
def step_top_deals_positive(context):

    logger.info(
        "Opening Top Deals"
    )

    AllureLogs.attach_log(
        "Opening Top Deals"
    )

    context.home.click_top_deals()

    Screenshot.capture(
        context.driver,
        f"{context.tc_id}_TopDeals"
    )

    logger.info(
        "Top Deals Opened Successfully"
    )


# =========================================================
# POSITIVE FLOW - APPLE
# =========================================================

@when(
    'user opens Apple section for positive flow'
)
@allure.step(
    "Open Apple Section For Positive Flow"
)
def step_apple_positive(context):

    logger.info(
        "Opening Apple Section"
    )

    AllureLogs.attach_log(
        "Opening Apple Section"
    )

    context.home.click_apple()

    Screenshot.capture(
        context.driver,
        f"{context.tc_id}_Apple"
    )

    logger.info(
        "Apple Section Opened Successfully"
    )


# =========================================================
# POSITIVE FLOW - MACBOOK
# =========================================================

@when(
    'user opens MacBook section for positive flow'
)
@allure.step(
    "Open MacBook Section For Positive Flow"
)
def step_macbook_positive(context):

    logger.info(
        "Opening MacBook Section"
    )

    AllureLogs.attach_log(
        "Opening MacBook Section"
    )

    context.macbook = MacBookPage(
        context.driver
    )

    context.macbook.click_macbook()

    Screenshot.capture(
        context.driver,
        f"{context.tc_id}_MacBook"
    )

    logger.info(
        "MacBook Section Opened Successfully"
    )


# =========================================================
# POSITIVE FLOW - FILTER
# =========================================================

@when(
    'user selects processor filter for positive flow'
)
@allure.step(
    "Select Processor Filter For Positive Flow"
)
def step_filter_positive(context):

    logger.info(
        "Selecting Processor Filter"
    )

    AllureLogs.attach_log(
        "Selecting Processor Filter"
    )

    context.macbook.select_processor_filter()

    Screenshot.capture(
        context.driver,
        f"{context.tc_id}_Filter"
    )

    logger.info(
        "Processor Filter Expanded Successfully"
    )


# =========================================================
# POSITIVE FLOW - PROCESSOR
# =========================================================

@when(
    'user selects processor for positive flow'
)
@allure.step(
    "Select Processor For Positive Flow"
)
def step_processor_positive(context):

    logger.info(
        f"Selecting Processor: "
        f"{context.processor}"
    )

    AllureLogs.attach_log(
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
        f"{context.tc_id}_Processor"
    )

    assert (
        processor_found is True
    ), (
        f"Processor Selection Failed: "
        f"{context.processor}"
    )

    logger.info(
        f"Processor Selected Successfully: "
        f"{context.processor}"
    )


# =========================================================
# POSITIVE VALIDATION
# =========================================================

@then(
    'positive ecommerce validation should pass'
)
@allure.step(
    "Validate Positive Ecommerce Flow"
)
def step_positive_validation(context):

    logger.info(
        "Validating Positive Flow"
    )

    assert (
        context.processor
        in
        context.driver.page_source
    ), (
        "Positive Validation Failed"
    )

    logger.info(
        "Positive Validation Passed"
    )

    AllureLogs.attach_log(
        "Positive Validation Passed"
    )


# =========================================================
# LOAD NEGATIVE DATA
# =========================================================

@given(
    'user loads negative test data "{tc_id}"'
)
@allure.step(
    "Load Negative Test Data"
)
def step_load_negative_data(
        context,
        tc_id
):

    logger.info(
        f"Loading Negative Data: "
        f"{tc_id}"
    )

    data = ExcelUtils.get_data_by_tc_id(
        "data/testdata.xlsx",
        "NegativeData",
        tc_id
    )

    assert data is not None, (
        f"No Negative Data Found: {tc_id}"
    )

    context.tc_id = data[0]
    context.processor = data[1]
    context.test_scenario = data[2]

    logger.info(
        "Negative Data Loaded Successfully"
    )

    AllureLogs.attach_log(
        "Negative Data Loaded Successfully"
    )


# =========================================================
# NEGATIVE FLOW
# =========================================================

@when(
    'user opens BestBuy website for negative flow'
)
def step_open_negative(context):

    context.home = HomePage(
        context.driver
    )

    context.home.open_bestbuy()

    Screenshot.capture(
        context.driver,
        f"{context.tc_id}_Homepage"
    )


@when(
    'user selects country for negative flow'
)
def step_country_negative(context):

    context.home.click_country()

    Screenshot.capture(
        context.driver,
        f"{context.tc_id}_Country"
    )


@when(
    'user opens Top Deals for negative flow'
)
def step_topdeals_negative(context):

    context.home.click_top_deals()

    Screenshot.capture(
        context.driver,
        f"{context.tc_id}_TopDeals"
    )


@when(
    'user opens Apple section for negative flow'
)
def step_apple_negative(context):

    context.home.click_apple()

    Screenshot.capture(
        context.driver,
        f"{context.tc_id}_Apple"
    )


@when(
    'user opens MacBook section for negative flow'
)
def step_macbook_negative(context):

    context.macbook = MacBookPage(
        context.driver
    )

    context.macbook.click_macbook()

    Screenshot.capture(
        context.driver,
        f"{context.tc_id}_MacBook"
    )


@when(
    'user selects processor filter for negative flow'
)
def step_filter_negative(context):

    context.macbook.select_processor_filter()

    Screenshot.capture(
        context.driver,
        f"{context.tc_id}_Filter"
    )


@when(
    'user selects invalid processor'
)
def step_invalid_processor(context):

    context.processor_found = (
        context.macbook.select_processor(
            context.processor
        )
    )

    Screenshot.capture(
        context.driver,
        f"{context.tc_id}_InvalidProcessor"
    )


@then(
    'negative ecommerce validation should pass'
)
def step_negative_validation(context):

    assert (
        context.processor_found
        is
        False
    ), (
        "Negative Validation Failed"
    )

    logger.info(
        "Negative Validation Passed"
    )

    AllureLogs.attach_log(
        "Negative Validation Passed"
    )

# =========================================================
# LOAD CHECKOUT NEGATIVE DATA
# =========================================================

@given(
    'user loads checkout negative data "{tc_id}"'
)
@allure.step(
    "Load Checkout Negative Data"
)
def step_load_checkout_negative_data(
        context,
        tc_id
):

    logger.info(
        f"Loading Checkout Negative Data: "
        f"{tc_id}"
    )

    AllureLogs.attach_log(
        f"Loading Checkout Negative Data: "
        f"{tc_id}"
    )

    data = ExcelUtils.get_data_by_tc_id(
        "data/testdata.xlsx",
        "CheckoutNegativeData",
        tc_id
    )

    context.tc_id = data[0]
    context.email = data[1]
    context.test_scenario = data[2]

    logger.info(
        "Checkout Negative Data Loaded Successfully"
    )

    AllureLogs.attach_log(
        "Checkout Negative Data Loaded Successfully"
    )


# =========================================================
# CHECKOUT FLOW - OPEN WEBSITE
# =========================================================

@when(
    'user opens BestBuy website for checkout flow'
)
@allure.step(
    "Open BestBuy Website For Checkout Flow"
)
def step_checkout_open_website(context):

    logger.info(
        "Opening BestBuy Website"
    )

    AllureLogs.attach_log(
        "Opening BestBuy Website"
    )

    context.home = HomePage(
        context.driver
    )

    context.home.open_bestbuy()

    Screenshot.capture(
        context.driver,
        f"{context.tc_id}_Homepage"
    )

    logger.info(
        "Homepage Opened Successfully"
    )


# =========================================================
# CHECKOUT FLOW - COUNTRY
# =========================================================

@when(
    'user selects country for checkout flow'
)
@allure.step(
    "Select Country For Checkout Flow"
)
def step_checkout_country(context):

    logger.info(
        "Selecting Country"
    )

    AllureLogs.attach_log(
        "Selecting Country"
    )

    context.home.click_country()

    Screenshot.capture(
        context.driver,
        f"{context.tc_id}_Country"
    )

    logger.info(
        "Country Selected Successfully"
    )


# =========================================================
# CHECKOUT FLOW - TOP DEALS
# =========================================================

@when(
    'user opens Top Deals for checkout flow'
)
@allure.step(
    "Open Top Deals For Checkout Flow"
)
def step_checkout_topdeals(context):

    logger.info(
        "Opening Top Deals"
    )

    AllureLogs.attach_log(
        "Opening Top Deals"
    )

    context.home.click_top_deals()

    Screenshot.capture(
        context.driver,
        f"{context.tc_id}_TopDeals"
    )

    logger.info(
        "Top Deals Opened Successfully"
    )


# =========================================================
# CHECKOUT FLOW - APPLE
# =========================================================

@when(
    'user opens Apple section for checkout flow'
)
@allure.step(
    "Open Apple Section For Checkout Flow"
)
def step_checkout_apple(context):

    logger.info(
        "Opening Apple Section"
    )

    AllureLogs.attach_log(
        "Opening Apple Section"
    )

    context.home.click_apple()

    Screenshot.capture(
        context.driver,
        f"{context.tc_id}_Apple"
    )

    logger.info(
        "Apple Section Opened Successfully"
    )


# =========================================================
# CHECKOUT FLOW - MACBOOK
# =========================================================

@when(
    'user opens MacBook section for checkout flow'
)
@allure.step(
    "Open MacBook Section For Checkout Flow"
)
def step_checkout_macbook(context):

    logger.info(
        "Opening MacBook Section"
    )

    AllureLogs.attach_log(
        "Opening MacBook Section"
    )

    context.macbook = MacBookPage(
        context.driver
    )

    context.macbook.click_macbook()

    Screenshot.capture(
        context.driver,
        f"{context.tc_id}_MacBook"
    )

    logger.info(
        "MacBook Section Opened Successfully"
    )


# =========================================================
# CHECKOUT FLOW - FILTER
# =========================================================

@when(
    'user selects processor filter for checkout flow'
)
@allure.step(
    "Select Processor Filter For Checkout Flow"
)
def step_checkout_filter(context):

    logger.info(
        "Selecting Processor Filter"
    )

    AllureLogs.attach_log(
        "Selecting Processor Filter"
    )

    context.macbook.select_processor_filter()

    Screenshot.capture(
        context.driver,
        f"{context.tc_id}_Filter"
    )

    logger.info(
        "Processor Filter Expanded Successfully"
    )


# =========================================================
# CHECKOUT FLOW - PROCESSOR
# =========================================================

@when(
    'user selects processor for checkout flow'
)
@allure.step(
    "Select Processor For Checkout Flow"
)
def step_checkout_processor(context):

    logger.info(
        "Selecting Processor"
    )

    AllureLogs.attach_log(
        "Selecting Processor"
    )

    context.macbook.select_processor(
        "Apple M4"
    )

    Screenshot.capture(
        context.driver,
        f"{context.tc_id}_Processor"
    )

    logger.info(
        "Processor Selected Successfully"
    )


# =========================================================
# CHECKOUT FLOW - ADD TO CART
# =========================================================

@when(
    'user adds product to cart for checkout flow'
)
@allure.step(
    "Add Product To Cart For Checkout Flow"
)
def step_checkout_add_cart(context):

    logger.info(
        "Adding Product To Cart"
    )

    AllureLogs.attach_log(
        "Adding Product To Cart"
    )

    context.macbook.click_listing_add_to_cart(
        "Apple M4"
    )

    Screenshot.capture(
        context.driver,
        f"{context.tc_id}_AddToCart"
    )

    logger.info(
        "Product Added To Cart Successfully"
    )


# =========================================================
# CHECKOUT FLOW - OPEN CART
# =========================================================

@when(
    'user opens cart for checkout flow'
)
@allure.step(
    "Open Cart For Checkout Flow"
)
def step_checkout_cart(context):

    logger.info(
        "Opening Cart"
    )

    AllureLogs.attach_log(
        "Opening Cart"
    )

    context.macbook.click_go_to_cart()

    context.cart = CartPage(
        context.driver
    )

    Screenshot.capture(
        context.driver,
        f"{context.tc_id}_Cart"
    )

    logger.info(
        "Cart Opened Successfully"
    )


# =========================================================
# CHECKOUT FLOW - CHECKOUT
# =========================================================

@when(
    'user proceeds to checkout for checkout flow'
)
@allure.step(
    "Proceed To Checkout For Checkout Flow"
)
def step_checkout_checkout(context):

    logger.info(
        "Proceeding To Checkout"
    )

    AllureLogs.attach_log(
        "Proceeding To Checkout"
    )

    context.cart.click_checkout()

    Screenshot.capture(
        context.driver,
        f"{context.tc_id}_Checkout"
    )

    logger.info(
        "Checkout Page Opened Successfully"
    )


# =========================================================
# CHECKOUT FLOW - INVALID EMAIL
# =========================================================

@when(
    'user enters invalid email'
)
@allure.step(
    "Enter Invalid Email"
)
def step_invalid_email(context):

    logger.info(
        "Entering Invalid Email"
    )

    AllureLogs.attach_log(
        "Entering Invalid Email"
    )

    context.cart.enter_invalid_email(
        context.email
    )

    context.cart.click_continue()

    Screenshot.capture(
        context.driver,
        f"{context.tc_id}_InvalidEmail"
    )

    logger.info(
        "Invalid Email Entered Successfully"
    )


# =========================================================
# CHECKOUT NEGATIVE VALIDATION
# =========================================================

@then(
    'checkout negative validation should pass'
)
@allure.step(
    "Validate Checkout Negative Flow"
)
def step_checkout_negative_validation(context):

    logger.info(
        "Validating Checkout Negative Flow"
    )

    assert (
        context.cart.verify_invalid_email_error()
        is
        True
    ), (
        "Checkout Negative Validation Failed"
    )

    logger.info(
        "Checkout Negative Validation Passed"
    )

    AllureLogs.attach_log(
        "Checkout Negative Validation Passed"
    )


# =========================================================
# LOAD NAVIGATION DATA
# =========================================================

@given(
    'user loads navigation data "{tc_id}"'
)
@allure.step(
    "Load Navigation Data"
)
def step_load_navigation_data(
        context,
        tc_id
):

    logger.info(
        f"Loading Navigation Data: "
        f"{tc_id}"
    )

    AllureLogs.attach_log(
        f"Loading Navigation Data: "
        f"{tc_id}"
    )

    data = ExcelUtils.get_data_by_tc_id(
        "data/testdata.xlsx",
        "NavigationData",
        tc_id
    )

    context.tc_id = data[0]
    context.test_scenario = data[1]

    logger.info(
        "Navigation Data Loaded Successfully"
    )

    AllureLogs.attach_log(
        "Navigation Data Loaded Successfully"
    )


# =========================================================
# NAVIGATION FLOW
# =========================================================

@when(
    'user opens BestBuy website for navigation flow'
)
@allure.step(
    "Open BestBuy Website For Navigation Flow"
)
def step_navigation_open(context):

    logger.info(
        "Opening BestBuy Website"
    )

    AllureLogs.attach_log(
        "Opening BestBuy Website"
    )

    context.home = HomePage(
        context.driver
    )

    context.home.open_bestbuy()

    Screenshot.capture(
        context.driver,
        f"{context.tc_id}_Homepage"
    )

    logger.info(
        "Homepage Opened Successfully"
    )


@when(
    'user selects country for navigation flow'
)
@allure.step(
    "Select Country For Navigation Flow"
)
def step_navigation_country(context):

    logger.info(
        "Selecting Country"
    )

    AllureLogs.attach_log(
        "Selecting Country"
    )

    context.home.click_country()

    Screenshot.capture(
        context.driver,
        f"{context.tc_id}_Country"
    )

    logger.info(
        "Country Selected Successfully"
    )


@when(
    'user opens Top Deals for navigation flow'
)
@allure.step(
    "Open Top Deals For Navigation Flow"
)
def step_navigation_topdeals(context):

    logger.info(
        "Opening Top Deals"
    )

    AllureLogs.attach_log(
        "Opening Top Deals"
    )

    context.home.click_top_deals()

    Screenshot.capture(
        context.driver,
        f"{context.tc_id}_TopDeals"
    )

    logger.info(
        "Top Deals Opened Successfully"
    )


@when(
    'user opens Apple section for navigation flow'
)
@allure.step(
    "Open Apple Section For Navigation Flow"
)
def step_navigation_apple(context):

    logger.info(
        "Opening Apple Section"
    )

    AllureLogs.attach_log(
        "Opening Apple Section"
    )

    context.home.click_apple()

    Screenshot.capture(
        context.driver,
        f"{context.tc_id}_Apple"
    )

    logger.info(
        "Apple Section Opened Successfully"
    )


@then(
    'navigation validation should pass'
)
@allure.step(
    "Validate Navigation Flow"
)
def step_navigation_validation(context):

    logger.info(
        "Validating Navigation Flow"
    )

    assert (
        "apple"
        in
        context.driver.page_source.lower()
    ), (
        "Navigation Validation Failed"
    )

    logger.info(
        "Navigation Validation Passed"
    )

    AllureLogs.attach_log(
        "Navigation Validation Passed"
    )