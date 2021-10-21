import pytest
from src.calculator import Calculator

@pytest.fixture
def calculator() -> Calculator:
    return Calculator()

def test_subtraction(calculator):
    assert calculator.subtraction(4, 2) == 2
    