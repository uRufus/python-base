'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе
определить параметры, общие для приведенных типов. В классах-наследниках реализовать
параметры, уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы,
отвечающие за приём оргтехники на склад и передачу в определенное
подразделение компании. Для хранения данных о наименовании и
количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации
вводимых пользователем данных. Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте
«Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
'''


class Warehouse:
    stocks = {}

    def move_to_stock(self, title: str, qty: int):
        if title in self.stocks:
            self.stocks[title]["stock"] += qty
        else:
            self.stocks.update({title: {"stock": qty}})
        return self.stocks

    def move_to_office(self, title: str, qty: int, office_dep: str):
        if title in self.stocks:
            if self.stocks[title]["stock"] >= qty:
                if "office" in self.stocks[title]:
                    if office_dep in self.stocks[title]["office"]:
                        self.stocks[title]["office"][office_dep] += qty
                    else:
                        self.stocks[title]["office"][office_dep] = qty
                else:
                    self.stocks[title].update({"office": {office_dep: qty}})
                self.stocks[title]["stock"] -= qty
                return self.stocks
            else:
                print(f"Не хватает количества товара {title} на складе. "
                      f"Остаток на складе: {self.stocks[title]['stock']}")
        else:
            print(f"Нет товара {title} на складе")


class OfficeEquipment:

    def __init__(self, title: str, height: int, length: int, width: int, weight: int):
        self.title = title
        self.height = height
        self.length = length
        self.width = width
        self.weight = weight


class Printer(OfficeEquipment):
    ink_volume = 100


class Scanner(OfficeEquipment):
    scans_per_min = 5


class Xerox(OfficeEquipment):
    copies_per_min = 10


printer = Printer("printer", 30, 40, 50, 60)
scanner = Scanner("scanner", 40, 50, 60, 70)
warehouse1 = Warehouse()
warehouse1.move_to_stock(printer.title, 2)
warehouse1.move_to_stock(scanner.title, 3)
print(warehouse1.stocks)
warehouse1.move_to_office(printer.title, 1, "IT department")
print(warehouse1.stocks)
warehouse1.move_to_office(printer.title, 1, "IT department")
print(warehouse1.stocks)
warehouse1.move_to_office(printer.title, 1, "IT department")
print(warehouse1.stocks)