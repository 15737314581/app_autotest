# coding = utf-8
from selenium.webdriver.common.by import By
import time


class LoginPage:
    agree_btn = (By.ID, 'com.tencent.mobileqq:id/dialogRightBtn')
    login_btn = (By.ID, 'com.tencent.mobileqq:id/btn_login')
    username_input = (By.XPATH, '//android.widget.EditText[@content-desc="请输入QQ号码或手机或邮箱"]')
    password_input = (By.XPATH, '//android.widget.EditText[@content-desc="密码 安全"]')
    submit_btn = (By.ID, 'com.tencent.mobileqq:id/login')
    before_allow_btn = (By.ID, 'com.tencent.mobileqq:id/dialogRightBtn')
    allow_btn = (By.ID, 'com.android.packageinstaller:id/permission_allow_button')


    def __init__(self,driver):
        self.driver = driver

    def custom_click(self,ele):
        self.driver.find_element(*ele).click()
    def custom_send_keys(self,ele,content):
        self.driver.find_element(*ele).send_keys(content)

    def qq_login(self,username,password):
        self.custom_click(LoginPage.agree_btn)
        time.sleep(2)
        self.custom_click(LoginPage.login_btn)
        time.sleep(2)
        self.custom_send_keys(LoginPage.username_input,username)
        time.sleep(2)
        self.custom_send_keys(LoginPage.password_input,password)
        time.sleep(2)
        self.custom_click(LoginPage.submit_btn)
        time.sleep(2)
        self.custom_click(LoginPage.before_allow_btn)
        time.sleep(2)
        self.custom_click(LoginPage.allow_btn)
        time.sleep(2)
        self.custom_click(LoginPage.allow_btn)
        time.sleep(5)


