"""7️ Hőmérséklet tanács
Kérj be egy hőmérsékletet Celsiusban, és adj tanácsot:
0 alatt: „Nagyon hideg, öltözz melegen!”


0–20: „Hűvös, kabát ajánlott.”


21–30: „Kellemes idő.”


30 felett: „Forróság, igyál sok vizet!”
"""

temp = int(input('Add meg a hőmérsékletet! '))

if temp < 0:
    print('Nagyon hideg, öltözz melegen!')

if 0 <= temp <= 20 :
    print('Hűvös, kabát ajánlott.')

if 21 <= temp <= 30:
    print('Kellemes idő.')

if temp > 30:
    print('Forróság, igyál sok vizet!')