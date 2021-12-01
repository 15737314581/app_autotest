# coding = utf-8
import uiautomator2 as u2
import time

driver = u2.connect('emulator-5554')
driver.app_stop('com.tencent.mobileqq')
if driver.app_wait('com.tencent.mobileqq',timeout=3):
    print('QQ正在运行')
else:
    driver.app_start('com.tencent.mobileqq')

driver(resourceId='com.tencent.mobileqq:id/btn_login').click()
# time.sleep(3)
driver(resourceId='com.tencent.mobileqq:id/em2').click()
driver.send_keys('123456',clear=True)
driver(resourceId="com.tencent.mobileqq:id/password").click()
driver.send_keys("111222", clear=True)

driver(resourceId='com.tencent.mobileqq:id/login').click()
