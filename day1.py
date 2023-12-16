import os
import re

dir_path = os.path.dirname(os.path.realpath(__file__))


def get_list_of_strings():
    """Reads input file and returns list of two-digit strings"""
    data_file = os.path.join(dir_path, 'data\\day1_input.txt')
    with open(data_file, 'r') as f:
        for line in f:
            digits = re.findall(r'\d', line)
            yield digits[0] + digits[-1]


def get_sum_of_two_digit_numbers():
    return sum(int(x) for x in get_list_of_strings())


if __name__ == '__main__':
    print("Sum of strings:", get_sum_of_two_digit_numbers())
