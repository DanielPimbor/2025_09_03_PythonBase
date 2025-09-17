"""5️ Szökőév ellenőrző
Kérj be egy évet, és írd ki, hogy szökőév-e.
(Szökőév, ha osztható 4-gyel, de nem 100-zal, kivéve ha 400-zal is osztható.)"""

i = '1'
while i == '1':

    while True:
        try:
            evszam = int(input('Adj meg egy évszámot és én megállapítom hogy szökőév-e. '))
            break
        except ValueError:
            print('Normális évszámot adj meg!')

    if evszam % 4 == 0 and evszam % 100 != 0 or evszam % 400 == 0 :
        print('Ez egy szökőév.')

    else:
        print('Nem szökőév.')


    i = input('Újra : 1 , Bezárás : 2 =>')

    if i != '1':
        break