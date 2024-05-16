from typing import List


def find_average(numbers: List[int]) -> float:
    sum_numbers = 0
    for number in numbers:
        sum_numbers += number
    return sum_numbers / len(numbers)
