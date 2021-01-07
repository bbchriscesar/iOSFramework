from Resources import capabilities
from ApplicationFeature import settings
import pytest
import Framework.iOSDriverMethods
import Framework.CommonFunctions

com = Framework.CommonFunctions.Common()
dev = com.readJSONConfig()

@pytest.mark.parametrize("details", dev['devices'])
def test_validateSettings(details):
    driver = capabilities.setup(details)
    ss = settings.Settings(driver)
    ss.newFeature()
    res = Framework.iOSDriverMethods.iOSDM(driver)
    res.quit_driver()