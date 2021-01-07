from PageObjects import locators as ss
from Framework.iOSDriverMethods import iOSDM
from Framework.CommonFunctions import Common
from selenium.webdriver.common.by import By
from time import sleep

xpath = By.XPATH
id = By.ID
css = By.CSS_SELECTOR
name = By.NAME
className = By.CLASS_NAME

class Settings(object):
    def __init__(self, driver):
        self.driver = driver
        self.adm = iOSDM(self.driver)
        self.com = Common()
        self.deviceDetails = self.com.readJSONConfig()
        self.path = self.com.get_screenshot_dir()
        self.screens = self.deviceDetails['screenshots']['main_screen'].split(",")

    def newFeature(self):
        self.driver.execute_script('mobile: scroll', {'direction': 'down'})
        sleep(2)
        self.driver.execute_script('mobile: scroll', {'direction': 'down'})
        sleep(2)