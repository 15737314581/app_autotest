# coding = utf-8
from selenium.webdriver.common.by import By
from config.read_excel2 import ReadExcel
import pytest
import time


class Test03:
    excel = ReadExcel()
    execute_infos = excel.read_excel_by_sheetname()

    @pytest.mark.parametrize('execute_info', execute_infos)
    def test_case(self, driver, execute_info):
        steps = execute_info['case_steps']
        data = execute_info['case_data']
        for step in steps:
            time.sleep(1)
            if step.action == 'wait':
                wait_value = data[step.validataData]
                driver.implicitly_wait(wait_value)
                continue
            elif step.action == 'end':
                driver.close_app()
                time.sleep(3)
                driver.launch_app()
                time.sleep(3)
                continue
            elif step.searchType == 'find_elements':
                element = getattr(driver, step.searchType)(getattr(By, step.searchBy), step.searchValue)[
                    step.searchIndex]
            else:
                element = getattr(driver, step.searchType)(step.searchValue)
            if step.action == 'screen':
                print("截图处理")
            elif step.action == 'assert':
                expected_result = data[step.validataData]
                actual_result = getattr(element, 'get_attribute')(data[step.validateAttr])
                try:
                    assert expected_result == actual_result
                    print('断言成功')
                except Exception as e:
                    print('断言失败：{}'.format(e))
            elif step.action == 'send_keys':
                send_keys_value = data[step.validataData]
                getattr(element, step.action)(send_keys_value)
            else:
                getattr(element, step.action)()


if __name__ == '__main__':
    pytest.main(['test03.py::Test03::test_case', '--html=../report3/report.html'])
