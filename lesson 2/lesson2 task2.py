# lesson2 task2
my_list0 = input('Привет! Введите значения для списка через пробел: ') #my_list0 = int(i) for i in input().split()]
my_list1 = my_list0.split()
my_list2 = list()
n=len(my_list1)
for i in range(0, len(my_list1)-1, 2):
    my_list2.insert(i, my_list1[i+1])
    my_list2.insert(i+1, my_list1[i])
if (((len(my_list1))%1)==0):
    my_list2.append(my_list1[n-1])
print(f'Список который вы ввели: {my_list1}')
print(f'Список c обменивающимися элементами с индексами 0 и 1, 2 и 3 и т.ди: {my_list2}')

