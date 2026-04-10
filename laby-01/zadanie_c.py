from matrices import Matrices
import sympy as sp

LAMBDA_VAL = -1 # zakladamy lambda = -1 z zadania A
N = 5  # rozmiar macierzy 5x5
I = sp.eye(N)

print(f"Obliczanie wymiaru jądra macierzy (X - \u03bbI) dla \u03bb = {LAMBDA_VAL}:")
print("-" * 50)

for m in Matrices:
    if m.name == 'H':
        break
    # lambda = -1, wiec X - (-1)I = X + I
    M = m.value - (LAMBDA_VAL * I)
    rzad = M.rank()
    wymiar_jadra = N - rzad

    print(f"Macierz {m.name}: wymiar jądra = {wymiar_jadra}  (rząd = {rzad})")