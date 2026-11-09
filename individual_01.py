#Вариант 4
n2 = (input("Введите натуральное число: "))
try:
    n1 = float(n2)
    if True:
        n = int(n1)
        if n/n1 != 1:
            print("Ошибка! Вы ввели не натуральное число!")
        else:
            r = n%7
            k=n//7
            if r ==0:
                print(f"{n}=7*{k}")
            else:
                print(f"{n}=7*{k}+{r}")
except ValueError:
    print("Ой, похоже это не число!")