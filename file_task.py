"""
file_task.py

Loe faili person.txt ja väljasta konsooli need isikud
(kogu info) kus kellaeg on 06:00:00 - 11:59:59

TÄIENDUS: Failis 06_read_files.py täienda teist faili päisega.
Lisades teise faili algusesse päise, mis kirjeldab veergude sisu:
Nimi;Vanus;Kuupäev või Name;Age;Date time.
Nüüd paranda seda faili, et see töötaks :-) Ära mõtle üle!
"""


import csv
from datetime import datetime  

filename = "person.txt"

with open(filename, "r", encoding="utf-8") as file
    file.readline() # Ainsus! Loeme pärise ära



    for line in f:
        person = line.strip().split(';')  # person on list
        date_time = person[2]             # Võtame kuupäeva

        # Muudame kuupäeva ja kellaaja objektiks (failis on string)
        date_time = datetime.strptime(date_time, '%d.%m.%Y %H:%M:%S')

        if date_time.hour >= 6 and date_time.hour <= 11:
            print(" ".join(person))       # Väljastame kogu info
