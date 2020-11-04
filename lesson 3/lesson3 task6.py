# lesson1 task6
def my_func(c):
    return c

a = str(input(f'Введите слово литинскими буквами: '))
b = 0
for i in range(0, len(a)):
    if ord(a[i]) >= 97 and ord(a[i]) <= 122:
        b = b+1
if b == len(a):
    print(my_func(a.title()))