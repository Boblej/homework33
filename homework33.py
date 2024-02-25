# задача
# напиши тестовые сценарии для данной функции и протестируйте ее при помощи pytest
# def calculate_average(numbers: List[float]) -> float:
#     """
#     Вычисляет среднее значение списка чисел.

#     :param numbers: Список чисел
#     :return: Среднее значение
#     """
#     if not numbers:
#         raise ValueError("Список чисел не должен быть пустым")

#     return sum(numbers) / len(numbers)

import pytest

def test_calculate_average_positive_numbers():
    numbers = [1, 2, 3, 4, 5]
    expected_average = 3
    assert calculate_average(numbers) == expected_average

def test_calculate_average_negative_numbers():
    numbers = [-1, -2, -3, -4, -5]
    expected_average = -3
    assert calculate_average(numbers) == expected_average

def test_calculate_average_zero():
    numbers = [0, 0, 0, 0, 0]
    expected_average = 0
    assert calculate_average(numbers) == expected_average

def test_calculate_average_empty_list():
    numbers = []
    with pytest.raises(ValueError):
        calculate_average(numbers)

def test_calculate_average_float_numbers():
    numbers = [1.1, 2.2, 3.3, 4.4, 5.5]
    expected_average = 3.3
    assert calculate_average(numbers) == pytest.approx(expected_average)
