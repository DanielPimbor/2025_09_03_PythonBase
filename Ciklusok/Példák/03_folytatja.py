folytatja = True

while folytatja:
    print('Vidd ki a szemetet!')

    while True:
        valasz = input('Mondjam még egyszer? (i/n) ')
        if valasz == 'i' or valasz == 'n':
            break
        else:
            print('Helytelen válasz. ')


    
    if valasz == 'n' :
        folytatja = False



print('>> Program vége! <<')
