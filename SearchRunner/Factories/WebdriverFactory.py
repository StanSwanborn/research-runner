from typing import List
from selenium import webdriver
from Models.Config.ConfigWebdriverModel import ConfigWebdriverModel

from Models.Enums.WebdriverEnum import WebdriverEnum
from selenium.webdriver.chrome.options import Options

class WebdriverFactory:
    @staticmethod
    def get_driver_for_type(webdriver_model: ConfigWebdriverModel):
        driver_type = webdriver_model.driver_type

        if driver_type == WebdriverEnum.chrome:
            return WebdriverFactory._get_chrome_driver(
                chromedriver_path = webdriver_model.driver_path,
                extension_paths   = webdriver_model.extension_paths)

        elif driver_type == WebdriverEnum.firefox:
            return WebdriverFactory._get_firefox_driver()
    
    @staticmethod
    def _get_chrome_driver(chromedriver_path: str, extension_paths: List[str]):
        chrome_options = Options()

        for ext_path in extension_paths:
            chrome_options.add_extension(ext_path)

        return webdriver.Chrome(
            chrome_options  = chrome_options, 
            executable_path = chromedriver_path)

    @staticmethod
    def _get_firefox_driver():
        pass