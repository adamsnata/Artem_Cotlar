import glob
import os
import zipfile
from zipfile import ZipFile
def test_zip_file():
    newzip = zipfile.ZipFile('../new_zip.zip', 'w')

    newzip.write('resources/docs-pytest-org-en-latest.pdf', 'docs-pytest-org-en-latest.pdf')
    newzip.write('resources/file_example_XLS_10.xls', 'file_example_XLS_10.xls')
    newzip.write('resources/file_example_XLSX_50.xlsx', 'file_example_XLS_50.xlsx')
    newzip.write('resources/new_csv.csv', 'new_csv.csv')
    newzip.close()


    with ZipFile('../new_zip.zip', 'r') as myzip:
        for item in myzip.namelist():
            print(item)

        assert item == ['docs-pytest-org-en-latest.pdf', 'file_example_XLS_10.xls', 'file_example_XLS_50.xlsx', 'new_csv.csv']










