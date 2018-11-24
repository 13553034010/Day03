from time import sleep

from appium import webdriver

# server 启动参数
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
    目标：scroll 滚动
    需求：
        1. 从存储滑到更多
"""
# 获取存储元素
save=driver.find_element_by_xpath("//*[contains(@text,'存储')]")
# 获取更多元素
more=driver.find_element_by_xpath("//*[contains(@text,'更多')]")

# 从存储滑到更多  直到自动停止为止
driver.scroll(save,more)

sleep(3)
driver.quit()
