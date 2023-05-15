import functions
from hermite import hermite
from inspect import getmembers, isfunction
from newton_cotes import newton_INFI

def main():
    while True:
        #funs = getmembers(functions, isfunction)
        ifun = int(input("Wybierz funkcje:(1. x^3+3x^2+2x+1, 2. cos(2x), 3. 2sin(x), 4. |x|, 5. 4x^2+3x+2, 6. Koniec): "))
        if ifun < 1 or ifun > 5:
            return

        #f = funs[ifun][1]
        typ = int(input("wybierz sposób obliczania: (1.Newtona-Cotesa opartą na trzech węzłach 2.Kwadratura Gaussa-Hermite'a):"))

        match typ:
            case 1:

                a = float(input("Podaj krok:"))
                #b = int(input("Podaj koniec przedziału:"))
                precion = float(input("Podaj dokładność:"))
                print(round(newton_INFI(a,ifun,precion),6))
                pass
            case 2:
                print("Na ilu węzłach ma być obliczona całka?[2,3,4,5]")
                nod = int(input())
                if nod < 2 or nod > 5:
                    return
                print(round(hermite(ifun,nod),6))
            case other:
                return

if __name__ == '__main__':
    main()


