#Вариант 4
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if a>b>c:
    print(f"{c},{b},{a}")
    print(f"{a},{b},{c}")
if a>c>b:
    print(f"{b},{c},{a}")
    print(f"{a},{c},{b}")
if b>a>c:
    print(f"{c},{a},{b}")
    print(f"{b},{a},{c}")
if b>c>a:
    print(f"{a},{c},{b}")
    print(f"{b},{c},{a}")
if c>a>b:
    print(f"{b},{a},{c}")
    print(f"{c},{a},{b}")
if c>b>a:
    print(f"{a},{b},{c}")
    print(f"{c},{b},{a}")
