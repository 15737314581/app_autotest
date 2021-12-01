# coding = utf-8
import uiautomator2 as u2

driver = u2.connect('emulator-5554')
driver.app_start('com.tencent.mobileqq','com.tencent.mobileqq.activity.LoginActivity')