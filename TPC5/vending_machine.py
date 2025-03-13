import re
import ply.lex as lex
import json

using_machine = True
balance = 0.0

##Tokens ->

tokens = (
    'LISTAR',
    'SELECIONAR',
    'MOEDA',
    'SAIR',
    'DINHEIRO',
    'CODIGO'
)

##Estados ->
states = (
    ('selectstate', 'exclusive'),
    ('moedastate', 'exclusive'),
)

t_ignore = ' \t\n,'

t_selectstate_ignore = ' \t\n,'
t_moedastate_ignore = ' \t\n,'

def t_LISTAR(t):
    r'LISTAR'
    list_products()
    return t

def t_SELECIONAR(t):
    r'SELECIONAR'
    t.lexer.begin('selectstate')
    return t

def t_MOEDA(t):
    r'MOEDA'
    t.lexer.begin('moedastate')
    return t

def t_SAIR(t):
    r'SAIR'
    global using_machine
    print("Exiting machine...")
    using_machine = False
    return t

def t_selectstate_CODIGO(t):
    r'[A-Z](\d){1,2}'
    process_selection(t.value)
    t.lexer.begin('INITIAL')
    return t

def t_moedastate_DINHEIRO(t):
    r'((1c|2c|5c|10c|20c|50c|1e|2e),?)+'
    add_money(t.value)
    t.lexer.begin('INITIAL')
    return t

# Error handlers
def t_error(t):
    print("Caracter desconhecido: '%s'" % t.value[0])
    t.lexer.skip(1)

def t_selectstate_error(t):
    print("Caracter desconhecido no estado SELECT_STATE: '%s'" % t.value[0])
    t.lexer.skip(1)

def t_moedastate_error(t):
    print("Caracter desconhecido no estado MOEDA_STATE: '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()


##Gerir a máquina 
def get_machine(path):
    with open(path, 'r') as file:
        return json.load(file)


def update_machine(path, data):
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)


def list_products():
    print("+--------+----------------------+--------+------------+")
    print("| Código | Nome                 | Preço  | Quantidade |")
    print("+--------+----------------------+--------+------------+")
    for item in machine_data:
        print(f"| {item['cod']:<6} | {item['nome']:<20} | €{item['preco']:<5} | {item['quant']:<10} |")
    print("+--------+----------------------+--------+------------+")


def add_money(value):
    global balance
    coins = {'1c': 0.01, '2c': 0.02, '5c': 0.05, '10c': 0.10, '20c': 0.20, '50c': 0.50, '1e': 1.00, '2e': 2.00}
    for coin in value.split(','):
        if coin in coins:
            balance += coins[coin]
    print(f"Saldo atual: €{balance:.2f}")


def process_selection(code):
    global balance
    for item in machine_data:
        if item['cod'] == code:
            if item['quant'] > 0 and balance >= item['preco']:
                item['quant'] -= 1
                balance -= item['preco']
                print(f"Produto {item['nome']} comprado! Saldo restante: €{balance:.2f}")
                return
            elif balance < item['preco']:
                print("Saldo insuficiente!")
                return
            else:
                print("Produto esgotado!")
                return
    print("Código inválido!")


def main():
    global using_machine, machine_data
    the_machine = "vending_machine.json"
    machine_data = get_machine(the_machine)
    
    while(using_machine):
        input_data = input(">> ")
        lexer.input(input_data)
        
        for tok in lexer:
            print(f"Token: {tok.type} -> {tok.value}")
    
    update_machine(the_machine, machine_data)

if __name__ == '__main__':
    main()