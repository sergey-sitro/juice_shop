import configparser
import os

from CONSTS import ROOT_DIR

abs_path = os.path.abspath(fr"{ROOT_DIR}/configurations/configuration.ini")
config = configparser.RawConfigParser()
config.read(abs_path)


class ReadConfig:
    @staticmethod
    def get_main_page_url():
        return config.get("URLs", "main_page_url")

    @staticmethod
    def get_login_page_url():
        return config.get("URLs", "login_page_url")

    @staticmethod
    def get_test_email():
        return config.get("Test_Credentials", "email")

    @staticmethod
    def get_test_password():
        return config.get("Test_Credentials", "password")
