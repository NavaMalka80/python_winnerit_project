import pytest
from source.discount_calculator import calculate_discount

#בדיקת פרמטרים שונים
@pytest.mark.parametrize("price, discount_percent, expected",[
    (100,10,90),
    (200,25,150),
    (50,0,50),
    (0,50,0)
])
def test_calculate_discount(price,discount_percent,expected):
    assert calculate_discount(price,discount_percent) == expected

#בדיקת חריגה ערכים שליליים
@pytest.mark.parametrize("price, discount_percent",[
    (-100,10),
    (200,-25),
    (5-0,0)
])
def test_calculate_discount_raises_error(price,discount_percent):
    with pytest.raises(ValueError, match="Price and discount must be non-negative"):
        calculate_discount(price,discount_percent)