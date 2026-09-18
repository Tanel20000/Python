# read_mycsv.py
filename ='Create-MyCSV-v.csv'
total = 0 # Lõppvastus
row = 0 


def is_number(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

f = open(filename, 'r') 
cols = len(f.readline().strip().split(';'))
f.close()


    #print(cols)# Test mitu veergu
column = input(f'Mitmes veerg kokku liita 1-{cols}: ')

if is_number(column):
    column = int(column)
    if column < 1 or column > cols:
        print(f'Veeru number vales vahemikus. Lubatud on 1-{cols}.')
        exit()#Siin lõpetab töö
    column -= 1# Lahuta 1 väärtusest
    with open(filename, 'r', ) as f:
        content = f.readlines()
        for line in content:
            parts = line.strip().split(';')
            if is_number(parts[column]):
                total += int(parts[column])
                row += 1
                
        print(f'Veeru summa: {total}')
        print(f'Veerge liideti: {row} rida') 

else:
    print(f'Sisestus ei ole number.')
