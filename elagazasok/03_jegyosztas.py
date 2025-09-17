"""3️ Jegyosztályozás
Kérj be egy pontszámot 0–100 között, és írd ki az érdemjegyet:
0–49: Elégtelen
50–64: Elégséges
65–79: Közepes
80–89: Jó
90–100: Jeles"""

while True:
    try:
        pontszam = int(input('Add meg a pontszámodat: '))
        break
    except ValueError:
        print('Nem pontszám.')

if pontszam  >=0  and pontszam <= 49:
    print('Elégtelen')

elif pontszam >= 50 and pontszam <= 64:
    print('Elégséges')
    
elif pontszam >= 65 and pontszam <= 79:
    print('Közepes')
    
elif pontszam >= 80 and pontszam <= 89:
    print('Jó')
    
elif pontszam >= 90 and pontszam <= 100:
    print('Jeles')

elif pontszam > 100 or pontszam < 0:
    print('Helytelen pontszámot adtál meg.')
