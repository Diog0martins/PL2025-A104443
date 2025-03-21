from operacoes_anasin import rec_Parser

linha = input("Introduza uma operação: ")
ast = rec_Parser(linha)

if ast:
    print("Pretty print:")
    ast.pp()
    ast.calculate()
