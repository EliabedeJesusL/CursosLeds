from app import multiplicar, dividir
import pytest

def test_multiplicar():
    assert multiplicar(3, 4) == 12
    assert multiplicar(-1, 5) == -5

def test_dividir():
    assert dividir(10, 2) == 5
    with pytest.raises(ValueError):
        dividir(10, 0)
