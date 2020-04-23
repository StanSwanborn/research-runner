from pathlib import Path
from Models.Config.ConfigModel import ConfigModel
from Controllers.Scholar.ScholarController import ScholarController

class SearchController():
    # Need to know how many scholar results there are.

    _config_model: ConfigModel
    _scholar_controller: ScholarController

    def __init__(self, config_path: Path):
        self._config_model = ConfigModel(config_path)
        self._scholar_controller = ScholarController(self._config_model)

    def do_search(self):
        self._scholar_controller.open_and_search()