# search_person.py
"""
Küsi kasutajalt isikut (eesnimi või perenimi) ja otsi failist sellist isikut. Kui
leiab, väljasta kogu faili rida. Otsida Persons.cvs failist. Kasuta import cvs varianti faili lugemiseks. Otsing on 
tõstutundetu. Otsing peab olema vähemalt kaks märki
"""

import csv

src = 'Persons.csv'

query = input("Sisesta eesnimi või perenimi (vähemalt 2 märki): ").strip()

if len(query) < 2:
    print("Otsing peab olema vähemalt 2 märki.")
else:
    query = query.lower()  # tõstutundetu otsing

    with open(src, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        header = next(reader)  # päis

        found_any = False

        for parts in reader:
            first_name = parts[0].lower()
            last_name = parts[1].lower()