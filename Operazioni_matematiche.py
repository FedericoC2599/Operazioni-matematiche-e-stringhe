import math as m

#Funzioni matematiche

def pari(x):
    return (x % 2 == 0)

def divisibile(x,y):
    return (x % y == 0)

def potenze(start,end,potenza_min,potenza_max):
    for x in range(start, end):
        for n in range (potenza_min,potenza_max):
            print(x ** n, end="")
        print()


def somma_da_input():
    while True:
        val=int(input("Valore da sommare: "))

        if val==0:
            break
        else:
            somma=somma + val

    print("Somma finale ",somma)

def range_potenze(NMAX,XMAX):
    for n in range(1, NMAX +1):
        print("%10d" % n, end="")

    print()

    for n in range(1, XMAX +1):
        print("%10s" % "x ",end="")

    print("\n"," ","-"*40)

    for x in range(1, XMAX +1):
        for n in range(1, NMAX+1):
            print("%10.0f" % x ** n, end="")
        print()