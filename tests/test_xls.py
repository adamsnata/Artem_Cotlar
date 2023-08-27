import os.path
import xlrd

# TODO оформить в тест, добавить ассерты и использовать универсальный путь
current = os.path.abspath(__file__)
project_root = os.path.dirname(current)
joined_path = os.path.join(project_root, 'resources', 'file_example_XLS_10.xls')

def test_xls():
    book = xlrd.open_workbook(joined_path)
    count_sheets = book.nsheets
    print(f'Количество листов {count_sheets}')
    name_sheet = book.sheet_names()
    print(f'Имена листов {name_sheet}')

    sheet = book.sheet_by_index(0)
    col_count = sheet.ncols
    print(f'Количество колонок  {col_count}')

    col_rows = sheet.nrows
    print(f'Количество строк    {col_rows}')

    cell = sheet.cell_value(rowx=3, colx=2)
    print(f'Пересечение строки и столбца {cell}')

    # for rx in range(sheet.nrows):
    # print(sheet.row(rx))

    assert count_sheets == 1
    assert name_sheet == ['Sheet1']
    assert col_count == 8
    assert col_rows == 10
    assert cell == 'Gent'
