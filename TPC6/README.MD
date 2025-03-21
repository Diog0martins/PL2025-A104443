# Analisador e Avaliador de Expressões Aritméticas  

Este programa analisa expressões aritméticas simples, construindo e avaliando uma árvore sintática abstrata (AST).  

## Leitura e Processamento da Expressão  

O programa recebe uma operação introduzida pelo utilizador, processa-a e constrói a sua árvore sintática abstrata. No final, imprime a estrutura da expressão e o seu resultado.  

## Análise Sintática  

O parser verifica se a expressão segue as regras de derivação definidas, gerando uma árvore de operações. A gramática utilizada é:  

| Regra | Definição |
|-------|----------|
| P1 | Operacao → Num ROp |
| P2 | ROp → ε |
| P3 | ROp → Op Num ROp |

## Análise Léxica  

O analisador léxico identifica os seguintes tokens:  

| Token | Definição |
|-------|----------|
| NUM  | Número inteiro |
| OP   | Operador `+`, `-`, `*`, `/` |


## Construção e Avaliação da Expressão  

A árvore sintática abstrata (AST) é criada com base na expressão introduzida. A sua avaliação segue as regras de precedência, resolvendo-se primeiro multiplicações e divisões antes de somas e subtrações.
