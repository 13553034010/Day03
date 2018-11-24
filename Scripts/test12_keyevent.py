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
    目标：模拟音量键
    需求：
        1. 减三次音量缩小键，每减1次暂停1秒
        2. 增三次音量增大键，每增1次暂停1秒
        
    提示：
        1. 24为增加音量键码 
        2. 25为：减少音量键码
        3. 方法：keyevent()
          
"""
# 减少 3此音量键
for i in range(6):
    print("i:",i)
    sleep(1)
    driver.keyevent(25)
    sleep(1)
    driver.keyevent(24)


# # 增加 3此音量键
# for y in range(4):
#     sleep(1)
#     print("y:",y)
#     driver.keyevent(24)


sleep(10)
driver.quit()
