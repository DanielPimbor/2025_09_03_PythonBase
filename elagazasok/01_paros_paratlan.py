"""Páros számra..."""

while True:
    try:
        szam = int(input('Adj meg egy egész számot: '))
        break
    except ValueError:
        print('Nem egész szám! Adj meg egy egész számot.')

if szam % 2 == 0 and szam != 0:
    print('Páros')

elif szam % 2 != 0:
    print('Páratlan.')

else:
    print('Nulla.')

