from zadanie_2.matrices import Matrices
import sympy as sp

P, J = Matrices.H.value.jordan_form()

print("\nMacierz przejścia P (realizująca podobieństwo):")
sp.pprint(P)

print("\nPostać klatkowa Jordana J:")
sp.pprint(J)

H_rekonstrukcja = P * J * P.inv()

print("\nWynik mnożenia P * J * P^-1:")
sp.pprint(H_rekonstrukcja)

print()
if Matrices.H.value == H_rekonstrukcja:
    print("Są takie same")
else:
    print("Są różne")
