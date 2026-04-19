from app.calc import Calculator


class TestCalculator:

    def setup_method(self):
        self.calc = Calculator()

    # сложение
    def test_add_positive(self):
        assert self.calc.adding(5, 3) == 8

    # вычитание
    def test_subtract_positive(self):
        assert self.calc.subtraction(10, 4) == 6

    # умножение
    def test_multiply_positive(self):
        assert self.calc.multiply(6, 7) == 42

    # деление
    def test_divide_positive(self):
        assert self.calc.division(15, 3) == 5