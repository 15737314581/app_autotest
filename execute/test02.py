# coding = utf-8
from selenium.webdriver.common.by import By
from config.read_excel import ReadExcel
import pytest
import time

class Test02:
    excel = ReadExcel()
    steps = excel.read_excel_by_sheetname('login')
    @pytest.mark.parametrize('step',steps)
    def test_case(self,driver,step):
        time.sleep(1)
        if step.action == 'wait':
            driver.implicitly_wait(step.validataData)
            return
        elif step.action == 'end':
            driver.close_app()
            time.sleep(3)
            driver.launch_app()
            time.sleep(3)
            return
        elif step.searchType == 'find_elements':
            element = getattr(driver,step.searchType)(getattr(By,step.searchBy),step.searchValue)[step.searchIndex]
        else:
            element = getattr(driver,step.searchType)(step.searchValue)
        if step.action == 'screen':
            print("截图处理")
        elif step.action == 'assert':
            expected_result = step.validataData
            actual_result = getattr(element,'get_attribute')(step.validateAttr)
            try:
                assert expected_result == actual_result
                print('断言成功')
            except Exception as e:
                print('断言失败：{}'.format(e))
        elif step.action == 'send_keys':
            getattr(element,step.action)(step.validataData)
        else:
            getattr(element,step.action)()

if __name__ == '__main__':
    pytest.main(['test02.py::Test02::test_case','--html=../report2/report.html'])

