from matrices import Matrices
import sympy as sp

print("Wielomiany charakterystyczne macierzy a-g:")

A = Matrices.A.value.charpoly(sp.symbols('lamda'))
print("A: ", sp.factor(A.as_expr()))

B = Matrices.B.value.charpoly(sp.symbols('lamda'))
print("B: ", sp.factor(B.as_expr()))

C = Matrices.C.value.charpoly(sp.symbols('lamda'))
print("C: ", sp.factor(C.as_expr()))

D = Matrices.D.value.charpoly(sp.symbols('lamda'))
print("D: ", sp.factor(D.as_expr()))

E = Matrices.E.value.charpoly(sp.symbols('lamda'))
print("E: ", sp.factor(E.as_expr()))

F = Matrices.F.value.charpoly(sp.symbols('lamda'))
print("F: ", sp.factor(F.as_expr()))

G = Matrices.G.value.charpoly(sp.symbols('lamda'))
print("G: ", sp.factor(G.as_expr()))

print()

print("Wartości własne w formacie {<wartość>: <ilość wystąpień>, ...}:")
print(Matrices.A.value.eigenvals())
print('Czyli jedyna to liczba "-1"')