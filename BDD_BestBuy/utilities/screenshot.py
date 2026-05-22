# =========================================================
# screenshot.py
# =========================================================

import os

from datetime import datetime

import allure


class Screenshot:

    # =====================================================
    # CAPTURE SCREENSHOT
    # =====================================================

    @staticmethod
    def capture(
            driver,
            screenshot_name="Screenshot"
    ):

        screenshot_dir = (
            "reports/screenshots"
        )

        # =================================================
        # CREATE FOLDER IF NOT EXISTS
        # =================================================

        if not os.path.exists(
                screenshot_dir
        ):

            os.makedirs(
                screenshot_dir
            )

        # =================================================
        # TIMESTAMP
        # =================================================

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        # =================================================
        # FINAL SCREENSHOT PATH
        # =================================================

        screenshot_path = (
            f"{screenshot_dir}/"
            f"{screenshot_name}_"
            f"{timestamp}.png"
        )

        # =================================================
        # SAVE SCREENSHOT
        # =================================================

        driver.save_screenshot(
            screenshot_path
        )

        # =================================================
        # ATTACH SCREENSHOT TO ALLURE
        # =================================================

        allure.attach(
            driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=
            allure.attachment_type.PNG
        )