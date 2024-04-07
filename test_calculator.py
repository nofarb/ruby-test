# test_calculator.py
import pytest
from calculator import Calculator

def test_add(): 
    calc = Calculator()
    assert calc.add(2, 4) == 6
