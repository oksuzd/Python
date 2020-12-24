"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class MyComplexNum:
    def __init__(self, some_tuple):
        self.x = some_tuple[0]
        self.y = some_tuple[1]

    def __add__(self, other_number):
        res = (self.x + other_number.x, self.y + other_number.y)
        return res

    def __mul__(self, other_number):
        res = (self.x * other_number.x - (self.y * other_number.y), self.x * other_number.y + self.y * other_number.x)
        return res

    def __str__(self):
        if self.y > 0:
            return f'{self.x} + {self.y}i'
        elif self.y < 0:
            return f'{self.x} - {abs(self.y)}i'
        elif self.y == 0:
            return f'{self.x}'


complex_1 = MyComplexNum((3, -2))
complex_2 = MyComplexNum((-7, 4))
sum_complex = MyComplexNum(complex_1 + complex_2)
mul_complex = MyComplexNum(complex_1 * complex_2)


print('1 комплексное число:', complex_1)
print('2 комплексное число:', complex_2)
print('Сумма комплексных чисел равна:', sum_complex)
print('Произведение комплексных чисел равно:', mul_complex)
