print(f"""
{'='*26} UZASADNIENIE {'='*26}
Dla macierzy X o wielu wartosciach wlasnych zachodzi:
dim ker(X - \u03bb * I) = dim ker(J - \u03bb * I).

1. Klatki dla innych wartosci wlasnych (\u03bc ≠ \u03bb):
   Macierz (J_\u03bc(\u03bc) - \u03bb * I) ma na przekatnej (\u03bc - \u03bb) ≠ 0. 
   Jest to macierz odwracalna, wiec wymiar jej jadra wynosi 0.

2. Klatki dla wartosci wlasnej \u03bb:
   Macierz (J_\u03bb(\u03bb) - \u03bb * I) sprowadza sie do klatki J_\u03bb(0).
   Wymiar jadra kazdej takiej pojedynczej klatki to zawsze 1.

WNIOSEK: Wymiar dim ker(X - \u03bb * I) sumuje jadra wszystkich klatek. 
Poniewaz klatki innych wartosci wlasnych daja 0, wynik odpowiada 
dokladnie liczbie klatek Jordana dla wybranej wartosci \u03bb.
{'='*66}
""")