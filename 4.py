# ? boolean / bool / логический тип
bool_1 = True
print(bool_1, type(bool_1))
bool_2 = False
print(bool_2, type(bool_2))

# ? логические операторы
print(5 > 3) # больше
print(4 >= 2) # больше или равно
print(3 < 1) # меньше
print(10 <= 3) # меньше или равно
print(10 == 3) # равно
print(10 != 3) # не равно

# ? условные операторы
num = -10
if num > 0:
    print("Число положительное")
else:
    print("Число отрицательное")

# ? число четное
num = 5
if num % 2 == 0:
    print("Число четное")
else:
    print("Число нечетное")

# ? if-elif-else
color = "green"
if color == "green":
    print("Едим")
elif color == 'red':
    print("Стой")
else:
    print("Ждем")

# ()
# not - не
# and - и
# or - или

# ? задачи
x   = True
y   = False
z   = True
print(x or y and z)
print(x and y or x)
print(not x or y and z)
print(not x and not y or z)
print(x and x or y and x or x)
print((x or y) and (not z))




