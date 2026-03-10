import numpy as np

a = np.matrix([[4, -1, -3, 5, -2],
               [-5, -1, 1, -4, 4],
               [8, -1, -4, 6, -5],
               [1, 0, 0, -1, -1],
               [5, -1, -3, 5, -3]])

b = np.matrix([[-1, 0, -1, 1, 1],
               [-5, -1, 1, -4, 4],
               [3, 0, -2, 2, -2],
               [1, 0, 0, -1, -1],
               [0, 0, -1, 1, 0]])

c = np.matrix([[-9, 1, 2, -5, 6],
               [-2, -1, 0, -2, 2],
               [-5, 1, 1, -4, 3],
               [1, 0, 0, -1, -1],
               [-8, 1, 2, -5, 5]])

d = np.matrix([[-4, 0, 0, -1, 3],
               [-2, -1, 0, -2, 2],
               [0, 0, -1, 0, 0],
               [1, 0, 0, -1, -1],
               [-3, 0, 0, -1, 2]])

e = np.matrix([[0, 0, -1, 2, 0],
               [-3, -1, 1, -2, 2],
               [3, 0, -2, 2, -2],
               [1, 0, 0, -1, -1],
               [1, 0, -1, 2, -1]])

f = np.matrix([[2, 0, -1, 2, -2],
               [-3, -1, 1, -2, 2],
               [3, 0, -2, 2, -2],
               [0, 0, 0, -1, 0],
               [3, 0, -1, 2, -3]])

g = np.matrix([[-1, 0, 0, 0, 0],
               [0, -1, 0, 0, 0],
               [0, 0, -1, 0, 0],
               [0, 0, 0, -1, 0],
               [0, 0, 0, 0, -1]])

print("Wielomiany charakterystyczne a-g:")
print("[x^5|x^4|x^3|x^2|x^1|x^0]")
print(np.poly(a),
      np.poly(b),
      np.poly(c),
      np.poly(d),
      np.poly(e),
      np.poly(f),
      np.poly(g),
      sep="\n")
print()

eigvals_A = np.round(np.linalg.eigvals(a),1).astype(np.int64)
print("Wartości charakterystyczne:")
print(eigvals_A)
print('Czyli jedynym pierwiastkiem wielomianu jest liczba "-1"')