
import pypdf
import os


# TODO оформить в тест, добавить ассерты и использовать универсальный путь
current = os.path.abspath(__file__)
project_root = os.path.dirname(current)
joined_path = os.path.join(project_root, 'resources', 'docs-pytest-org-en-latest.pdf')





def test_pdf_file():
    reader = pypdf.PdfReader(joined_path)
    number_of_pages = len(reader.pages)
    first_page = reader.pages[0]
    text = first_page.extract_text()
    print(number_of_pages)
    assert number_of_pages == 412
    print(first_page)
    print(text)


# count = 0
# for image_file in first_page.images:
#     with open(str(count) + image_file.name, 'wb') as fp:
#         fp.write(image_file.data)
#         count += 1

