'''2. Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.'''


def person_data(name, surname, birth_date, city, email, phone):
    print(f"Ваши данные: Имя: {name} Фамилия: {surname} "
          f"год рождения: {birth_date} город: {city} email: {email} телефон: {phone}")


person_data(name="Daniel", birth_date="22.01.1909",
            city="Moscow", email="ss@ss.ru", phone="19292", surname="Creig")
