# 03_loops.py
import random 

names= ['Kati', 'Katrin', 'Katrina', 'Katariina']

for name in names:
    print(name)

print() # Tühi rida

for x in range (len (names)):
    print(names[x], end = ' ')

    print("\n") # Topelt reavahetus

for x in range(1, 5):
    print(x, end='|')

    print("\n")

for x in range(0, 10, 2):
    print(x, end='|')

print("\n")

x = 0 
while x < len (names):
    print(names[x], random.randint(1, 122))
    x+=1 # x = x +1

print() 

# ÜLESANNE: Väljasta listi nimed konsooli iga nimi
# eraldi real, kuid iga nime ees on järjekorra
# number, millele järgneb punkt ja tühik ja siis nimi.
# Kati
# Katrin
# Katrina
# Katariina
for x in range(len(names)):
    print(f"{x+1}. {names[x]}")
    print(str(x+1) + '.' + names [x])

# ÜLESANNE: Sama mis eelmine aga tagurpidises 
# järjekorras

index = len(names) -1 # 
order_number = 1
while index >= 0:
    print(f'{order_number}. {names[index]}')
    order_number += 1
    index -= 1
