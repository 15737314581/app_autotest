# coding = utf-8
from appium import webdriver
import time
info = {
        "deviceName": "emulator-5554",
        "platformName": "Android",
        "appPackage": "com.tencent.mobileqq",
        "appActivity": ".activity.SplashActivity",
        "platformVersion": "6.0.1",
        "onRest": True
    }
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", info)
for i in range(2):
    driver.find_element_by_id('com.tencent.mobileqq:id/dialogRightBtn').click()
    time.sleep(10)
    driver.find_element_by_id('com.tencent.mobileqq:id/btn_login').click()
    time.sleep(2)
    driver.find_element_by_xpath('//android.widget.EditText[@content-desc="请输入QQ号码或手机或邮箱"]').send_keys('123456')
    driver.find_element_by_xpath('//android.widget.EditText[@content-desc="密码 安全"]').send_keys('111222')
    driver.find_element_by_id('com.tencent.mobileqq:id/login').click()
    time.sleep(2)
    driver.find_element_by_id('com.tencent.mobileqq:id/dialogRightBtn').click()
    time.sleep(1)

    driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
    time.sleep(1)
    driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
    time.sleep(15)
    driver.close_app()
    time.sleep(2)
    driver.launch_app()
