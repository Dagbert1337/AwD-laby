from matrices import Matrices
import sympy as sp

print("Ciągi wymiarów jąder potęg macierzy (X - \u03bbI):")
print("(stabilizacja następuje po osiągnięciu wymiaru 5)\n")

for m in Matrices:
    if m.name == 'H':
        break
    X = m.value
    lam_val = -1
    I = sp.eye(5)
    M = X - lam_val * I

    wymiary = []
    k = 1
    poprzedni_wymiar = -1
    obecny_wymiar = 0

    while obecny_wymiar < 5:
        potega_M = M ** k
        obecny_wymiar = 5 - potega_M.rank()
        wymiary.append(obecny_wymiar)

        if obecny_wymiar == poprzedni_wymiar:
            break

        poprzedni_wymiar = obecny_wymiar
        k += 1

    print(f"Macierz {m.name}: {wymiary}")

print(f"""
{'='*10} ZALEZNOSC WIELKOSCI KLATEK OD WZROSTU JADER {'='*10}

Niech d_k oznacza wymiar jadra k-tej potegi:
d_k = dim ker( (X - \u03bb * I)**k ), gdzie przyjmujemy d_0 = 0.

Zaleznosci wielkosci klatek Jordana prezentuja sie nastepujaco:
1. Pierwsza roznica: (d_k - d_{k-1})
   Mowi nam, ile jest klatek Jordana o rozmiarze CO NAJMNIEJ k.

2. Druga roznica (dokladna liczba klatek):
   Aby znalezc liczbe klatek o rozmiarze DOKLADNIE k, odejmujemy 
   od siebie dwa kolejne przyrosty:
   liczba_klatek(k) = (d_k - d_{k-1}) - (d_{k+1} - d_k)
   liczba_klatek(k) = 2 * d_k - d_{k-1} - d_{k+1}
   
{'='*65}
""")