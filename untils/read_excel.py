import os
import openpyxl
import pytest
from config import datas_path
class ReadExcel:
    def  read_excel(self,file_path,sheet_name):
        datas = []
        try:
            wb = openpyxl.load_workbook(file_path)
            sheet = wb[sheet_name]
            for row in sheet.iter_rows(min_row=2):
                data= tuple([cell.value for cell in row])
                datas.append(data)
        except Exception as e:
            print(e)
        return datas
if __name__ == '__main__':
    file_path = os.path.join(datas_path, 'autointerface.xlsx')
    datas = ReadExcel().read_excel(file_path,'Sheet1')
    print(datas)