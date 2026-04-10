from matrices import Matrices
import sympy as sp

lamda = sp.Symbol('\u03bb')

print("Wielomiany charakterystyczne macierzy a-g:")
for m in Matrices:
    if m.name == 'H':
        break
    char_poly = m.value.charpoly(lamda)
    print(f"{m.name}: {sp.factor(char_poly.as_expr())}")

print("\nWartości własne w formacie {<wartość>: <ilość wystąpień>, ...}:")
for m in Matrices:
    if m.name == 'H':
        break
    print(f"{m.name}: {m.value.eigenvals()}")