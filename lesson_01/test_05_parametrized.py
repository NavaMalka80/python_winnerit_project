import pytest

def test_multiply_two_positive_ints():
    assert 2 * 3 == 6
def test_multiply_identity():
    assert 1 * 99 == 99
def test_multiply_zero() :
    assert 0 * 100 == 0

def test_with_negative_number():
    assert -1 * 100 == -100

test_data = [(1, 5, 6), (10, 5, 15), (1, 0, 1), (20, 40,60),(10,500, 510)]

@pytest.mark.parametrize("num_1, num_2, result", test_data)
def test_sum_parameters(num_1, num_2, result):
    assert num_1 + num_2 == result

@pytest.mark.parametrize("expected_username, actual_username", [("qwerty", "qwerty"), ("Qwerty", "qwerty"), ("abc","abc")])
def test_string_parameters(expected_username, actual_username):
    assert expected_username. lower() == actual_username. lower()
