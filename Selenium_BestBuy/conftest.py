# =========================================================
# conftest.py
# =========================================================

import pytest
import os
import threading
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


# =========================================================
# POPUP HANDLER THREAD
# =========================================================

def auto_close_popup(driver):

    try:

        popup = WebDriverWait(
            driver,
            3
        ).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//button[contains(text(),'No, Thanks')]"
                )
            )
        )

        if popup.is_displayed():

            driver.execute_script(
                "arguments[0].click();",
                popup
            )

            print(
                "=========== POPUP CLOSED ==========="
            )

    except:

        pass
# =========================================================
# FIXTURE
# =========================================================

@pytest.fixture(scope="function")
def setup():

    options = webdriver.ChromeOptions()

    # =====================================================
    # CHROME OPTIONS
    # =====================================================

    options.add_argument(
        "--start-maximized"
    )

    options.add_argument(
        "--disable-notifications"
    )

    options.add_argument(
        "--disable-infobars"
    )

    options.add_argument(
        "--disable-extensions"
    )

    options.add_argument(
        "--disable-popup-blocking"
    )

    options.add_argument(
        "--disable-blink-features=AutomationControlled"
    )

    # =====================================================
    # ANTI BOT DETECTION
    # =====================================================

    options.add_experimental_option(
        "excludeSwitches",
        ["enable-automation"]
    )

    options.add_experimental_option(
        "useAutomationExtension",
        False
    )

    # ========================= DRIVER ============================

    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        ),
        options=options
    )

    # =====================================================
    # WAIT
    # =====================================================

    driver.implicitly_wait(5)

    # =====================================================
    # REMOVE SELENIUM DETECTION
    # =====================================================

    driver.execute_script(
        "Object.defineProperty("
        "navigator, "
        "'webdriver', "
        "{get: () => undefined}"
        ")"
    )

    # =====================================================
    # START POPUP HANDLER THREAD
    # =====================================================

    popup_thread = threading.Thread(
        target=auto_close_popup,
        args=(driver,),
        daemon=True
    )

    popup_thread.start()

    yield driver

    # =====================================================
    # CLOSE DRIVER
    # =====================================================

    driver.quit()


# =========================================================
# AUTOMATIC ALLURE REPORT OPEN
# =========================================================

def pytest_unconfigure(config):

    print(
        "\n=========================================="
    )

    print(
        "TESTS COMPLETED SUCCESSFULLY"
    )

    print(
        "OPENING ALLURE REPORT..."
    )

    print(
        "==========================================\n"
    )

    os.system(
        "allure serve reports/allure-results"
    )