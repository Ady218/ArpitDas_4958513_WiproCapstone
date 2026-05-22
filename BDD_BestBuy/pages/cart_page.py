from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):

        self.driver = driver

    # =====================================================
    # TITLE
    # =====================================================

    def get_title(self):

        return self.driver.title

    # =====================================================
    # VERIFY CART ITEM
    # =====================================================

    def verify_cart_item(self):

        return "MacBook" in self.driver.page_source

    # =====================================================
    # CHECKOUT
    # =====================================================

    def click_checkout(self):
        checkout = WebDriverWait(
            self.driver,
            20
        ).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//button[contains(text(),'Checkout')]"
                )
            )
        )

        # Smooth Scroll
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior:'smooth', block:'center'});",
            checkout
        )

        # Wait Clickable
        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(text(),'Checkout')]"
                )
            )
        )

        # JS Click
        self.driver.execute_script(
            "arguments[0].click();",
            checkout
        )

        # =====================================================
        # WAIT FOR CHECKOUT PAGE FULLY LOAD
        # =====================================================

        # Wait Email Field Visible
        WebDriverWait(
            self.driver,
            20
        ).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//input[@type='email']"
                )
            )
        )

        # Wait Continue Button Visible
        WebDriverWait(
            self.driver,
            20
        ).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//button[@data-track='Sign In: Continue']"
                )
            )
        )

        # Wait Full DOM Load
        WebDriverWait(
            self.driver,
            20
        ).until(
            lambda driver:
            driver.execute_script(
                "return document.readyState"
            ) == "complete"
        )

    # =====================================================
    # ENTER INVALID EMAIL
    # =====================================================

    def enter_invalid_email(
            self,
            email
    ):

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

        # Smooth Scroll
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior:'smooth', block:'center'});",
            email_box
        )

        email_box.clear()

        email_box.send_keys(email)

    # =====================================================
    # INVALID EMAIL ERROR
    # =====================================================

    def verify_invalid_email_error(self):

        return (
                "valid email"
                in
                self.driver.page_source.lower()
        )

    # =====================================================
    # CLICK CONTINUE
    # =====================================================

    def click_continue(self):

        continue_button = WebDriverWait(
            self.driver,
            20
        ).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//button[@data-track='Sign In: Continue']"
                )
            )
        )

        # Smooth Scroll
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior:'smooth', block:'center'});",
            continue_button
        )

        # Wait Clickable
        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[@data-track='Sign In: Continue']"
                )
            )
        )

        # JS Click
        self.driver.execute_script(
            "arguments[0].click();",
            continue_button
        )