from itertools import chain
import os
import regex as re

dir_path = os.path.dirname(os.path.realpath(__file__))

replacements = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

replacements_escaped = {re.escape(k): v for k, v in replacements.items()}


def get_first_and_last_letter(s: str) -> tuple[str, str]:
    """Return first and last digits."""
    base_pattern = r"|".join(
        chain(replacements_escaped.keys(), replacements_escaped.values(), ["0"])
    )
    start_pattern = re.compile(base_pattern)
    end_pattern = re.compile(base_pattern, re.REVERSE)
    first_found = start_pattern.search(s).group()
    first = replacements_escaped.get(first_found, first_found)
    last_found = end_pattern.search(s).group()
    last = replacements_escaped.get(last_found, last_found)
    return first, last


def get_list_of_strings():
    """Reads input file and returns list of two-digit strings"""
    data_file = os.path.join(dir_path, "data\\day1_input.txt")
    with open(data_file, "r") as f:
        for line in f:
            first, last = get_first_and_last_letter(line)
            two_digit_string = first + last
            print(two_digit_string)
            yield two_digit_string


def get_sum_of_two_digit_numbers():
    return sum(int(x) for x in get_list_of_strings())


if __name__ == "__main__":
    print("Sum of strings:", get_sum_of_two_digit_numbers())
