def dodawanie(a,b):
    return  a+b
def odejmowanie(a,b):
    return a-b
def mnozenie(a,b):
    return a*b
def dzielenie(a,b):
    if b!=0:
        return a/b
    else:
        return "Nie dzielimy przez 0"

l1 = float(input("Podaj pierwszą liczbe: "))
l2 = float(input("Podaj drugą liczbe: "))

print("Wybierz opeeracje: ")
print("1 dodawanie")
print("2 odejmowanie")
print("3 mnożenie")
print("4 dzielenie")

operacja = input("Podaj nr operacji: ")

if operacja in ('1','2','3','4'):
    if operacja =='1':
        wynik = dodawanie(l1,l2)
        znak = '+'
    elif operacja == '2':
        wynik = odejmowanie(l1,l2)
        znak = '-'
    elif operacja == '3':
        wynik = mnozenie(l1,l2)
        znak = '*'
    elif operacja == '4':
        wynik = dzielenie(l1,l2)
        znak = '/'
    else:
        print("Nieprawidłowy wybór operacji.")
    
    print(f"Wynik: {l1} {znak} {l2} = {wynik}")
