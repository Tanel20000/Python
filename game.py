from random import randint

# Algväärtused
pc_nr = randint(1, 100)
steps = 0
game_over = False
cheated = False   # jälgime, kas kasutaja pettis

print(pc_nr)

def new_game():
    """ÜLESANNE 2: Paneb muutujad algseisu tagasi uue mängu jaoks"""
    global pc_nr, steps, game_over, cheated
    pc_nr = randint(1, 100)
    steps = 0
    game_over = False
    cheated = False # Ei ole petja
    print(f"(Uus salajane number testimiseks): {pc_nr}")

def ask():
    """Küsib mängijalt arvu ja kontrollib vastust"""
    global steps, game_over, cheated

    user_nr = int(input('Sisesta number (1-100): '))
    steps += 1

    # PETMINE: vale vahemik
    if user_nr < 1 or user_nr > 100:
        if user_nr == 1000: # Kontrollime kõigepealt tagaust, kuna see on väljaspool vahemikku 1-100
            print(f'Leidsid tagaukse. Õige vastus on {pc_nr}.')
        else:
            print("Sa sisestasid lubatud vahemikust väljas oleva arvu!")
        cheated = True
        game_over = True

    # Tavaline mänguloogika
    elif user_nr > pc_nr:
        print('Paku väiksem arv.')

    elif user_nr < pc_nr:
        print('Paku suurem arv.')

    else:
        game_over = True # Mäng saab läbi, aga me ei trüki siin veel samme

def lets_play():
    """Käivitab numbri äraarvamise mängu"""
    global game_over
    
    while not game_over:
        ask()

    # ÜLESANNE 1: Lõpusõnum kontrollib petmist alles siin, kui tsükkel on läbi
    if cheated:
        print("Sa petsid mängu!")
    else:
        print(f"Mäng lõppes. Arvasid numbri ära {steps} sammuga.")

    # Küsime kasutajalt uue mängu kohta pärast lõpusõnumit
    answer = input('Kas mängime veel? [J/E]: ').upper()
    if answer == 'J':
        new_game()    # Nüüd on see funktsioon üleval pool olemas ja kood ei anna viga!
        lets_play()   # Alustame mängutsüklit uuesti

# Käivita mäng esimest korda
lets_play()

