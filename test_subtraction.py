# /test_subtraction.py
import pytest
from calculator import Calculator

def test_subtraction():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2
