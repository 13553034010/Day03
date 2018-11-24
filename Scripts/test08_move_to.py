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
    目标：move_to移动方法
    需求：
        1. 使用TouchAction类内方法
        2. 从 存储 移动 更多
        
"""

# 定位 存储
save=driver.find_element_by_xpath("//*[@text='存储']")
# 定位 更多
more=driver.find_element_by_xpath("//*[@text='更多']")

# 调用 move_to 方法
TouchAction(driver).press(save).wait(100).move_to(more).wait(100).release().perform()
"""
    思路：
        1. 首先点击存储别松手
        2. 往更多方向移动
        3. 移动到更多位置，松手
"""

sleep(10)
driver.quit()
