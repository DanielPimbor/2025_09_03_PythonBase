"""A csoport: Készítsünk programot, amely labdák csomagolásához végez számításokat.
A labdákat szalaggal kell átkötni úgy, hogy kétszer körbe érje őket, és a masni készítéséhez számolunk még 60 cm-t.
A labda körül a szalag egy kör (kerület képlete 2*r*PI)
A program kérje be a labda átmérőjét, a labdák számát, és a rendelkezésre álló szalag hosszát!
Számítsa ki, és írja a képernyőre, hogy a bekért számú labda csomagolásához hány centiméter szalagra van szükség, valamint állapítsa meg,
hogy elegendő szalagunk van-e a művelet elvégzéséhez, és ezt is közölje a felhasználóval!"""




átmérő = float(input('Adja meg a labda átmérőjét cm-ben: '))

labdák_száma = int(input('Adja meg a labdák számát: '))

adott_cm = float(input('Adja meg a szalagok összhosszát cm-ben: '))

szükséges_cm = átmérő * 2 * 3.14 * labdák_száma + 60 * labdák_száma

print(f'Ennyi cm szalagra lesz szükség: {szükséges_cm} cm ')

if float(szükséges_cm) > float(adott_cm):
    print('Nincs elegendő szalagunk hozzá.')

elif float(szükséges_cm) < float(adott_cm):
    print(f'Van elég szalagunk hozzá és még marad {float(adott_cm) - float(szükséges_cm)} cm ')

else:
    print('Pont elég szalagunk van hozzá.')




