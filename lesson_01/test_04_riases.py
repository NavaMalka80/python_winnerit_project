import pytest

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 2 / 0
    assert str(e.value) in 'division by zero'
    assert str(e.typename) in 'ZeroDivisionError'