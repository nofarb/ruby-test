# test_calculator.py
import pytest
import time
from calculator import Calculator

def test_add(): 
    calc = Calculator()
    time.sleep(10)  
    assert calc.add(3, 4) == 7
    
def test_long_running_one():
    # Simulating a long process
    print("Test 1 is running, simulating a long process...")
    time.sleep(25)  # Sleep for 120 seconds (2 minutes)
    assert True  # Simulating a successful test
