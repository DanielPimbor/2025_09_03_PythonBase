"""2. Feladat
A program a pénzfeldobást modellezi. Kérdezze meg a felhasználótól a választását (fej vagy írás), majd adjon tájékoztatást, hogy eltalálta-e! """

import random

fej_iras = random.randint(1, 2)

while True:
    try:
        tipp = int(input('Fej vagy írás? Fej : 1 , Írás : 2 => '))
        if tipp == 1 or tipp == 2:
            break
        else:
            print('Helytelen válasz, próbáld újra. Csak 1 vagy 2 lehet.')
    except ValueError:
        print('Helytelen válasz. Csak számot adj meg (1 vagy 2).')

oldalak = {1: "Fej", 2: "Írás"}

if tipp == fej_iras:
    print('Eltaláltad!')
else:
    print('Sajnos nem találtad el.')

print(f'{oldalak[fej_iras]} volt!')




