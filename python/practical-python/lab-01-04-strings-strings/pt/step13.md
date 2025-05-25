# Exercício 1.14: Concatenação de strings

Embora os dados de string sejam somente leitura, você sempre pode reatribuir uma variável a uma string recém-criada.

Tente a seguinte instrução que concatena um novo símbolo "GOOG" ao final de `symbols`:

```python
>>> symbols = symbols + 'GOOG'
>>> symbols
'AAPL,IBM,MSFT,YHOO,SCOGOOG'
>>>
```

Ops! Não era isso que você queria. Corrija-o para que a variável `symbols` contenha o valor `'AAPL,IBM,MSFT,YHOO,SCO,GOOG'`.

```python
>>> symbols = ?
>>> symbols
'AAPL,IBM,MSFT,YHOO,SCO,GOOG'
>>>
```

Adicione `'HPQ'` ao início da string:

```python
>>> symbols = ?
>>> symbols
'HPQ,AAPL,IBM,MSFT,YHOO,SCO,GOOG'
>>>
```

Nestes exemplos, pode parecer que a string original está sendo modificada, em aparente violação de strings serem somente leitura. Não é o caso. Operações em strings criam uma string totalmente nova a cada vez. Quando o nome da variável `symbols` é reatribuído, ele aponta para a string recém-criada. Depois, a string antiga é destruída, pois não está mais sendo usada.
