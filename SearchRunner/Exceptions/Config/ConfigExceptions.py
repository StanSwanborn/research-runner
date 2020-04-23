class ConfigNotValidException(Exception):
    """CONFIG file is invalid"""

class ConfigChromedriverNotFoundException(ConfigNotValidException):
    """Invalid path to Chromedriver as found in CONFIG"""

class ConfigFirefoxdriverNotFoundException(ConfigNotValidException):
    """Invalid path to Firefoxdriver (geckodriver) as found in CONFIG"""