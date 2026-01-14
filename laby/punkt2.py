import random

def zapis_do_pliku(dzien, kurs, rekord):
    with open("wyniki.txt", "w") as wyniki:
        wyniki.writelines([str(dzien)+'\n', str(kurs)+'\n', str(rekord)+'\n'])
    print("Wyniki zapisano do pliku 'wyniki.txt'.")

def rysuj_wykres(x, czy_rekord):
    print(f"{x:>5.1f}|", end="")
    tmp = '#'
    print(int(x/10) * tmp, end=" ")
    if czy_rekord:
        print("STONKS")
    else:
        print()

def nowy_kurs(x_prev, x_prev2, e): #musialem, niestety polecenie wymaga, w chuj zbedne
    return (x_prev+x_prev2)/2 + random.uniform(-e, e)

def sim(x0, x1, e, rekord, cnt, rys):
    x2 = nowy_kurs(x0, x1, e)
    czy_rekord = False
    if x2 > rekord:
        rekord = x2
        czy_rekord = True
        cnt+=1
    if rys:
        rysuj_wykres(x2, czy_rekord)
    return x1, x2, rekord, cnt

def interactive(e):
    x0 = random.randint(20,60)
    x1 = random.randint(20,60)
    rekord = 0
    cnt = 0
    dzien = 1
    while True:
        n = int(input("Podaj liczbe dni: (0 - zapis do pliku, <0 - koniec): "))
        if n < 0:
            exit()
        if n == 0:
            zapis_do_pliku(dzien, x1, rekord)
            continue
        dzien += n
        rekord = max(x0, x1, rekord)
        for _ in range(n):
            x0, x1, rekord, cnt = sim(x0, x1, e, rekord, cnt, 1)
        print(f"Bieżący kurs: {x1:.2f}, maksymalny kurs: {rekord:.2f}. Liczba rekordów: {cnt}")

def non_interactive(e):
    N = int(input("Podaj liczbę symulacji: "))
    x0 = random.randint(20,60)
    x1 = random.randint(20,60)
    suma_rekordow = 0
    for _ in range(N):
        record = 0
        cnt = 0
        for _ in range(200):
            x0, x1, record, cnt = sim(x0, x1, e, record, cnt, 0)
        suma_rekordow += cnt
    print(f"Średnia liczba rekordów w {N} symulacjach: {suma_rekordow/N:.2f}")
        

def main():
    #random.seed(2026)
    tryb = str(input("Tryb interaktywny? (t/n): "))
    e = int(input("Podaj parametr e (dodatnia liczba rzeczywista): "))
    if tryb == "t":
        interactive(e)
    elif tryb == "n":
        non_interactive(e)
    
    

if __name__ == "__main__":
    main()