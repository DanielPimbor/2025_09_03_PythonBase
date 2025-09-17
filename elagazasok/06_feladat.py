"""6️ Egyszerű jelszóellenőrző
Kérj be egy jelszót, és ha megegyezik a „titok” szóval, írd ki: „Belépés engedélyezve!”, különben „Helytelen jelszó!”.
"""



password = input('Adja meg a jelszót: ')

while password != "titok":
    print('Helytelen jelszó. Próbálja újra. ')
    password = input('Adja meg a jelszót: ')

print('Belépés engedélyezve.')