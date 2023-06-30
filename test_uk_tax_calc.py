"""
Function to test the tax calculation solution in uk_tax_calc.py
"""

from uk_tax_calc import tax_calc1, tax_calc2, tax_calc3, tax_calc4

"""TEST CYCLE 1"""

def test_tax_calc1():
    # 1. Define first failing test for the tax calculator method
    assert tax_calc1(1) == 0


# define second test
def test_tax_calc2():
    # 2. Define the tax calculation and get a GREEN test
    assert tax_calc1(2000) == 0


"""TEST CYCLE 2 """

def test_tax_calc3():
    # test other values including negatives
    assert tax_calc2(1) == 0


def test_tax_calc4():
    assert tax_calc2(2000) == 0


def test_tax_calc5():
    # test negatives
    assert tax_calc2(-2000) == None


def test_tax_calc6():
    """TEST CYCLE 3"""
    assert tax_calc3(12000) == 0

def test_tax_calc7():
    """TEST CYCLE 4"""
    assert tax_calc4(12001) == 0.2
