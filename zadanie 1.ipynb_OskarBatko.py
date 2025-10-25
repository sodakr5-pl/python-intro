import random #https://docs.python.org/3/library/random.html

Lista_1=[1,4,52,3,4,12,56] # Tworzymy pierwszą listę liczb
lista_2=[4,12,3,12,4,5,6,7,23] # Tworzymy drugą listę liczb

zip_listy=list(zip(Lista_1,lista_2)) # Łączymy listy w pary (krotki) za pomocą zip()
print("Połączone listy=",zip_listy) # Wyświetlamy połączone listy

lista=[] # Tworzymy pustą listę, do której dodamy losowe liczby

for i in range(0,10): # Pętla for generująca 10 liczb
    lista.append(random.randint(0,10000)) # Dodajemy losową liczbę z zakresu 0-10000
    
print (lista) # Wyświetlamy listę losowych liczb

try: # Próba wybrania losowego elementu z listy
    losowy=random.choice(lista) # Wybieramy losowy element
    print (losowy) # Wyświetlamy wylosowaną liczbę
except IndexError:  # Obsługa błędu, gdy lista jest pusta
    print ("Lista jest pusta!") # Komunikat w przypadku pustej listy


#link do repozytorium - https://github.com/sodakr5-pl/python-intro.git