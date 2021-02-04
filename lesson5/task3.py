'''
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
'''
ave_salary = 0
low_cost_employees = []
SALARY_BORDER = 20000
with open("task3.txt", "w", encoding="utf-8") as file:
    number_of_employees = int(input("Введите количество  сотрудников: "))
    for i in range(number_of_employees):
        employee = input("Введите фамилию сотрудника: ")
        salary = float(input("Введите зарплату сотрудника: "))
        file.write(f"{employee} {salary} \n")
        if salary < SALARY_BORDER:
            low_cost_employees.append(employee)
        ave_salary += salary
    ave_salary /= number_of_employees

print(f"Сотрудники с низкой зарплатой:  {low_cost_employees} "
      f"Средняя зарплата сотрудников: {ave_salary}")
