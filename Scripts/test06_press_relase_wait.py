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
    目标：模拟手势高级操作 --按下、等待、释放
    需求：
        1. 打开设置
        2. 按下wlan5秒钟
"""

# 定位 wlan
wlan=driver.find_element_by_xpath("//*[@text='WLAN']")
"""
    方法解释：
        1. press:按下
        2. wait:等待
        3. release：释放
        4. perform：执行
"""
# TouchAction(driver).press(wlan).wait(5000).release().perform()
# 单独测试 按下
TouchAction(driver).press(wlan).perform()

sleep(10)
driver.quit()
