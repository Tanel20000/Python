# 04_functions.py

def welcome():
    """Väljastab tervituse"""
    print('Tere, kuidas läheb?')


def welcome_name(name):
    """Tagastab tervituse koos nimega"""
    return f"Tervitus saadetud kasutajale: {name}"


def introduce(name, age=25):
    """Loob lihtsa tutvustava lause"""
    return f'Tema on {name} ja ta on {age} aastane!'


def multiply(number1: int, number2: int) -> int:
    """Korrutab kaks arvu"""
    return number1 * number2


def division(a, b):
    """Teostab kahe arvu jagamist"""
    if b == 0:
        return "Viga: nulliga ei saa jagada!"
    return a / b


# Testid
print(welcome_name("Marko"))

names = ['Jüri', 'Anna', 'Mihkel', 'Siim']
for name in names:
    print(welcome_name(name))

print(division(6, 2))
print(division(10, 5))
print(division(10, 0))
print()

print(introduce('Marko'))
print(introduce('Mari', 67))
print(introduce(age=50, name='Kalle'))
print(introduce('Kalle', age=25))
# ÜLESANNE: Loo funktsioon name_length() mis võtab vastu nime
# ja tagastab nime pikkuse.

def name_length(name):
    return len(name)

print(name_length("Tanel"))      # 5
print(name_length("Katrin"))     # 6
print(name_length("Jüri"))       # 4

# ÜLESANNE: Lisa käsitsi names listi veel paar nime. Väljasta
# listist need nimed kelle nime pikkus on 4 tähte
for name in names:
    if len(name) == 4:
        print(name)

        