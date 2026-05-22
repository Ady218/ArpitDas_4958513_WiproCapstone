# =========================================================
# read_properties.py
# =========================================================

from configparser import ConfigParser


config = ConfigParser()

config.read(
    "config/config.ini"
)


class ReadConfig:

    # =====================================================
    # BASE URL
    # =====================================================

    @staticmethod
    def get_base_url():

        return config.get(
            'common info',
            'baseURL'
        )

    # =====================================================
    # BROWSER
    # =====================================================

    @staticmethod
    def get_browser():

        return config.get(
            'common info',
            'browser'
        )

    # =====================================================
    # IMPLICIT WAIT
    # =====================================================

    @staticmethod
    def get_implicit_wait():

        return config.get(
            'common info',
            'implicitWait'
        )

    # =====================================================
    # EXPLICIT WAIT
    # =====================================================

    @staticmethod
    def get_explicit_wait():

        return config.get(
            'common info',
            'explicitWait'
        )