# coding = utf-8
import uiautomator2 as u2
import time
driver = u2.connect('emulator-5554')
# 滑动
# driver.swipe(400,1000,400,500,1)
# 按home键
driver.press('home')
x = driver.window_size()[1]
y = driver.window_size()[0]
print(x,y)
# driver.drag(x * 0.326, y * 0.378, x * 0.498, y * 0.378)

# 整个屏幕左滑
time.sleep(2)
driver.swipe_ext('right')
time.sleep(2)
driver.swipe_ext('left')

