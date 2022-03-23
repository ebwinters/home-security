import json

def readAppSetting(appSettingKey):
    f = open('D:\\repos\\home-security\\appsettings.json')
    contents = json.load(f)
    f.close()
    return contents[appSettingKey]
