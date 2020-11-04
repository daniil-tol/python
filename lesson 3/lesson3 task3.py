# lesson1 task3
def my_func(x, y, z):
    a = [x, y, z]
    min_1 = min(a)
    a.remove(min_1)
    print(sum(a))
print(my_func(float(input("Укажите первое число: ")), float(input("Укажите второе число: ")), (float(input("Укажите третье число: ")))))