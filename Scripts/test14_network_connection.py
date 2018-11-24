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
    目标：获取手机设备现有网络类型
          
"""
# 获取手机网络类型
print("当前网路类型为：",driver.network_connection)

# 设置手机类型
driver.set_network_connection(6)

print("设置类型后：当前网路类型为：",driver.network_connection)

sleep(10)
driver.quit()
