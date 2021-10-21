import pytest
from src.calculator import Calculator

@pytest.fixture
def calculator() -> Calculator:
    return Calculator()

def test_multiplication(calculator):
    assert calculator.multiplication(2, 2) == 4
    