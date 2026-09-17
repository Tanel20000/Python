# 02_lists.py
# Andmekogumid
# List [nimekiri], tuple (järjend),
# dictionary {sõnastik}

places = [] #tüi list
places.append('Kehtna')
places.append('Rapla') #lisa uus element lõppu
places.extend(['Viljandi', 'Tartu', 'Rapla']) # lõppu
places[1:1] = ['Tallinn', 'Pärnu']
places.insert(2, 'Are')

numbers = [1, 6, 3, 9, -12] # Loo nu,britelist

print(places)
print(numbers)

# Kustutamine
places.remove('Rapla') #Esimene leitud eemaldatakse
places.pop(6) # Viimane
del places [2] # Are
print(places)

#üLESANNE: Lisa Rapla, Pärnu ja Viljandi vahele ning listi lõppu
places.append('Rapla')
places.insert(3, 'Rapla')
print(places)

# Leiame elemendi indeksi ja mitu korda esineb
place = places [-1] # Võta viimane element ja omista muutujale
index = places.index(place) # Esimene leitud Rapla 
count = places.count(place) # Mitu leiti
print(index, count)

if places in places: 
    print(f'{places} on nimekirjas olemas.')
if 'Kohila' not in places:
    print('Kohilat pole nimekirjas. ')


print(len(places)) # Listi suurus
print(places[len(places)-1]) # Viimane element: Rapla 

# Koopia
new_list = places # Ei tee koopiat!
list_copy = places.copy()
list_list = list(places)
print(new_list)
print(list_copy)
print(list_list)

list_copy.sort() # A->Z .sort(reverse=True)
new_list_list = sorted(places, reverse = True)

print(list_copy)
print(new_list_list)
print(places)


new_list_list.clear() #tühejnda list
print(new_list_list)

# Ülesanne: kasuta originaal listi (places) ja eemalda
# viimane Rapla ilma [-1] kasutamata. Väljasa kolmanda
# elemendi keskmine täht SUURTÄHENA.
places.pop(len(places)-1)
print(places[2] [2]. title ()) #Pärnu => R .upper()
print(places)
