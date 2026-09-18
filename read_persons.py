# read_persons.py
"""
Kasutajanimi:
    - eesnimi.perenimi
    -läbivalt väikeste tähtedega
    - eemalda rõhumärgid ( õüäö ja lätlased omad :))
    -eesnimedes tühik ja sidekriips eemaldada
EPOSTIAADRESS
    -kasutajanimi@asutus.com
KELLELE TEHA
    - Sündinud 1990 - 1990
UUS FAIL    
    - Sisaldab päist
    - Eesinimi; Perenimi; Isikukood, Kasutajanimi; Epost
    """
# Source - https://stackoverflow.com/a/518232



import unicodedata

src = 'Persons.csv'
dst = 'Person_accounts.csv.'
domain = '@asutus.com'
header = ['Kasutajanimi', 'Epost']

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

# print(strip_accents('äöõüÄÖÕšŠ'))
with open(src, 'r', encoding='utf-8') as source:
   with open(dst, 'w', encoding='utf-8') as dest:
      content = source.readlines()
      old_header = content[0].strip().split(';')
      new_header = ';'.join(old_header [:2]+ old_header [4:] + header)
      dest.write(new_header + "\n")

      for line in content[1:]:
         parts = line.strip().split(';')
         year = int(parts[2].split('.') [2])

         if 1990 <= year <= 1999:
            first_name = parts[0]
            last_name = parts[1]

            # Eemalda tühik ja sidekriips eesnimest
            first_name = first_name.replace('', '')
            first_name = first_name.replace('-', '')

            # kasutajanime loomine
            username = '.'.join([first_name, last_name]).lower()
            username = strip_accents(username)

            # E-Posti loomine
            email = username + domain



            email = username + domain 

            new_line = ';'.join(parts[:2] + parts [4:] + [username, email])
            dest.write(new_line + "\n")


            print(parts[0], parts[1], username, email)
            # Väljasta kontod kus kasutajanimi on 20 või rohkem
            # märkki
            if len(username) >= 20:
               print(new_line)

print('Valmis')

    






