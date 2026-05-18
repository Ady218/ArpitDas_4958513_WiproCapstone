import logging
import os


class LogGen:

    @staticmethod
    def loggen():

        if not os.path.exists("logs"):
            os.makedirs("logs")

        logger = logging.getLogger(__name__)

        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(
            "logs/automation.log"
        )

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        return logger