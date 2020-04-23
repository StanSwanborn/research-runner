from typing import List
from Models.Enums.WebdriverEnum import WebdriverEnum

class ConfigWebdriverModel():
    driver_type: WebdriverEnum
    driver_path: str
    extension_paths: List[str]

    def __init__(self, json):
        self.driver_type = WebdriverEnum[json['driver_type']]
        self.driver_path = json['driver_path']
        self.extension_paths = json['extension_paths']