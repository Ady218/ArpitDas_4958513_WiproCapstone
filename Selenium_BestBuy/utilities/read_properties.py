class ReadConfig:

    @staticmethod
    def get_base_url():

        with open(
            "config/config.properties"
        ) as f:

            for line in f:

                if "baseURL" in line:

                    return line.split("=")[1].strip()

    @staticmethod
    def get_browser():

        with open(
            "config/config.properties"
        ) as f:

            for line in f:

                if "browser" in line:

                    return line.split("=")[1].strip()

    @staticmethod
    def get_implicit_wait():

        with open(
            "config/config.properties"
        ) as f:

            for line in f:

                if "implicitWait" in line:

                    return line.split("=")[1].strip()

    @staticmethod
    def get_explicit_wait():

        with open(
            "config/config.properties"
        ) as f:

            for line in f:

                if "explicitWait" in line:

                    return line.split("=")[1].strip()


