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
driver.implicitly_wait(30)


"""
    目标：move_to移动方法
    需求：
        1.进入设置
        2.向上滑动屏幕到可见"安全"选项
        3.进入到安全
        4.点击屏幕锁定方式
        5.点击图案
        6.绘制图案
        
    坑：
        坑1：元素等待必须有
        坑2：坐标点不是元素，必须添加sleep
        
"""

# 定位 电池
dianchi=driver.find_element_by_xpath("//*[@text='电池']")
# 定位 WLAN
wlan=driver.find_element_by_xpath("//*[@text='WLAN']")

# 拖拽 从电池 拖拽 WLAN
driver.drag_and_drop(dianchi,wlan)
# 点击 安全
driver.find_element_by_xpath("//*[@text='安全']").click()
# 点击 屏幕锁定方式
driver.find_element_by_xpath("//*[@text='屏幕锁定方式']").click()
# 点击 图案
driver.find_element_by_xpath("//*[@text='图案']").click()
"""
    1. 239,851 2. 714,851 3. 1194,851
    2. 714,1336
    3, 239,1801 2. 714,1801 3. 1194,1801 
    
    提示：后面那个坐标点减前面那个坐标点
"""

# 注意：坐标点不上元素，如果在第一时间内没有找到此坐标点的化，将不执行，也不抛异常
sleep(2)


# 滑动
TouchAction(driver).press(x=239,y=851).wait(100).move_to(x=714-239,y=0).wait(100).\
    move_to(x=1194-714,y=0).wait(100).move_to(x=714-1194,y=1336-851).wait(100).\
    move_to(x=239-714,y=1801-1336).wait(100).move_to(x=714-239,y=0).wait(100).move_to(x=1194-714,y=0).\
    wait(100).release().perform()


sleep(10)
driver.quit()
