import numpy as np
import math

REPEATS = 10000

def wczytaj():
    X = []
    y = []

    m = int(input("Podaj liczbę przykładów: "))
    n = int(input("Podaj liczbę parametrów: "))

    for _ in range(m):
        X.append(np.array([int(input(f"Podaj parametr parametr nr{i}: ")) for i in range(n)]))
        y.append(int(input("Podaj oczekiwany wynik: ")))

    X = np.array(X)
    y = np.array(y)

    return X, y

def normalizuj(X, mean, std):
    return (X - mean)/(std + 1e-8)

def sigmoid(z):
    return 1/(1+pow(math.e, -z))

def koszt(X, y, W, b):
    m = X.shape[0]

    koszt = 0

    for i in range(m):
        f_wb_i = sigmoid(np.dot(W, X[i]) + b)
        koszt += y*np.log(f_wb_i) + (1-y)*np.log(1 - f_wb_i)
    
    return -koszt/m

def regresja_logiczna(X, y):
    m, n = X.shape
    W = np.zeros(m)
    b = 0
    alf = 0.03

    for j in range(REPEATS):
        tmp_W = np.zeros(m)
        tmp_b = 0

        for i in range(n):
            f_wb_i = sigmoid(np.dot(W, X[i]) + b)
            error = f_wb_i - y[i]
            tmp_W += error * X[i]
            tmp_b += error

        if np.linalg.norm(tmp_W)/m < 0.003 and abs(tmp_b)/m < 0.003:
            print(f"Regresja zakończyła się po {j} powtórzeniach.")
            break
        W -= alf * tmp_W / m
        b -= alf * tmp_b / m

    print("Regresja zakończyła się po 10000 powtórzeniach.")
    return W, b

def testuj(W, b, mean, std):
    n = W.shape[0]
    k = int(input("Ile przykładów chcesz sprawdzić: "))

    for _ in range(k):
        X_test = np.array([int(input(f"Podaj parametr nr {i}: ")) for i in range(n)])
        X_test_norm = normalizuj(X_test, mean, std)
        f_wb = sigmoid(np.dot(W, X_test_norm)+b)
        #print(f"Podany przykład jest szukaną wartością na {f_wb}%.")
        print(round(f_wb))
        

def main():
    X, y = wczytaj()

    X_mean = np.mean(X, axis = 0)
    X_std = np.std(X, axis = 0)
    X_norm = normalizuj(X, X_mean, X_std)

    W, b = regresja_logiczna(X_norm, y)

    testuj(W, b, X_mean, X_std)




if __name__ == "__main__":
    main()