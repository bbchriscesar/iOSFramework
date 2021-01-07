from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

xpath = By.XPATH
id = By.ID
css = By.CSS_SELECTOR
name = By.NAME
className = By.CLASS_NAME

class iOSDM(object):
    def __init__(self, driver):
        self.driver = driver

    def quit_driver(self):
        self.driver.quit()

    def waitandclick(self, locator, element):
        wait = WebDriverWait(self.driver, 10)
        try:
            element = wait.until(EC.presence_of_element_located((locator, element)))
            element.click()
        except Exception as ex:
            print(ex)