from datetime import date
# 01_variables.py

# Muutjad ja andmetüübid
name = 'Tanel Vilimaa'
age = 43
height = 1.88
is_student = False

# Tavaline print
print('nimi' + name)
print('vanus'+ str (age)+ 'a.')

#f-string
print(f'pikkus: {height} m.')
print(f'Kas on õpilane: {is_student}')

# Andmete küsimine
birth_year = int(input())


print(f'{birth_year} {type(birth_year)}'

#Tänane kuupäev
today = date.today()
print(f"kuupäev {today}. Vormindatud: {today.strftime("%d.%m.%Y")}")
print(f'Jooksev aasta: {today.year}')

#Arvutamine
calculated_age = today.year - birth_year
print(f'Ligikaudne vanus on {calculated_age} aastat.')

# ÜLESANNE: Eelmine lause tee + märkidega.
print('Ligikaudn vanus on ' str(calculated_age) + ' aastat.')

#Tingimus
if calculated_age >= 18:
    print('Oled täisealine.')
else:
    print('Oled alaealine.')

    temperature = 15

    if temperature < 0:
        print('Väga külmetab.')
    elif temperature < 20:
        print('Õues on jahe.')
    else:
        print('Õues on soe.')

#Ülesanne kontrolli muutujat calculated_age
#Kontrolli esmalt kas see on õiges vahemikus 1-122 k.a.
#alla 18-> alaealine
#all 65->tööealine
#alla 100-> pensionär
#ülejäänud on pikaealised
if calculated_age < 1 or calculated_age > 122:
    print('Sisestatud vanus on vale.')
elif calculated_age < 18:
    print('Oled alaealine.')
elif calculated_age < 65:
    print('Oled tööealine.')
elif calculated_age < 100:
    print('Oled pensionär.')
else:
    print('Oled pikaealine.')
    