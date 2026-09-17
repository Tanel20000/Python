from random import randint
"""
ÜLESANNE 1: jälgi, kas kasutaja petab või mitte. Kui kasutaja ei peta, 
siis ütle nii nagu praegu mitme sammuga ära arvas. Kui kasutaja pettis, 
siis ütle sa petsid mängu ja ära samme ütle.
"""

pc_nr = randint(1, 100)
steps = 0
game_over = False
cheated = False   # jälgime, kas kasutaja pettis

print(pc_nr)

def ask():
    """Küsib mängijalt arvu ja kontrollib vastust"""
    global steps, game_over, cheated

    user_nr = int(input('Sisesta number (1-100): '))
    steps += 1

    # PETMINE: vale vahemik
    if user_nr < 1 or user_nr > 100:
        print("Sa sisestasid lubatud vahemikust väljas oleva arvu!")
        cheated = True
        game_over = True

    # PETMINE: tagaukse
    elif user_nr == 1000:
        print(f'Leidsid tagaukse. Õige vastus on {pc_nr}.')
        cheated = True
        game_over = True

    # Tavaline mänguloogika
    elif user_nr > pc_nr:
        print('Paku väiksem arv.')

    elif user_nr < pc_nr:
        print('Paku suurem arv.')

    else:
        print(f'Arvasid numbri ära {steps} sammuga.')
        game_over = True


def lets_play():
    """Käivitab numbri äraarvamise mängu"""
    while not game_over:
        ask()

    # Lõpusõnum
    if cheated:
        print("Sa oled pettur!")
    else:
        print(f"Mäng lõppes. Arvasid numbri ära {steps} sammuga.")


lets_play()  # Käivita mäng
