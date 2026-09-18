# 05_files.py
filename = 'name.txt'
names_filename = 'names.txt'
name = input('Sisesta nimi: ')
def valid_name(name):
    """kontrollib kas nimi on sobiv"""
    if len(name) < 2:
        return False

    for char in name:
        if not char.isalpha() and char != " " and char != "-":
            return False
    return True

f = open(filename, 'w', encoding='utf-8')
f.write(name + "\n")  # Nimi + reavahetus failis
f.close()





# Nime lisamine teise faili
if valid_name(name):
     with open(names_filename,'a', encoding= 'utf-8') as f:
        f.write(name + "\n")

        print(f'Nimi lisati faili {names_filename}. ')
else:
     print(f'Nime ei lisatud faili {names_filename}. ')
