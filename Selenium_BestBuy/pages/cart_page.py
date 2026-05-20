from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):

        self.driver = driver

    def get_title(self):

        return self.driver.title

    def verify_cart_item(self):
        return "MacBook" in self.driver.page_source

    def click_checkout(self):
        checkout = self.driver.find_element(
            By.XPATH,
            "//button[contains(text(),'Checkout')]"
        )

        checkout.click()

    def enter_invalid_email(self, email):
        email_box = WebDriverWait(
            self.driver,
            20
        ).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//input[@type='email' and @name='fld-e']"
                )
            )
        )

        email_box.clear()

        email_box.send_keys(email)

    def verify_invalid_email_error(self):
        return (
                "valid email" in self.driver.page_source.lower()
        )

    def click_continue(self):
        continue_button = WebDriverWait(
            self.driver,
            20
        ).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[@data-track='Sign In: Continue']"
                )
            )
        )

        continue_button.click()