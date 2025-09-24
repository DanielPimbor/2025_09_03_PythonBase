"""1. Feladat
Készíts egy rövid programot, amely 1 és 3 között generál véletlenszámot, majd összehasonlítja ezt a felhasználó által megadott, 
szintén ebbe a tartományba eső számmal! Az összehasonlítás eredményéről tájékoztassa a felhasználót! """

import random

random_szam = random.randint(1, 3)

while True:
    try:
        tipp = int(input('Tippelj egy számot 1 és 3 között. '))
        if 1 <= tipp <= 3:
            break
        else:
            print('Nem jó számot adtál meg, próbáld újra.')
    except ValueError:
        print('Helytelen válasz. ')


if int(tipp) == int(random_szam):
    print('Eltaláltad a számot. Hurrá!')

else:
    print(f'Sajnos nem találtad el. Ez volt a szám: {random_szam} ')
