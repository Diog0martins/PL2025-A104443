# Analisador Léxico

Este programa é um analisador léxico para uma liguagem de query com a qual se podem escrever frases do
género:

```
# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000
```

O texto desta linguagem de query é analisado e transformado em tokens. Para a análise léxica, é utilizada a biblioteca PLY (Python Lex-Yacc).

Os tokens são divididos nas seguintes categorias:

|Token |Exemplos|
|------|-------|
|**Variávies** | ?nome, ?desc, ?s, ?w|
|**Prefixos**|dbo, foaf|
|**Tipos**| MusicalArtist, name, artist, abstract|
|**Abreviação de tipo**| a|
|**Língua**| en|
|**Número**| 1000|
|**Ponto**| .|
|**Dois pontos**| :|
|**Arroba**| @|
|**WHERE**| where|
|**SELECT**| select|
|**LIMIT**| LIMIT|
|**Chaveta esquerda**| {|
|**Chaveta direita**| }|
|**String**| Chuck Berry |
|**Ignorar**| ' ', '\n', '\t' e comentários(texto que precede um #)|
  
<br>
O lexer é construído tendo em conta cada um desses tokens, tal como as expressões regulares que os definem.

<br>


_**Nota:** O resultado do tokenizer é observável no stdout_
