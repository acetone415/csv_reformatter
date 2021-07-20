import csv
import datetime
from collections import namedtuple
from pathlib import Path


DIR_TO_REFORMAT = Path(__file__) / 'reports/to_reformat'
DIR_REFORMATTED = Path(__file__) / 'reports/reformatted'


start_time = datetime.datetime.now()

filename = 'report_example2'  # input file
reformatted_csv = f'{filename}_made_on_{datetime.datetime.now().date()}'  # output file

keys = ('office', 'id', 'full_name', 'reg_numb', 'date')  # input file columns
Person = namedtuple('Person', keys)
info = {}
all_docs_list = []  # list of documents to sign

with open(f'{filename}.csv', encoding='utf_8', newline='\n') as csvfile:
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

with open(f'{reformatted_csv}.csv', 'w', encoding='utf-8', newline='\n') as csvfile:
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