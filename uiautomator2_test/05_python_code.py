# coding = utf-8
import uiautomator2 as u2
from uiautomator2.ext.htmlreport import HTMLReport
import time
driver = u2.connect('emulator-5554')
driver.app_stop('com.netease.cloudmusic')
driver.app_start('com.netease.cloudmusic')

driver.implicitly_wait(20) # 隐式等待
hrp = HTMLReport(driver, 'report')
hrp.patch_click() # 记录好每一次的事件

driver(resourceId="com.netease.cloudmusic:id/portalTitle", text="歌单").click()

# 滑动操作
# time.sleep(3)
# driver(scrollable=True).scroll.toEnd() # 滑动到底部
# driver(scrollable=True).scroll.to(text=u'视频合辑') # 滑动到指定位置