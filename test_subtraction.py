# /test_subtraction.py
import pytest
from calculator import Calculator

def test_subtraction():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2

def test_subtraction2():
    calc = Calculator()
    time.sleep(14)  

    assert calc.subtract(6, 3) == 3
