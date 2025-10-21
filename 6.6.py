n = int(input())
if 1 <= n <= 999:
    p = "чётное" if n % 2 == 0 else "нечётное"
    if n < 10:
        d = "однозначное"
    elif n < 100:
        d = "двузначное"
    else:
        d = "трёхзначное"
    print(p, d, "число")
else:
    print("Ошибка")
