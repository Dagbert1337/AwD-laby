import numpy as np

a = np.matrix([[4, -1, -3, 5, -2], [-5, -1, 1, -4, 4], [8, -1, -4, 6, -5], [1, 0, 0, -1, -1], [5, -1, -3, 5, -3]])
print(np.poly(a))

print(np.polynomial.Polynomial.fromroots(np.linalg.eigvals(a)))