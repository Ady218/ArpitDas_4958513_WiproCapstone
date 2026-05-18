from selenium.webdriver.common.by import By


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