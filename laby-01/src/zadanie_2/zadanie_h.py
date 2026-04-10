from matrices import Matrices
import sympy as sp


macierze_do_sprawdzenia = [('H', Matrices.H.value), ('K', Matrices.K.value)]

for nazwa, Y in macierze_do_sprawdzenia:
    print(f"{'='*25} MACIERZ {nazwa} {'='*25}\n")
    n = Y.rows

    eigenvals = Y.eigenvals()
    lam_val = list(eigenvals.keys())[0]
    print(f"1. Wartość własna \u03bb: {lam_val} (krotność algebraiczna: {eigenvals[lam_val]})")

    I = sp.eye(n)
    M = Y - lam_val * I

    wymiary_jader = [0]
    k = 1

    while True:
        potega_M = M ** k
        wymiar = n - potega_M.rank()
        wymiary_jader.append(wymiar)

        if wymiar == n or (k > 1 and wymiary_jader[k] == wymiary_jader[k - 1]):
            break
        k += 1

    print(f"2. Ciąg wymiarów jąder d_k (od k=1): {wymiary_jader[1:]}")

    wymiary_jader.append(wymiary_jader[-1])

    klatki = {}
    for i in range(1, len(wymiary_jader) - 1):
        ilosc_klatek = 2 * wymiary_jader[i] - wymiary_jader[i - 1] - wymiary_jader[i + 1]
        if ilosc_klatek > 0:
            klatki[i] = ilosc_klatek

    print("   Rozmiary klatek Jordana wywnioskowane z ciągu:")
    for rozmiar, ilosc in klatki.items():
        print(f"   -> {ilosc} klatka/i o rozmiarze {rozmiar}x{rozmiar}")

    print("\n3. Weryfikacja funkcją z systemu algebry (jordan_form):")
    P, J = Y.jordan_form()
    sp.pprint(J)
    print("\n")