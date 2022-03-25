import json
import os

def readAppSetting(appSettingKey):
    f = open(os. getcwd() + '/appsettings.json')
    contents = json.load(f)
    f.close()
    return contents[appSettingKey]
