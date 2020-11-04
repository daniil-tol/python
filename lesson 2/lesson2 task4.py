# lesson2 task4
my_string = input('Bведите строку из нескольких слов, разделённых пробелами: ').split()
print(my_string)
for a in range(len(my_string)):
    if len(str(my_string[a])) <= 10:
        print(f' {a+1} {my_string[a].title()}')
        a += 1
    else:
        print(f' {a+1} {my_string[a][0:10].title()}')
        a += 1