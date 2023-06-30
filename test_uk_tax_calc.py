"""
Function to test the tax calculation solution in uk_tax_calc.py
"""

from uk_tax_calc import tax_calc1, tax_calc2, tax_calc3, tax_calc4


def test_tax_calc1():
    """--------------------TEST CYCLE 1------------------------------"""
    # 1. Define first failing test for the tax calculator method
    assert tax_calc1(1) == 0

def test_tax_calc2():
    """ define second test
    2. Define the tax calculation and get a GREEN test"""
    assert tax_calc1(2000) == 0

def test_tax_calc3():
    """--------------------TEST CYCLE 2 ------------------------------"""
    # test other values including negatives
    assert tax_calc2(1) == 0

def test_tax_calc4():
    """ test values below 120001"""
    assert tax_calc2(2000) == 0

def test_tax_calc5():
    """test negatives"""
    assert tax_calc2(-2000) is None


def test_tax_calc6():
    """----------------------TEST CYCLE 3----------------------------"""
    assert tax_calc3(-12000) == 0

def test_tax_calc7():
    """----------------------TEST CYCLE 4----------------------------"""
    assert tax_calc4(12001) == 0.2

def test_tax_calc9():
    """call the assert function on 30,000"""
    assert tax_calc4(30000) == 3600

def test_tax_calc10():
    """call the assert function on boundary values"""
    assert tax_calc4(36000) == 4800  


def test_tax_calc11():
    """---------------------TEST CYCLE 5-----------------------------"""
    # call the assert function on boundary values
    assert tax_calc4(36001) == 4800.4

def test_tax_calc12():
    """call the assert function"""
    assert tax_calc4(37000) == 5200

def test_tax_calc13():
    """call the assert function on income in the lower band"""
    assert tax_calc4(13000) == 200
    
def test_tax_calc14():
    """call the assert function"""
    assert tax_calc4(40000) == 6400

def test_tax_calc15():
    """call the assert function on a high income of 100k"""
    assert tax_calc4(100000) == 30400

def test_tax_calc16():
    """call the assert function on a negative value """
    assert tax_calc4(-2) == 0