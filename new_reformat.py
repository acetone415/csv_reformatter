import csv, datetime
from collections import namedtuple

start_time = datetime.datetime.now()
filename = 'report.csv'
reformated_csv = 'out.csv'
keys = ('office', 'id', 'full_name', 'reg_numb', 'date')
Person = namedtuple('Person', keys)
info = {}
docs = []

with open(filename, encoding='utf_8', newline='\n') as csvfile:
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
        if employee.reg_numb not in docs:
            docs.append(employee.reg_numb)

with open(reformated_csv, 'w', encoding='utf-8', newline='\n') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Филиал', 'ФИО', 'ТН'] + docs)
    for item in info:
        doc_field = []
        for key in docs:
            doc_field.append(info[item]['docs'].get(key, None))
        writer.writerow([info[item]['office'],
                         info[item]['full_name'],
                         item,
                         *doc_field
                         ]
                        )
print(f'Time:{datetime.datetime.now() - start_time}')