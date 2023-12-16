import pytest

from day1 import get_list_of_strings


def test_all_strings_have_length_two():
    assert all(2 == len(y) for y in get_list_of_strings())
