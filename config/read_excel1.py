# coding = utf-8
import xlrd
from model.case_model import steps_model


class ReadExcel:
    def read_excel_by_sheetname(self):
        workbook = xlrd.open_workbook('../data/autotest.xlsx')
        sheetnames = workbook.sheet_names()
        # print(sheetnames)
        # large_list = []
        large_dict = dict()
        for sheetname in sheetnames:
            dict_data1 = dict()
            if sheetname == 'data':
                data_xls = workbook.sheet_by_name(sheetname)
                for i in range(data_xls.nrows):
                    data_list = []
                    for j in range(data_xls.ncols):
                        if j == 0:
                            key1 = data_xls.cell_value(i, j)
                            # print(key1)
                        else:
                            data_list.append(eval(data_xls.cell_value(i, j)))
                    # print(data_list)
                    dict_data1.update({'{}'.format(key1): data_list})
                # dict_data4 = dict()
                # dict_data4.update({'{}'.format('data'): dict_data1})
                # large_list.append(dict_data4)
                large_dict.update({'{}'.format('data'): dict_data1})

            else:
                data_xls = workbook.sheet_by_name(sheetname)
                big_list = []
                dict_data2 = dict()
                for i in range(data_xls.nrows):
                    if i == 0:  # 处理掉表头
                        continue
                    else:
                        smart_list = []  # 一个集合代表一个步骤
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
                        big_list.append(model)
                # 循环走完之后，需要将数据做成字典
                dict_data2.update({"{}".format(sheetname): big_list})
                # dict_data3 = dict()
                # dict_data3.update({"{}".format('case'): dict_data2})
                # large_list.append(dict_data3)
                large_dict.update({"{}".format('case'): dict_data2})
        # print(large_list)
        print(large_dict)
        return large_dict


if __name__ == '__main__':
    excel = ReadExcel()
    result = excel.read_excel_by_sheetname()
    print(result)
