from utilities.read_properties import ReadConfig

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            30
        )

    # =====================================================
    # OPEN WEBSITE
    # =====================================================

    def open_bestbuy(self):

        self.driver.get(
            ReadConfig.get_base_url()
        )

    # =====================================================
    # TITLE
    # =====================================================

    def get_title(self):

        return self.driver.title

    # =====================================================
    # COUNTRY
    # =====================================================

    def click_country(self):

        usa_button = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//img[@alt='United States']"
                )
            )
        )

        # Smooth Scroll
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior:'smooth', block:'center'});",
            usa_button
        )

        # Wait Clickable
        self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//img[@alt='United States']"
                )
            )
        )

        # JS Click
        self.driver.execute_script(
            "arguments[0].click();",
            usa_button
        )

    # =====================================================
    # TOP DEALS
    # =====================================================

    def click_top_deals(self):

        top_deals = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//*[contains(text(),'Top Deals')]"
                )
            )
        )

        # Smooth Scroll
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior:'smooth', block:'center'});",
            top_deals
        )

        # Wait Clickable
        self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//*[contains(text(),'Top Deals')]"
                )
            )
        )

        # JS Click
        self.driver.execute_script(
            "arguments[0].click();",
            top_deals
        )

    # =====================================================
    # APPLE
    # =====================================================

    def click_apple(self):

        apple = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//*[contains(text(),'Apple')]"
                )
            )
        )

        # Smooth Scroll
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior:'smooth', block:'center'});",
            apple
        )

        # Wait Clickable
        self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//*[contains(text(),'Apple')]"
                )
            )
        )

        # JS Click
        self.driver.execute_script(
            "arguments[0].click();",
            apple
        )