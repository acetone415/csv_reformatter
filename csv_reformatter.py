import argparse
import csv
import datetime
import os
from collections import namedtuple


parser = argparse.ArgumentParser()
parser.add_argument('filepath', help='Path to input CSV file')
parser.add_argument('-d', '--dir', default='./',
    help='Directory for output CSV. Default=%(default)s')
args = parser.parse_args()
file_path = args.filepath
output_csv_dir = args.dir

input_filename = os.path.basename(file_path)
output_filename = f'{datetime.datetime.now().date()}_{input_filename}'
output_csv_path = os.path.join(output_csv_dir, output_filename)


start_time = datetime.datetime.now()

keys = ('office', 'id', 'full_name', 'reg_numb', 'date')  # input file columns
Person = namedtuple('Person', keys)
info = {}
all_docs_list = []  # list of documents to sign


with open(file_path, encoding='utf_8', newline='\n') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        employee = Person(*row)
        if employee.id in info.keys():
            info[employee.id]['docs'].update({employee.reg_numb: employee.date})
        else:
            info.update({employee.id: {
                'office': employee.office,
                'full_name': employee.full_name,
                'docs': {employee.reg_numb: employee.date}
            }})
        if employee.reg_numb not in all_docs_list:
            all_docs_list.append(employee.reg_numb)


with open(output_csv_path, 'w', encoding='utf-8', newline='\n') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Филиал', 'ФИО', 'ТН'] + all_docs_list)
    for item in info:
        doc_field = []
        for key in all_docs_list:
            doc_field.append(info[item]['docs'].get(key, None))
        writer.writerow([info[item]['office'],
                         info[item]['full_name'],
                         item,
                         *doc_field
                         ]
                        )

print(f'Time:{datetime.datetime.now() - start_time}')
