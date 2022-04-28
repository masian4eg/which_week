import unittest

import code_test


class WeekTest(unittest.TestCase):

    def test_week(self): # тест корректного ввода данных
        self.assertEqual(code_test.which_week(31, 12, 2020), 'Номер недели\n106')

    def test_type(self): # тест некорректного ввода данных
        self.assertEqual(code_test.which_week(31, '12', 'elephant'), 'Не верный формат даты')

    def test_value(self): # тест неправильных чисел
        self.assertEqual(code_test.which_week(123, -5, 2019), 'Не верный формат чисел')

    def test_year(self): # тест разрешенного диапазона 2019-2022 годов
        self.assertEqual(code_test.which_week(31, 10, 2015),
                         'Введена не верная дата. Введите любую дату в промежутке 2019-2022 годов')


if __name__ == '__main__':
    unittest.main()
