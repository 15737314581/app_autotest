# coding = utf-8
import time

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# from model.case_model import steps_model
from config.read_excel import ReadExcel
import pytest


class Test01:
    read_excel = ReadExcel()
    steps = read_excel.read_excel_by_sheetname('login')

    @pytest.mark.parametrize("step",steps)
    def test_case(self, driver, step):
        time.sleep(1)
        if step.searchType == 'find_elements':
            element = getattr(driver, step.searchType)(getattr(By, step.searchBy), step.searchValue)[
                int(step.searchIndex)]
        elif step.action == 'wait':  # 等待页面加载
            driver.implicitly_wait(int(step.validataData))
            return
        else:
            element = getattr(driver, step.searchType)(step.searchValue)
        if step.action == 'screenshot':  # 截图
            print('截图')

        elif step.action == 'assert':  # 断言
            # 获取内容

            actual_result = getattr(element, 'get_attribute')(step.validateAttr)
            expected_result = step.validataData
            # 断言
            try:
                assert expected_result == actual_result
                print('断言成功')
            except Exception as e:
                print('断言失败：{}'.format(e))

            print('断言')

        elif step.action == 'send_keys':  # 输入文字
            getattr(element, step.action)(step.validataData)
            print("输入：" + step.validataData)

        else:
            getattr(element, step.action)()


if __name__ == '__main__':
    pytest.main(["test01.py::Test01::test_case","--html=../report/report.html"])
