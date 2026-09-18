# 06_read_files.py
from datetime import datetime
from random import randint
from calendar import monthrange
from os.path import exists, getsize

# Failinimed
names_filename = "names.txt"
person_filename = "person.txt"

if exists(names_filename):
    if getsize(names_filename):
        now = datetime.now()
        days_in_month = monthrange(now.year, now.month)[1]
        print(now, days_in_month)  # TEST!

        with open(names_filename, 'r', encoding='utf-8') as r:
            with open(person_filename, 'w', encoding='utf-8') as w:
                w.write("Nimi; Vanus; Kuupäev\n") # Päis!
                
                for line in r:
                    line = line.strip()
                    age = randint(1, 122)
                    # Juhuslik kuupäev ja kellaaeg jooksvas kuus
                    random_date = datetime(
                        now.year,
                        now.month,
                        randint(1, days_in_month),
                        randint(0, 23),
                        randint(0, 59),
                        randint(0, 59)
                    )
                    print(line, age, random_date)

                    formatted_datetime = random_date.strftime("%d.%m.%Y %H:%M:%S")

                    # versioon 1
                    w.write(f'{line};{age};{formatted_datetime}\n')

                    #versioon 2
                    person = [line, str(age), formatted_datetime]
                    w.write(';'.join(person) + "\n")

                print(f'fail {person_filename} on loodud.')
    else:
        print(f'Fail {names_filename} on tühi.')
else:
    print(f'Faili {names_filename} ei leitud.')
