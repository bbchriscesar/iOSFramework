from appium import webdriver

def setup(var):
        desired_caps_android = {
            "automationName": var['automationName'],
            "platformName": var['platformName'],
            "platformVersion": var['platformVersion'],
            "deviceName": var['deviceName'],
            "updatedWDABundleId": var['updatedWDABundleId'],
            "udid": var['udid'],
            "bundleId": var['bundleId'],
            "xcodeSigningId": var['xcodeSigningId']
        }
        driver = webdriver.Remote('http://localhost:' + var['port'] + '/wd/hub', desired_caps_android)
        return driver