from matrices import Matrices
import sympy as sp

macierze = [('M', Matrices.M.value), ('N', Matrices.N.value)]

for nazwa, Y in macierze:
    print(f"{'='*25} MACIERZ {nazwa} {'='*25}")
    n = Y.rows
    eigenvals = Y.eigenvals()

    for lam_val, mult in eigenvals.items():
        print(f"\n--- Wartość własna \u03bb = {lam_val} (krotność alg.: {mult}) ---")

        I = sp.eye(n)
        A = Y - lam_val * I

        wymiary_jader = [0]
        k = 1
        while True:
            dim_ker = len((A ** k).nullspace())
            wymiary_jader.append(dim_ker)

            if dim_ker == mult or (k > 1 and wymiary_jader[k] == wymiary_jader[k - 1]):
                break
            k += 1

        print(f"Ciąg wymiarów jąder d_k: {wymiary_jader[1:]}")

        d = wymiary_jader + [wymiary_jader[-1]]
        print("Struktura klatek dla \u03bb = {}:".format(lam_val))
        istnieja_klatki = False
        for i in range(1, len(d) - 1):
            liczba_klatek = 2 * d[i] - d[i - 1] - d[i + 1]
            if liczba_klatek > 0:
                print(f"   -> {liczba_klatek} klatka/i o rozmiarze {i}x{i}")
                istnieja_klatki = True
        if not istnieja_klatki:
            print("   -> Brak klatek (błąd obliczeń)")

    print(f"\n--- Weryfikacja końcowa dla macierzy {nazwa} (postać Jordana) ---")
    P, J = Y.jordan_form()
    sp.pprint(J)
    print("\n")