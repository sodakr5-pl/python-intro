def email_check(x):
    if len(x)==0:
        return False
    if '@' not in x:
        return False
    if not ('.pl' in x or '.com' in x):
        return False
    return True


def oblicz(a,h):
    if (a<=0) or (h<=0):
        return 'a lub h nie może być 0 lub mniejsze'
    else:
        wynik=a*h/2
        return wynik
    

def sortowanie(x):
    for i in range(len(x)):
        for j in range(len(x)-1):
            if x[j]>x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]
    return x

def konwertuj_date(data):
    dzien, miesiac,rok =data.split('-')
    return "/".join([rok, miesiac, dzien])

def palindrom(tekst):
    tekst=tekst.lower().replace(" ", "")  
    return tekst==tekst[::-1]



print(email_check("oskar@o2.pl"))

print(oblicz(2,-3))


lista=[2,3,6,1,2,3,9,0]
print(sortowanie(lista))


print(konwertuj_date("09-11-2025"))


print(palindrom("kot"))       
print(palindrom("A to kota"))   
print(palindrom("Auto"))  


#https://github.com/sodakr5-pl/python-intro/tree/zadanie_2