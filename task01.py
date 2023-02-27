# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению
import random
list_len = int(input("Введите длину списка: "))
list = []
for i in range(list_len):
    list.append(random.randint(1, 100))
print(list)
count = 0
number = int(input("Введите искомое число: "))
for element in list:
    if element == number:
        count += 1
print(f"Число {number} встречается в списке {count} раз")


