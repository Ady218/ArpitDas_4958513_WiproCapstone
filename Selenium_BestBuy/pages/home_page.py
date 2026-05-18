import time

from utilities.read_properties import ReadConfig

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 30)

    def open_bestbuy(self):
        self.driver.get(
            ReadConfig.get_base_url()
        )

    def get_title(self):
        return self.driver.title

    def click_country(self):
        usa_button = self.driver.find_element(
            By.XPATH,
            "//img[@alt='United States']"
        )
        usa_button.click()

    def click_top_deals(self):

        top_deals = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//*[contains(text(),'Top Deals')]"
                )
            )
        )

        top_deals.click()

        time.sleep(3)

    def click_apple(self):

        apple = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//*[contains(text(),'Apple')]"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            apple
        )

        time.sleep(3)