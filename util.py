import json

def readAppSetting(appSettingKey):
    f = open('appsettings.json')
    contents = json.load(f)
    f.close()
    return contents[appSettingKey]