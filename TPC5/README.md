# Máquina de Venda Automática  

Este programa simula uma máquina de venda automática, permitindo ao utilizador listar produtos, inserir dinheiro e selecionar um item para compra.  

Os comandos disponíveis são:  

| Comando      | Descrição |
|-------------|-----------|
| **LISTAR** | Mostra a lista de produtos disponíveis, juntamente com os seus preços e quantidades. |
| **MOEDA**  | Permite inserir dinheiro na máquina. As moedas aceites são: `1c`, `2c`, `5c`, `10c`, `20c`, `50c`, `1e`, `2e`. |
| **SELECIONAR** | Inicia o processo de seleção de um produto. O utilizador deve introduzir o código do produto desejado. |
| **SAIR** | Encerra a máquina de venda automática. |

## Estrutura dos produtos  
Os produtos são armazenados num ficheiro JSON no seguinte formato:  

```json
[
    {"cod": "A23", "nome": "água 0.5L", "preco": 0.7, "quant": 8},
    {"cod": "A45", "nome": "Coca Cola 0.7L", "preco": 1.2, "quant": 5},
    {"cod": "C67", "nome": "Sumo 300ml", "preco": 1.2, "quant": 10}
]
```

Cada produto tem um **código**, um **nome**, um **preço** e uma **quantidade disponível**.  

## Funcionamento  

### 1. Listar produtos  
O utilizador pode ver os produtos disponíveis usando o comando `LISTAR`.  
O output gerado segue um formato tabular:  

```
+--------+----------------------+--------+------------+
| Código | Nome                 | Preço  | Quantidade |
+--------+----------------------+--------+------------+
| A23    | Água 0.5L            | €0.7   | 8          |
| A45    | Coca Cola 0.5L       | €1.2   | 5          |
| B67    | Sumo 300ml           | €1.2   | 10         |
+--------+----------------------+--------+------------+
```

### 2. Inserir moedas  
O utilizador pode adicionar dinheiro com o comando `MOEDA`, seguido dos valores das moedas:  

```
>> MOEDA 50c,1e,20c
Saldo atual: €1.70
```

### 3. Comprar um produto  
Para comprar um produto, o utilizador deve inserir `SELECIONAR` e depois o código do produto desejado:  

```
>> SELECIONAR
>> C67
Produto Sumo 300ml comprado! Saldo restante: €0.50
```

- Se o saldo for insuficiente, a máquina avisará o utilizador.  
- Se o produto estiver esgotado, será indicado que não há stock.  
- Se o código do produto for inválido, será apresentado um erro.  

### 4. Sair da máquina  
Para encerrar a máquina, basta introduzir `SAIR`:  

```
>> SAIR
Exiting machine...
```

## Implementação  

O programa faz uso da biblioteca `PLY (Python Lex-Yacc)` para a análise léxica. Os tokens principais são:  

- **LISTAR** → Lista os produtos.  
- **MOEDA** → Entra no estado de inserção de moedas.  
- **SELECIONAR** → Entra no estado de seleção de produtos.  
- **SAIR** → Termina o programa.  
- **CODIGO** → Representa o código de um produto (exemplo: `A23`).  
- **DINHEIRO** → Representa moedas inseridas na máquina.  

O lexer utiliza expressões regulares para reconhecer cada comando e processar a interação do utilizador.

### Estados do Meta Autómato  

O programa implementa um **automato** com diferentes estados que controlam a interação do utilizador:  

- **INITIAL**: Estado padrão onde o utilizador pode introduzir qualquer comando principal.  
- **selectstate**: Estado ativado após `SELECIONAR`, onde o utilizador deve introduzir um código de produto válido.  
- **moedastate**: Estado ativado após `MOEDA`, permitindo a inserção de moedas no saldo da máquina.  

Cada estado define regras específicas para interpretar corretamente os inputs do utilizador e garante que a sequência de ações segue a lógica esperada. Se um comando inválido for introduzido num estado específico, o programa apresenta uma mensagem de erro.  


## Nota  
O estado e a quantidade de produtos são atualizados no ficheiro JSON sempre que ocorre uma compra. 
