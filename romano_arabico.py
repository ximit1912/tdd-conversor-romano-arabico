

def romano_para_arabico(romano):
    romano_para_inteiro = {
        'I': 1, 'V': 5, 'X':10, 'L':50,
        'C':100, 'D':500, 'M':1000
    }

    total = 0
    valor_anterior = 0

    for char in romano:
        valor_atual = romano_para_inteiro.get(char, 0)
        if valor_atual > valor_anterior:
            #subtrai o valor anterior (pois foi somado antes) e adiciona a diferença
            total += valor_atual - 2 * valor_anterior
        else:
            total += valor_atual
        valor_anterior = valor_atual
    
    return total
    