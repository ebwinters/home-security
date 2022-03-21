import json

def readAppSetting(appSettingKey):
    f = open('/home/pi/home-sec/appsettings.json')
    contents = json.load(f)
    f.close()
    return contents[appSettingKey]
