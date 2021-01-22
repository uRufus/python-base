'''2. Для списка реализовать обмен значений соседних элементов, т.е.
 Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
  При нечетном количестве элементов последний сохранить на своем месте.
  Для заполнения списка элементов необходимо использовать функцию input().'''

# Вариант 1

new_list = []
last_element = []
even_element = 0
list_of_elements = []
while True:
    element = input("Вариант 1. Введите значение в список элементов. Чтобы закончить ввод нажмите 'Enter': ")
    if element != '':
        list_of_elements.append(element)
    else:
        break
print(list_of_elements)
if len(list_of_elements) < 2:
    print(list_of_elements)
else:
    if len(list_of_elements) % 2 != 0:
        last_element = list_of_elements.pop()
    while even_element < len(list_of_elements):
        new_list.append(list_of_elements[even_element + 1])
        new_list.append(list_of_elements[even_element])
        even_element += 2
    if last_element:
        new_list.append(last_element)
    print(new_list)

# Вариант 2
list_of_elements = []
while True:
    element = input("Вариант 2. Введите значение в список элементов. Чтобы закончить ввод нажмите 'Enter': ")
    if element != '':
        list_of_elements.append(element)
    else:
        break
odd_count = 1
even_list = []
odd_list = []
new_list = []
index = 0
print(list_of_elements)
for element in list_of_elements:
    if odd_count % 2 == 1:
        even_list.append(element)
    else:
        odd_list.append(element)
    odd_count += 1
while index < len(odd_list):
    new_list.append(odd_list[index])
    new_list.append(even_list[index])
    index += 1
if len(odd_list) < len(even_list):
    new_list.append(even_list[index])
print(new_list)

# Вариант 3
list_of_elements = []
while True:
    element = input("Вариант 3. Введите значение в список элементов. Чтобы закончить ввод нажмите 'Enter': ")
    if element != '':
        list_of_elements.append(element)
    else:
        break
print(list_of_elements)
if len(list_of_elements) % 2 == 0:
    list_of_elements[::2], list_of_elements[1::2] = list_of_elements[1::2], list_of_elements[::2]
    print(list_of_elements)
else:
    last_element = list_of_elements.pop()
    list_of_elements[::2], list_of_elements[1::2] = list_of_elements[1::2], list_of_elements[::2]
    list_of_elements.append(last_element)
    print(list_of_elements)
