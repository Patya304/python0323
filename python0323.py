lista = [10,5,6,7,2]
fib = [0,1]
'''
Egész számok listájának átlaga:
Írj egy függvényt, amely egy egész számokból álló listát kap, majd visszaadja a lista átlagát.
'''
def num_listajanak_atlaga(lista):
    szamok = len(lista)
    ossz = sum(lista)
    return ossz / szamok

'''
Páros számok keresése:
Írj egy függvényt, amely egy egész számokból álló listát kap, majd visszaadja a páros számok listáját.
'''
def par_szamok_keresese(lista):
    paros = []
    for szam in lista:
        if szam % 2 == 0:
            paros.append(szam)
    return paros

'''
Fibonacci sorozat:
Írj egy függvényt, amely egy egész számot kap, majd visszaadja a Fibonacci sorozat első n elemét.
'''
def fibonacci_sorozat():
    n = int(input("szamot: "))
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return print(fib)
fibonacci_sorozat()

'''
Szám faktoriálisa:
Írj egy függvényt, amely egy egész számot kap, majd visszaadja az adott szám faktoriálisát.
'''
def szam_faktorialisa(valami):
    k = 1
    for i in range(1, valami + 1):
        k = k * i
    return k
print(szam_faktorialisa(5))

'''
Legnagyobb elem keresése:
Írj egy függvényt, amely egy egész számokból álló listát kap, majd visszaadja a lista legnagyobb elemét.
'''

'''
Szövegben szereplő szavak számolása:
Írj egy függvényt, amely egy szöveget kap, majd visszaadja, hogy hány szó van a szövegben.
'''

'''
Egész számok listájának összege:
Írj egy függvényt, amely egy egész számokból álló listát kap, majd visszaadja a lista összegét.
'''

'''
Prímszámok keresése:
Írj egy függvényt, amely egy egész számot kap, majd visszaadja a prímszámok listáját, amelyek kisebbek vagy egyenlőek az adott számnál.
'''

'''
Szóközök eltávolítása:
Írj egy függvényt, amely egy szöveget kap, majd visszaadja a szöveget a szóközök eltávolítása után.
'''

'''
Szöveg megszámlálása:
Írj egy függvényt, amely egy szöveget és egy karaktert kap, majd visszaadja, hogy hány alkalommal szerepel a karakter a szövegben.
'''

'''
Szöveg megfordítása:
Írj egy függvényt, amely egy szöveget kap, majd visszaadja a szöveg megfordított verzióját.
'''


'''
Szöveg cseréje:
Írj egy függvényt, amely egy szöveget, egy régi karaktert és egy új karaktert kap, majd visszaadja a szöveget a régi karakterek új karakterre cserélése után.
'''

'''
Számok száma
Írj egy függvényt, amely megszámolja az adott listában található számok számát, majd visszaadja azt.
'''

'''
Legnagyobb szám megtalálása
Írj egy függvényt, amely megtalálja az adott listában található legnagyobb számot, majd visszaadja azt.
'''
