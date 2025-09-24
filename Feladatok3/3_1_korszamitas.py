"""1. Feladat
Thonny fejlesztői környezetben készíts egy rövid programot, amely

    kommentként tartalmazza a program funkciójának leírását,
    konstansként tárolja PI értékét,
    egy másik változóban tárolja egy kör sugarának nagyságát (cm-ben megadva),
    kiszámolja és a képernyőre kiírja a kör kerületét és területét!

[Megjegyzés] A szorzás jele: *"""



PI = 3.14
radius = int(input("Add meg a kör sugarát cm-ben: "))
kerulet = PI * 2 * radius
terulet = PI * radius * radius

print(f"Kerület: {kerulet} cm")
print(f"Terület: {terulet} cm²")

while True:
    valasz = input("Szeretnél kerekíteni? (Igen/Nem): ").strip().lower()
    
    if valasz == "igen":
        print(f"Kerekített kerület: {int(kerulet)} cm")
        print(f"Kerekített terület: {int(terulet)} cm²")
        print("A művelet elvégezve.")
        break
    elif valasz == "nem":
        print("A művelet elvégezve.")
        break
    else:
        print("Érvénytelen válasz. Kérlek, írd be: Igen vagy Nem.")