# Task 1

vitanya = "Hello, Python World!"
print(vitanya)

# Task 2

a = int(input("Ведіть перше ціле число: "))
b = int(input("Ведіть друге ціле число: "))

print(f"Результат додавання ваших чисел: {a+b}")
print(f"Результат віднімання ваших чисел: {a-b}")
print(f"Результат множення ваших чисел: {a*b}")
print(f"Результат ділення ваших чисел: {a/b}")
print(f"Результат цільночисельного ділення ваших чисел: {a//b}")

# Task 3

words_1 = input("Введіть перше речення: ")
words_2 = input("Введіть друге речення: ")
words_all = words_1 + " " + words_2

print(f"Те що ви ввели: {words_all} \nДовжина ваших рядків: {len(words_all)}")

# Task 4

number = int(input("Введіть число: "))

if number%2 == 0:
    print("Парне")
else:
    print("Непарне")

# Task 5

for i in range(1, 11):
    print (i)

# Task 6

num = int(input("Введіть ціле число: "))

if num > 0:
    print("Позитивний")
elif num < 0:
    print("Негативний")
else:
    print("Нуль")

# Task 7

for i in range(2, 11, 2):
    print (i)

# Task 8

n = int(input("Введіть число: "))
list_n = []

for i in range(1,n):
     list_n.append(i)

print(f"Сума від 1 до {n} не включно - {sum(list_n)}")

# Task 9

for i in range(10, 0, -1):
    print (i)

# Task 10

for i in range(1, 11):
    if i == 5:
        continue
    if i == 7:
        break
    print(i)