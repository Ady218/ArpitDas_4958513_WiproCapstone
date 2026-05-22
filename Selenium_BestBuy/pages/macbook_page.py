import time

# from selenium.webdriver.common.keys import Keys

# from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class MacBookPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 6)

    def click_macbook(self):
        macbook = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//a[contains(@href,'macbook')]"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            macbook
        )

        time.sleep(1.3)

        self.driver.execute_script(
            "arguments[0].click();",
            macbook
        )

        time.sleep(1.3)

    def select_processor_filter(self):
        self.driver.execute_script(
            "window.scrollBy(0,1200)"
        )

        time.sleep(4)

        processor = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//*[contains(text(),'Processor Model')]"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            processor
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            processor
        )

        time.sleep(3)

    def select_processor(self, processor):

        try:

            filter_panel = self.wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//div[contains(@class,'facet')]"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight",
                filter_panel
            )

            time.sleep(3)

            processor_checkbox = self.wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        f"//div[@aria-label='{processor}']"
                    )
                )
            )

            self.driver.execute_script(
                "arguments[0].scrollIntoView();",
                processor_checkbox
            )

            time.sleep(2)

            self.driver.execute_script(
                "arguments[0].click();",
                processor_checkbox
            )

            

            time.sleep(2)

            self.driver.refresh()

            self.wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//button[contains(@data-testid,'add-to-cart')]"
                    )
                )
            )

            return True

        except:

            return False

    def click_listing_add_to_cart(self, processor):

        if processor == "Apple M4":

            add_to_cart_xpath = (
                "//button[@data-testid='plp-add-to-cart-6571025']"
            )

        elif processor == "Apple M3":

            add_to_cart_xpath = (
                "//button[@data-testid='plp-add-to-cart-6598900']"
            )

        else:

            return False

        add_to_cart = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    add_to_cart_xpath
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            add_to_cart
        )

        time.sleep(1.5)

        add_to_cart.click()

        time.sleep(2.2)

        return True

    def click_go_to_cart(self):
        go_to_cart = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "(//a[@data-cy='go-to-cart'])[2]"
                )
            )
        )

        time.sleep(2)

        go_to_cart.click()

        time.sleep(3)