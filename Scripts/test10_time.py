from time import sleep

from appium import webdriver

# server 启动参数
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# 输入中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
# app的信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

# 声明我们的driver对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


"""
    目标：获取手机设备时间
    方法：device_time
    返回：手机设备当前时间     
"""
# 打印手机当前设备时间
print(driver.device_time)

sleep(10)
driver.quit()