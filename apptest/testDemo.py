# coding = utf-8e
from appium import webdriver
import time
import unittest
from PO_page.QQLoginPage import LoginPage

info = {
    "deviceName": "emulator-5554",
    "platformName": "Android",
    "appPackage": "com.tencent.mobileqq",
    "appActivity": ".activity.SplashActivity",
    "platformVersion": "6.0.1",
    "onRest": True
}


class QQLoginTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', info)
        self.driver.implicitly_wait(5)
        self.login_page = LoginPage(self.driver)

    def tearDown(self) -> None:
        self.driver.quit()

    def test01(self):
        self.login_page.qq_login('123456','111222')

if __name__ == '__main__':
    unittest.main()



