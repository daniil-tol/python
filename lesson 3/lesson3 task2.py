# lesson1 task2
def my_func(name, surname, birth_year, city, email, phone):
    return print(f'{name} {surname} {birth_year} {city} {email} {phone}')
print(my_func(name = str(input("Укажите свое имя: ")), surname = str(input("Укажите свою фамилию: ")), birth_year = str(input("Укажите свой город проживания: ")), city = str(input("Укажите свой город проживания: ")), email = str(input("Укажите свой email: ")), phone = str(input("Укажите свой телефон: "))))