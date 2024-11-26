import pytest
from source.discount_calculator import calculate_discount

@pytest.fixture
def base_price():
    return 100

@pytest.mark.parametrize("discount_percent,expected", [
    (10,90),
    (25,75),
    (0,100)
])
def test_calculate_discount(base_price, discount_percent,expected):
    assert calculate_discount(base_price,discount_percent) == expected
