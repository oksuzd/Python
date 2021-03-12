"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например, словарь.

6. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""


class Warehouse:

    def __init__(self, location):
        self.location = location
        self.warehousing = {}

    def __str__(self):
        return f'Склад по адресу: {self.location}'

    def appliances_income(self):
        """приём оргтехники на склад"""
        app_1 = Printer("HP Laser 107a", 6999, False)
        self.warehousing.update({f'{app_1.name}': 5})
        app_2 = Scanner("Canon CanoScan LiDE 400", 6499, "A4")
        self.warehousing.update({f'{app_2.name}': 7})
        app_3 = Xerox("HP LaserJet Pro 400 M428dw", 29699, 38)
        self.warehousing.update({f'{app_3.name}': 2})

    def availability(self):
        """что хранится на складе"""
        self.appliances_income()
        self.__str__()
        return f'В наличии: {self.warehousing}'


class OfficeAppliances:
    def __init__(self, model_name, price):
        self.name = "Оргтехника"
        self.model_name = model_name
        self.price = price

    def __str__(self):
        return f'{self.name}: {self.model_name}'

    def additional_params(self):
        pass

    def show_info(self):
        return f'{self.__str__()}\nЦена: {self.price} руб.\n{self.additional_params()}\n'


class Printer(OfficeAppliances):
    def __init__(self, model_name, price, color_print=False):
        super().__init__(model_name, price)
        self.name = "Принтер"
        self.color_print = color_print

    def additional_params(self):
        if self.color_print:
            return 'Цветная печать: Да.'
        else:
            return 'Цветная печать: Нет.'


class Scanner(OfficeAppliances):
    def __init__(self, model_name, price, max_paper_format):
        super().__init__(model_name, price)
        self.name = "Сканнер"
        self.max_paper_format = max_paper_format

    def additional_params(self):
        return f'Максимальный формат бумаги: {self.max_paper_format}.'


class Xerox(OfficeAppliances):
    def __init__(self, model_name, price, copy_speed):
        super().__init__(model_name, price)
        self.name = "Копировальная машина"
        self.copy_speed = copy_speed

    def additional_params(self):
        return f'Скорость копирования: {self.copy_speed} стр/мин.'


wh_1 = Warehouse("ул. Ленина, 3")
print(wh_1)
print(wh_1.availability())
