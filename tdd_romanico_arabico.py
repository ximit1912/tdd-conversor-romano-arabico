import pytest
from romanico_arabico import romanico_para_arabico

def teste_simbolos():
    assert romanico_para_arabico('I') == 1
    assert romanico_para_arabico('V') == 5
    assert romanico_para_arabico('X') == 10
    assert romanico_para_arabico('L') == 50
    assert romanico_para_arabico('C') == 100
    assert romanico_para_arabico('D') == 500
    assert romanico_para_arabico('M') == 1000
    