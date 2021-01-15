'''Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
 и выведите в формате чч:мм:сс.
 Используйте форматирование строк.'''
user_input = int(input("Введите количество секунд "))
hours = user_input // 3600
if hours > 24:
    hours %= 24
minutes = (user_input % 3600) // 603
seconds = (user_input % 3600) % 60
print(f"Время {hours}:{minutes}:{seconds}")