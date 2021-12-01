# coding = utf-8
import xlrd
from model.case_model import steps_model


class ReadExcel:
    def read_excel_by_sheetname(self, sheetname):
        workbook = xlrd.open_workbook('../data/autotest_base.xlsx')
        case_sheet = workbook.sheet_by_name(sheetname)
        nrows = case_sheet.nrows
        ncols = case_sheet.ncols

        case_list = []
        for i in range(1, nrows):
            object_list = []
            for j in range(0, ncols):
                object_list.append(case_sheet.cell_value(i, j))
            model = steps_model()
            print(object_list)
            model.sort = object_list[0]
            model.action = object_list[1]
            model.searchType = object_list[2]
            model.searchValue = object_list[3]
            model.searchBy = object_list[4]
            model.searchIndex = object_list[5]
            model.validataData = object_list[6]
            model.validateAttr = object_list[7]
            case_list.append(model)
        return case_list


if __name__ == '__main__':
    excel = ReadExcel()
    result = excel.read_excel_by_sheetname('login')
    print(result)
