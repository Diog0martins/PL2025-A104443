from operacoes_analex import lexer
from operacoes_ast import Operation, EmptyOperation

prox_simb = ('Erro', '', 0, 0)

def parserError(simb):
    print("Erro sintático, token inesperado: ", simb)

def rec_term(simb):
    global prox_simb
    if prox_simb and prox_simb.type == simb:
        token_value = prox_simb.value
        prox_simb = lexer.token()
        return token_value
    else:
        parserError(prox_simb)
        return None

def rec_ROp():
    global prox_simb
    if prox_simb is None or prox_simb.type != 'OP':
        print("Derivando por P2: ROp -->")
        print("Reconheci P2: ROp -->")
        return EmptyOperation()
    
    print("Derivando por P3: ROp --> Op Num ROp")
    op = rec_term('OP')
    num = rec_term('NUM')
    
    if num is None:
        return EmptyOperation()

    next_op = rec_ROp()
    print("Reconheci P3: ROp --> Op Num ROp")

    return Operation(op, num, next_op)

# P1: Operacao --> Num ROp
# P2: ROp -->
# P3:       | Op Num  ROp

def rec_Operacao():
    global prox_simb
    print("Derivando por P1: Operacao --> Num ROp")
    
    num = rec_term('NUM')
    if num is None:
        return EmptyOperation()

    rop = rec_ROp()
    print("Reconheci P1: Operacao --> Num ROp")

    return Operation("", num, rop)

def rec_Parser(data):
    global prox_simb
    lexer.input(data)
    prox_simb = lexer.token()
    return rec_Operacao()

