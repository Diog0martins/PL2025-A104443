# Análise de um dataset de obras musicais

O desenvolvimento deste programa basou-se numa expressão regular que fosse capaz de fazer *match* com qualquer linha do csv independentemente das suas unicidades. A expressão regular é a seguinte:

```
^([^;]*);\"?((?:[^\"]|\"\")*?)\"?;\d{1,4};(.+);([^;]*);\d{2}(:\d{2}){2};.*?(?:\n|$)
```

Fazendo uso desta expressão regular, foi possível capturar os seguintes campos de cada linha do ficheiro:
1. Nome do Compositor
2. Nome de cada Período
3. Nome de cada obra

Ao obter estes dados, cada um deles foi processado de modo a obter os seguintes resultados: 
1. Uma lista de todos os compositores ordenada alfabeticamente 
2. O número de obras de cada período
3. A lista do nome de obras, por cada período, ordenadas alfabeticamente

_**Nota:** Estes resultados são todos observáveis no stdout_
