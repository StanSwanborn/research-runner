import sys
import json
from Models.Enums.WebdriverEnum import WebdriverEnum
from Procedures.OutputProcedure import OutputProcedure as output
from Models.Config.ConfigWebdriverModel import ConfigWebdriverModel

class ConfigModel():
    webdriver_model: ConfigWebdriverModel
    search_string: str

    def __init__(self, config_path):
        self.data = self.load_json(config_path)
        self.webdriver_model = ConfigWebdriverModel(
            json = self.get_value_for_key('webdriver')
        )
        
        self.search_string = self.get_value_for_key('search_string')

    def load_json(self, config_path):
        try:
            with open(config_path) as config_file:
                return json.load(config_file)
        except FileNotFoundError:
            output.console_log("File not found, make sure file exists or path is correct...")
            sys.exit(0)
        except ValueError:
            output.console_log("Decoding JSON has failed, please check validity of config file...")
            sys.exit(0)

    def get_value_for_key(self, key):
        try:
            value = self.data[key]
            return value
        except KeyError:
            output.console_log(f"Value requested from config.json with unknown key: ['{key}']")
            sys.exit(0)