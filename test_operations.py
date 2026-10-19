from operations import somar, subtrair

def test_somar():
    assert somar(10, 5) == 15
    assert somar(-1, 1) == 0

def test_subtrair():
    assert subtrair(10, 5) == 5
    assert subtrair(0, 5) == -5
