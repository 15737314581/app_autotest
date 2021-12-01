# coding = utf-8

# coding = utf-8
import xlrd
from model.case_model import steps_model


class ReadExcel:
    def read_excel_by_sheetname(self):
        workbook = xlrd.open_workbook('../data/autotest.xlsx')
        names = workbook.sheet_names()
        step_dict = dict()
        data_dict = dict()
        result = []
        for name in names:
            if name == 'data':
                data_xls = workbook.sheet_by_name(name)
                for i in range(data_xls.nrows):
                    data_name = data_xls.cell_value(i, 0)
                    data_dict[data_name] = []
                    for j in range(data_xls.ncols):
                        data_value = data_xls.cell_value(i, j).strip()
                        if j == 0 or data_value == '':
                            continue
                        else:
                            data_dict[data_name].append(eval(data_value))
            else:
                data_xls = workbook.sheet_by_name(name)
                step_dict[name] = []
                for i in range(data_xls.nrows):
                    if i == 0:
                        continue  # 跳过表头
                    else:
                        smart_list = []
                        for j in range(data_xls.ncols):
                            smart_list.append(data_xls.cell_value(i, j))
                        model = steps_model()
                        model.sort = smart_list[0]
                        model.action = smart_list[1]
                        model.searchType = smart_list[2]
                        model.searchValue = smart_list[3]
                        model.searchBy = smart_list[4]
                        model.searchIndex = smart_list[5]
                        model.validataData = smart_list[6]
                        model.validateAttr = smart_list[7]
                        step_dict[name].append(model)
        # 格式转化
        for case_name in step_dict.keys():
            if data_dict[case_name]:
                num = 0
                for data in data_dict[case_name]:
                    result.append({
                        "case_name": case_name,
                        "case_data": data,
                        "case_steps": step_dict[case_name],
                        "case_num": "{}_{}".format(case_name, num)
                    })
                    num += 1
            else:
                result.append({
                    "case_name": case_name,
                    "case_data": {},
                    "case_steps": step_dict[case_name],
                    "case_desc": "{}_0".format(case_name)
                })
        print(result)
        return result

if __name__ == '__main__':
    excel = ReadExcel()
    print(excel.read_excel_by_sheetname())
