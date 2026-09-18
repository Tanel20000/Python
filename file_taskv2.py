






import csv
from datetime import datetime

filename = 'person.txt'

with open(filename, 'r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)  # Jäta päis vahele

    for row in reader:
        date_time = row[2]

        date_time = datetime.strptime(date_time, "%d.%m.%Y %H:%M:%S")

        if 6 <= date_time.hour <= 11:
            print(' '.join(row))
