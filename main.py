import functions
from hermite import hermite
from inspect import getmembers, isfunction

def main():
    while True:
        funs = getmembers(functions, isfunction)
        ifun = int(input("Wybierz funkcje:(0. x^3+3x^2+2x+1, 1. cos(2x), 2. 2sin(x), 3. |x|, 4. 4x^2+3x+2, 5. Koniec): "))
        if ifun < 0 or ifun > 4:
            return

        f = funs[ifun][1]
        typ = int(input("wybierz sposób obliczania: (1.Newtona-Cotesa opartą na trzech węzłach 2.Kwadratura Gaussa-Hermite'a):"))

        match typ:
            case 1:
                pass
            case 2:
                print("Na ilu węzłach ma być obliczona całka?[2,3,4,5]")
                nod = int(input())
                if nod < 2 or nod > 5:
                    return
                print(round(hermite(f,nod),6))
            case other:
                return

if __name__ == '__main__':
    main()


