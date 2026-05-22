# =========================================================
# allure_logs.py
# =========================================================

import allure


class AllureLogs:

    # =====================================================
    # ATTACH LOGS TO ALLURE REPORT
    # =====================================================

    @staticmethod
    def attach_log(message):

        allure.attach(
            message,
            name="Execution Log",
            attachment_type=
            allure.attachment_type.TEXT
        )