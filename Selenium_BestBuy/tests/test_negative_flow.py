import pytest
import allure
import os

from pages.home_page import HomePage
from pages.macbook_page import MacBookPage

from utilities.logger import LogGen
from utilities.excel_utils import ExcelUtils


path = "data/testdata.xlsx"

test_data = ExcelUtils.get_all_data(
    path,
    "NegativeData"
)


@allure.feature("BestBuy Negative Automation")
class TestNegativeFlow:

    logger = LogGen.loggen()

    @pytest.mark.parametrize(
        "tc_id, processor, scenario",
        test_data
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