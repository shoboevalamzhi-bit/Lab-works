import math

x = 1.0 
tol = 0.0001
k = 0

while True:
    x = math.log(3 * x)
    k += 1
    a = math.exp(x) - 3 * x
    if abs(a) < tol:
        x = x
        break
    x1 = x

print(f"Уравнение Корень: x = {x1:.4f}")
print(f"Количество итераций: {k}")
print(f"f({x1:.4f}) = {abs(a):.5f}")
