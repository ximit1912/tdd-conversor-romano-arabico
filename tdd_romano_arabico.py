import pytest
from romano_arabico import romano_para_arabico

def teste_simbolos():
    assert romano_para_arabico('I') == 1
    assert romano_para_arabico('V') == 5
    assert romano_para_arabico('X') == 10
    assert romano_para_arabico('L') == 50
    assert romano_para_arabico('C') == 100
    assert romano_para_arabico('D') == 500
    assert romano_para_arabico('M') == 1000
    
def teste_combinacoes_simbolos():
    assert romano_para_arabico('II') == 2
    assert romano_para_arabico('VI') == 6
    assert romano_para_arabico('XV') == 15