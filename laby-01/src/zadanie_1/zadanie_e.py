from matrices import Matrices
import sympy as sp

print(f"""
{'='*39} HIPOTEZA {'='*39}

Liczba klatek Jordana macierzy X o wartosci wlasnej \u03bb wynosi: dim(ker(X - \u03bb * I)).

{'='*41} DOWOD {'='*41}
1. Lemat:
   Jesli macierze sa podobne (B = P^-1 * A * P), to ich przesuniecia o skalar 
   rowniez: B - \u03bb * I = P^-1 * A * P - P^-1 * (\u03bb * I) * P = P^-1 * (A - \u03bb * I) * P.
   Wniosek: dim( ker(X - \u03bb * I) ) = dim( ker(J - \u03bb * I) ), gdzie J to postac Jordana.
   
2. Dowód właściwy:
   Macierz J - \u03bb * I sklada sie z klatek Jk(0) na przekatnej.
   Kazda klatka Jk(0) ma postac macierzy z zerami na przekatnej i jedynkami 
   tuz nad nia. Wymiar jadra kazdej takiej pojedynczej klatki to zawsze 1.
   
   Suma wymiarow jader wszystkich blokow (czyli dim( ker(J - \u03bb * I) )) musi wiec 
   odpowiadac dokladnie liczbie klatek w macierzy Jordana.
{'='*88}
""")

print("Weryfikacja Lematu i Hipotezy dla macierzy A-G:\n")

for m in Matrices:
    if m.name == 'H':
        break
    X = m.value
    lam_val = list(X.eigenvals().keys())[0]
    n = X.rows
    I = sp.eye(n)

    P, J = X.jordan_form()

    # weryfikacja lematu: czy (X - lambda*I) jest podobne do (J - lambda*I)?
    # czy P^-1 * (X - lambda*I) * P daje (J - lambda*I)?
    lewy_wynik = P.inv() * (X - lam_val * I) * P
    prawy_wynik = J - lam_val * I
    lemat_potwierdzony = lewy_wynik == prawy_wynik

    # weryfikacja hipotezy: czy liczba klatek == dim(ker(X - lambda*I))?
    superdiag = [J[i, i + 1] for i in range(n - 1)]
    liczba_klatek = n - superdiag.count(1)
    wymiar_jadra = (X - lam_val * I).nullspace().__len__()

    hipoteza_potwierdzona = liczba_klatek == wymiar_jadra

    print(f"{'-'*14} Macierz {m.name} {'-'*14}")
    print(f"Lemat (Podobieństwo): {'ZALICZONE' if lemat_potwierdzony else 'BŁĄD'}")
    print(
        f"Hipoteza (Klatki={liczba_klatek}, Jądro={wymiar_jadra}): {'ZALICZONE' if hipoteza_potwierdzona else 'BŁĄD'}")
    print("-" * 40)