import json
import os
from datetime import date

class Common:

    def get_current_date(self):
        today = str(date.today())
        return today

    def get_screenshot_dir(self):
        self.dir_path = os.path.dirname(os.getcwd()) + '/Resources/Screenshot/' + self.get_current_date() + '/'
        if not os.path.exists(self.dir_path):
            os.makedirs(self.dir_path)
        return self.dir_path

    def readJSONConfig(self):
        with open('/Users/christiannec/PycharmProjects/SampleiOSFramework/Resources/config.json') as json_data:
            deviceconfig = json.load(json_data)
        return deviceconfig