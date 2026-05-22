# =========================================================
# environment.py
# =========================================================

import os
import threading

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

    except Exception:

        pass


# =========================================================
# BEFORE SCENARIO
# =========================================================

def before_scenario(
        context,
        scenario
):

    print(
        f"\n========== STARTING: "
        f"{scenario.name} =========="
    )

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

    # =====================================================
    # DRIVER INITIALIZATION
    # =====================================================

    context.driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        ),
        options=options
    )

    # =====================================================
    # IMPLICIT WAIT
    # =====================================================

    context.driver.implicitly_wait(5)

    # =====================================================
    # REMOVE SELENIUM DETECTION
    # =====================================================

    context.driver.execute_script(
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
        args=(context.driver,),
        daemon=True
    )

    popup_thread.start()


# =========================================================
# AFTER SCENARIO
# =========================================================

def after_scenario(
        context,
        scenario
):

    # =====================================================
    # FAILURE SCREENSHOT
    # =====================================================

    if scenario.status == "failed":

        screenshot_dir = (
            "reports/screenshots"
        )

        if not os.path.exists(
                screenshot_dir
        ):

            os.makedirs(
                screenshot_dir
            )

        screenshot_path = (
            f"{screenshot_dir}/"
            f"{scenario.name}.png"
        )

        context.driver.save_screenshot(
            screenshot_path
        )

        print(
            f"Screenshot Saved: "
            f"{screenshot_path}"
        )

    # =====================================================
    # CLOSE DRIVER
    # =====================================================

    context.driver.quit()

    print(
        f"========== COMPLETED: "
        f"{scenario.name} ==========\n"
    )


# =========================================================
# AUTOMATIC ALLURE REPORT GENERATION
# =========================================================

def after_all(context):

    print(
        "\n=========================================="
    )

    print(
        "BDD EXECUTION COMPLETED SUCCESSFULLY"
    )

    print(
        "GENERATING ALLURE REPORT..."
    )

    print(
        "==========================================\n"
    )

    # =====================================================
    # GENERATE PERMANENT REPORT
    # =====================================================

    os.system(
        "allure generate reports/allure-results "
        "-o reports/allure-report --clean"
    )

    # =====================================================
    # OPEN ALLURE REPORT
    # =====================================================

    os.system(
        "allure open reports/allure-report"
    )