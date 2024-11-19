

def romano_para_arabico(romano):
    romano_para_inteiro = {
        'I': 1, 'V': 5, 'X':10, 'L':50,
        'C':100, 'D':500, 'M':1000
    }
    return romano_para_inteiro.get(romano, 0)