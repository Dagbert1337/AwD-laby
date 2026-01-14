def linear_regression(x, y, w, b):
    tmp_w = 0
    tmp_b = 0
    alpha = 0.01
    for i in range(n):
        f_wb = w*x[i] + b
        error = f_wb - y[i]
        tmp_w += error * x[i]
        tmp_b += error
    w -= alpha*tmp_w/n
    b -= alpha*tmp_b/n
    return w, b

x = []
y = []

n = int(input())

for _ in range(n):
    x.append(int(input()))
    y.append(int(input()))

w=0
b=0
for _ in range(1000):
    w, b = linear_regression(x, y, w, b)

m = int(input())
for _ in range(m):
    x_new = int(input())
    y_pred = w * x_new + b
    print(f"{y_pred:.2f}")