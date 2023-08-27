import csv
import os.path

from tests.conftest import RESOURCE_PATH

# TODO оформить в тест, добавить ассерты и использовать универсальный путь

joined_path = os.path.join(RESOURCE_PATH, 'new_csv.csv')


def test_csv():
    with open(joined_path, 'w', newline='') as csv_file:
        csvwriter = csv.writer(csv_file, delimiter=';')
        csvwriter.writerow(['Bonny', 'Born', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    with open(joined_path) as csv_file:
        csvreader = csv.reader(csv_file, delimiter=';')
        names = []
        for row in csvreader:
            print(row)
            names.append(row)

    assert names == [['Bonny', 'Born', 'Peter'], ['Alex', 'Serj', 'Yana']]
    assert len(names) == 2
