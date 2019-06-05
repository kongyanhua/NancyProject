import xlrd


def read_excel(path,row_num):
    # open and read an excel
    book = xlrd.open_workbook(path)
    # # print number of sheets
    # print(book.nsheets)
    # # print sheet names
    # print(book.sheet_names())
    # # get the first worksheet
    first_sheet = book.sheet_by_index(0)
    # read a row
    # print(first_sheet.row_values(0))
    # # read a cell
    # cell = first_sheet.cell(0,0)
    # print(cell)
    # print(cell.value)
    # # read a row slice
    # print(first_sheet.row_slice(rowx=0, start_colx=0, end_colx=2))
    return first_sheet.row_values(row_num)



# if __name__=='__main__':
#     Test1 = read_excel(r'C:\Users\nkong009\PycharmProjects\NancyProject\Data\TestExcel.xlsx',1)
#     print(Test1)


