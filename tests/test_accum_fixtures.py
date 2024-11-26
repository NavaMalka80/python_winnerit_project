import pytest
from source.accum import Accumulator

@pytest.fixture
def accum():
    return Accumulator()


def test_new_accum(global_accum):
    assert global_accum.count == 0


def test_add_counts(global_accum):
    global_accum.add_counts()
    assert global_accum.count == 1


@pytest.mark.skip(reason="Broken Test")
def test_add_counts_twice(global_accum):
    global_accum.add_counts()
    global_accum.add_counts()
    assert global_accum.count == 2

@pytest.mark.xfail(reason="Failed because server is down", raises=AssertionError)
def test_add_counts_with_params(accum):
    accum.add_counts(10)
    assert accum.count == 11

@pytest.mark.winnerit
def test_add_counts_and_setter(accum):
    accum.count = 2
    accum.add_counts()
    assert accum.count == 3


def test_get_brand(accum):
    with pytest.raises(AttributeError) as err:
        print(accum.__brand)

    assert str(err.value) == "'Accumulator' object has no attribute '__brand'"
