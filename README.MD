csv_reformater

This script returns a reformatted report (CSV file) about signed documents from the following format:

>'Office name','person id','full_name','reg_numb','date'

to the new format:

>'Office name', 'full_name', 'person id', 'reg_numb1', 'reg_numb2', ... , 'reg_numbN'


Where:
- 'reg_numb1', 'reg_numb2', ... , 'reg_numbN' - documents for signing
- '' means that document wasn't signed
- 'N' means that there was no task to sign the document
- 'year-month-day' - a day when document was signed



