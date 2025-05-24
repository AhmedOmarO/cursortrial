"""
Test cases for the calculator module.
"""
import pytest
from src.calculator import Calculator

def test_add():
    """Test addition operation."""
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0.1, 0.2) == pytest.approx(0.3)

def test_subtract():
    """Test subtraction operation."""
    calc = Calculator()
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(1, 1) == 0
    assert calc.subtract(-1, -1) == 0

def test_multiply():
    """Test multiplication operation."""
    calc = Calculator()
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-2, 3) == -6
    assert calc.multiply(0, 5) == 0

def test_divide():
    """Test division operation."""
    calc = Calculator()
    assert calc.divide(6, 2) == 3
    assert calc.divide(5, 2) == 2.5
    assert calc.divide(-6, 2) == -3

def test_divide_by_zero():
    """Test division by zero raises ValueError."""
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(5, 0) 