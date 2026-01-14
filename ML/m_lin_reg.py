import numpy as np
REPEATS = 10000

X=[]
y=[]

n = int(input("Ile przykładów: "))
m = int(input("Ile parametrów: "))

for _ in range(n):
    X.append(np.array([int(input(f"Wpisz parametr nr {i+1}: ")) for i in range(m)]))
    y.append(int(input("Wpisz oczekiwany wynik: ")))

X = np.array(X)
y = np.array(y)

# feature scaling
X_mean = np.mean(X, axis = 0)
X_std = np.std(X, axis = 0)
X_norm = (X - X_mean)/(X_std + 1e-8)

# multiple gradient descent
alf = 0.01
W = np.zeros(m)
b = 0
for j in range(REPEATS):
    tmp_W = np.zeros(m)
    tmp_b = 0
    for i in range(n):
        error = np.dot(W, X_norm[i]) + b - y[i]
        tmp_W += error * X_norm[i]
        tmp_b += error
    print(np.linalg.norm(tmp_W), abs(tmp_b), sep=' ')
    if np.linalg.norm(tmp_W) / n < 0.005 and abs(tmp_b) / n < 0.005:
        print(f"Wykonano {j} powtorzen")
        break
    W -= alf * tmp_W / n 
    b -= alf * tmp_b / n

# tests
k = int(input("Ile testow chcesz sprawdzic: "))
for _ in range(k):
    X_test = np.array([int(input(f"Wpisz parament nr {i+1}: ")) for i in range(m)])
    X_test_norm = (X_test - X_mean)/(X_std + 1e-8)
    print(f"Przewidywany wynik to {(np.dot(W, X_test_norm) + b):.2f}")