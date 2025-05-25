# Exercício 1.19: Extraindo e reatribuindo elementos de lista

Experimente algumas pesquisas:

```python
>>> symlist[0]
'HPQ'
>>> symlist[1]
'AAPL'
>>> symlist[-1]
'GOOG'
>>> symlist[-2]
'DOA'
>>>
```

Tente reatribuir um valor:

```python
>>> symlist[2] = 'AIG'
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'DOA', 'GOOG']
>>>
```

Pegue algumas fatias (slices):

```python
>>> symlist[0:3]
['HPQ', 'AAPL', 'AIG']
>>> symlist[-2:]
['DOA', 'GOOG']
>>>
```

Crie uma lista vazia e adicione um item a ela.

```python
>>> mysyms = []
>>> mysyms.append('GOOG')
>>> mysyms
['GOOG']
```

Você pode reatribuir uma porção de uma lista a outra lista. Por exemplo:

```python
>>> symlist[-2:] = mysyms
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG']
>>>
```

Quando você faz isso, a lista no lado esquerdo (`symlist`) será redimensionada conforme apropriado para fazer o lado direito (`mysyms`) caber. Por exemplo, no exemplo acima, os dois últimos itens de `symlist` foram substituídos pelo único item na lista `mysyms`.
