# Conjuntos (Sets)

Conjuntos são coleções de itens únicos não ordenados.

```python
tech_stocks = { 'IBM','AAPL','MSFT' }
# Sintaxe alternativa
tech_stocks = set(['IBM', 'AAPL', 'MSFT'])
```

Conjuntos são úteis para testes de pertinência (membership tests).

```python
>>> tech_stocks
set(['AAPL', 'IBM', 'MSFT'])
>>> 'IBM' in tech_stocks
True
>>> 'FB' in tech_stocks
False
>>>
```

Conjuntos também são úteis para eliminação de duplicatas.

```python
names = ['IBM', 'AAPL', 'GOOG', 'IBM', 'GOOG', 'YHOO']

unique = set(names)
# unique = set(['IBM', 'AAPL','GOOG','YHOO'])
```

Operações adicionais em conjuntos:

```python
unique.add('CAT')        # Adicionar um item
unique.remove('YHOO')    # Remover um item

s1 = { 'a', 'b', 'c'}
s2 = { 'c', 'd' }
s1 | s2                 # União de conjuntos (Set union) { 'a', 'b', 'c', 'd' }
s1 & s2                 # Intersecção de conjuntos (Set intersection) { 'c' }
s1 - s2                 # Diferença de conjuntos (Set difference) { 'a', 'b' }
```

Nestes exercícios, você começa a construir um dos principais programas usados para o restante deste curso. Faça seu trabalho no arquivo `report.py`.
