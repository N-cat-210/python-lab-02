import math
import sys

if __name__ == "__main__":
    x = float(input("x (от 0.1 до 1): "))
    if not 0.1 <= x <= 1:
        print("Ошибка: требуется 0.1 <= x <= 1")
        sys.exit(1)

    euler_gamma = 0.5772156649015329
    eps = 1e-10
    max_terms = 1000
    
    k = 1

    term = (x ** 2) / 4.0
    total = term

    while term > eps:
        if k >= max_terms:
            print("Превышен предел числа членов ряда")
            sys.exit(1)
            
        term *= (x ** 2) * (2 * k) / ((2 * k + 1) * (2 * k + 2) ** 2)
        k += 1
        total += term

    result = euler_gamma + math.log(x) + total

    print(f"Chi({x}) = {result:.10f}")
    print(f"Членов ряда: {k}")
    print(f"Оценка остатка ряда: {term:.3e}")