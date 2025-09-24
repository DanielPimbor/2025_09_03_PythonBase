"""4️ Három szám közül a legnagyobb
Kérj be három egész számot, és írd ki, melyik a legnagyobb.
"""

print('Adj meg 3 számot és megmondom melyik a legnagyobb.')

i = '1'
while i == '1':

    szam1 = int(input('Add meg az első számot. '))

    szam2 = int(input('Add meg az második számot. '))

    szam3 = int(input('Add meg a harmadik számot. '))

    if szam1 > szam2 and szam1 > szam3:
        print(f'{szam1} a legnagyobb.')

    elif szam2 > szam1 and szam2 > szam3:
        print(f'{szam2} a legnagyobb.')

    elif szam3 > szam2 and szam3 > szam1:
        print(f'{szam3} a legnagyobb.')

    i = input('Újra : 1 , Bezárás : 2 => ')

    if i != '1':
        print('Viszlát!')
        break