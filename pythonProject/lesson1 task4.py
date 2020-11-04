s = int(input("Введите число? "))
print(s)
a0 = 0
maxn = 0
while s % 10 != 0:
    a = s % 10
    s = s//10
    if a >= a0:
      a0 = a
print(f"Cамая большая цифра в числе {a0} ")