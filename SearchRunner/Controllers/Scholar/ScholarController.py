import time
import pyautogui
from selenium import webdriver
from Models.Config.ConfigModel import ConfigModel
from Procedures.ScreenProcedure import ScreenProcedure
from Factories.WebdriverFactory import WebdriverFactory

class ScholarController():
    _driver: webdriver
    _config_model: ConfigModel

    def __init__(self, config_model: ConfigModel):
        self._config_model = config_model
        self._driver = WebdriverFactory.get_driver_for_type(
            config_model.webdriver_model
        )

    def open_and_search(self):
        self._driver.get('https://scholar.google.com')
        
        pos = None
        while pos is None:
            pos = pyautogui.locateOnScreen("./Assets/images/scholar_search_bar.png")

        fixed_pos = ScreenProcedure.pyautogui_position_fix_and_center(pos)

        #pyautogui.click(fixed_pos[0], fixed_pos[1], clicks=1, interval=0.0, button="left")
        # Scholar opens with cursor focused on textbox, just write, hit enter and extract NR of results.
        pyautogui.write(self._config_model.search_string)
        time.sleep(10)
        
        