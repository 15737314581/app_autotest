import pytest
from appium import webdriver
from py.xml import html

import os

driver = None


def pytest_html_report_title(report):
    report.title = "华测教育 - 自动化测试报告"


def pytest_configure(config):
    # 配置pytest
    # 添加接口地址与项目名称
    config._metadata["项目名称"] = "QQ应用登录功能"
    # 删除Java_Home
    config._metadata.pop("JAVA_HOME")


@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("所属部门: -软件测试")])
    prefix.extend([html.p("测试人员: jjf")])


@pytest.fixture(scope="session")
def driver():
    global driver
    info = {
        "deviceName": "emulator-5554",
        "platformName": "Android",
        "appPackage": "com.tencent.mobileqq",
        "appActivity": ".activity.SplashActivity",
        "platformVersion": "6.0.1",
        "onRest": True
    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", info)

    yield driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        # xfail = hasattr(report, 'wasxfail')
        # if (report.skipped and xfail) or (report.failed and not xfail):
        screen = _capture_screenshot()
        # only add additional html on failure
        html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:360px;height:334px;" ' \
               'align="right"/></div>' % screen
        extra.append(pytest_html.extras.html(html))
    report.extra = extra


def _capture_screenshot():
    return driver.get_screenshot_as_base64()
