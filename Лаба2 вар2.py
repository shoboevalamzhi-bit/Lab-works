import math

def find_root(x_start, tol, max_iter):
    x = x_start
    k = 0
    while k < max_iter:
        x = math.log(3 * x)
        k += 1
        a = math.exp(x) - 3 * x
        if abs(a) < tol:
            break
    return x, k, a

x1, k, a = find_root(1.0, 0.0001, 100)
print("Уравнение Корень: x = %.4f" % x1)
print("Количество итераций:", k)
print("f(%.4f) = %.5f" % (x1, abs(a)))
