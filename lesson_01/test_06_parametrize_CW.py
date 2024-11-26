import test

import pytest


def add(x,y):
    return  x+y

@pytest.mark.parametrize("x ,y ,expected" ,[(1,2,3),(0,0,0),(-1,1,0),(3,5,8)])
def test_add(x,y,expected):
    assert add(x, y) == expected