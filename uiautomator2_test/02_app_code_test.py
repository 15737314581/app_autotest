# coding = utf-8
import uiautomator2 as u2

driver = u2.connect('emulator-5554')
# 关闭app
driver.app_stop('com.tencent.mobileqq')
# 判断这个app是否启动了
if driver.app_wait('com.tencent.mobileqq',timeout=5):
    print('QQ正在运行')
else:
    driver.app_start('com.tencent.mobileqq')

# 查看运行的app信息
print(driver.app_current())

# 获取窗口大小
print(driver.window_size())
# 查看当前正在运行的所有应用
print(driver.app_list_running())

# 停止所有app
# driver.app_stop_all()