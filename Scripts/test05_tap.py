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
    目标：模拟手势高级操作 --轻敲
    需求：
        1. 打开设置
        2. 轻敲wlan
"""

# 定位 wlan
wlan=driver.find_element_by_xpath("//*[@text='WLAN']")
# 调用轻敲  1. 导包(TouchAciton) 2.方法 tap

"""注意：在TouchAction类中，所有的方法都必须执行perform()方法才能执行！"""
# 1. 基于元素 轻敲
# TouchAction(driver).tap(wlan).perform()
# 2. 基于坐标 轻敲
TouchAction(driver).tap(x=381,y=651).perform()

sleep(3)
driver.quit()
