"""Végezd el azt hogy ha a bevitt szam az kisebb mint nulla akkor negativ..."""

szam = int(input('Adj meg egy számot: '))

if szam < 0:
    print('Ez a szám negatív.')

elif szam > 0:
    print('Ez a szám pozitív.')

elif szam == 0:
    print('Ez a szám egyenlő nullával.')