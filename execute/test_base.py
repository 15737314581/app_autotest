# coding = utf-8
from appium import webdriver
from selenium.webdriver.common.by import By
from config.read_excel1 import ReadExcel

import time


def test():
    info = {
        "deviceName": "emulator-5554",
        "platformName": "Android",
        "appPackage": "com.tencent.mobileqq",
        "appActivity": ".activity.SplashActivity",
        "platformVersion": "6.0.1",
        "onRest": True
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", info)
    excel = ReadExcel()
    data_excel = excel.read_excel_by_sheetname()
    case_datas = data_excel['data']
    case_steps = data_excel['case']
    data_keys = case_datas.keys()
    for data_key in data_keys:
        case_value_list = case_datas[data_key]
        case_step_list = case_steps[data_key]
        for case_value in case_value_list:
            print(case_value)
            for step in case_step_list:
                time.sleep(1)
                if step.action == 'wait':
                    wait_value = case_value[step.validataData]
                    driver.implicitly_wait(wait_value)
                    continue
                elif step.action == 'end':
                    driver.close_app()
                    time.sleep(2)
                    driver.launch_app()
                    time.sleep(2)
                    continue
                elif step.searchType == 'find_elements':
                    element = getattr(driver, step.searchType)(getattr(By, step.searchBy), step.searchValue)[step.searchIndex]
                else:
                    element = getattr(driver, step.searchType)(step.searchValue)
                if step.action == 'screen':
                    print("截图处理")
                elif step.action == 'assert':
                    expected_result = case_value[step.validataData]
                    actual_result = getattr(element, 'get_attribute')(case_value[step.validateAttr])
                    try:
                        assert expected_result == actual_result
                        print('断言成功')
                    except Exception as e:
                        print('断言失败：{}'.format(e))
                elif step.action == 'send_keys':
                    send_keys_value = case_value[step.validataData]
                    getattr(element, step.action)(send_keys_value)
                else:
                    getattr(element, step.action)()



if __name__ == '__main__':
    test()
