"""
Function to test the tax calculation solution in uk_tax_calc.py
"""

from uk_tax_calc import tax_calc1, tax_calc2

# 1. Define first failing test for the tax calculator method
# 2. Define the tax calculation and get a GREEN test
def test_tax_calc1():
    assert tax_calc1(1) == 0

# define second test
def test_tax_calc2():
    assert tax_calc1(2000) == 0

# test other values including negatives
def test_tax_calc3():
    assert tax_calc2(1) == 0

def test_tax_calc4():
    assert tax_calc2(2000) == 0

def test_tax_calc5():
    assert tax_calc2(-2000) == None