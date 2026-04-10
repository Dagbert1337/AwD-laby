from matrices import Matrices
import sympy as sp

print("Sprawdzenie podobieństwa do macierzy blokowej (Postać Jordana):")

for m in Matrices:
    if m.name == 'H':
        break
    P, J = m.value.jordan_form()

    n = J.shape[0]
    superdiag = [J[i, i + 1] for i in range(n - 1)]

    liczba_klatek = n - superdiag.count(1)

    print(f"\n====================")
    print(f"---- Macierz {m.name} ----")
    print(f"====================")
    print("Macierz Jordana (J):")
    sp.pprint(J)
    print(f"\nLiczba klatek Jordana: {liczba_klatek}")