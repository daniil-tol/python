seconds = int(input("Введите время в секундах? "))
clock = seconds // 3600
minute = (seconds % 3600) // 60
seconds_2 = (seconds % 3600) % 60


print (f"Введенное время в формате чч:мм:сс -> {clock}:{minute}:{seconds_2}")
# НЕ нашел с помощью, какого синтаксиса f можновывести целое двузначное число?