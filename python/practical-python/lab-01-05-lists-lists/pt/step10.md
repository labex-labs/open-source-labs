# Exercício 1.22: Adicionando (Appending), inserindo (inserting) e excluindo itens

Use o método `append()` para adicionar o símbolo `'RHT'` ao final de `symlist`.

```python
>>> symlist.append('RHT') # append 'RHT'
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']
>>>
```

Use o método `insert()` para inserir o símbolo `'AA'` como o segundo item na lista.

```python
>>> symlist.insert(1, 'AA') # Insert 'AA' as the second item in the list
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']
>>>
```

Use o método `remove()` para remover `'MSFT'` da lista.

```python
>>> symlist.remove('MSFT') # Remove 'MSFT'
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT']
>>>
```

Adicione (Append) uma entrada duplicada para `'YHOO'` ao final da lista.

_Nota: é perfeitamente aceitável que uma lista tenha valores duplicados._

```python
>>> symlist.append('YHOO') # Append 'YHOO'
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT', 'YHOO']
>>>
```

Use o método `index()` para encontrar a primeira posição de `'YHOO'` na lista.

```python
>>> symlist.index('YHOO') # Find the first index of 'YHOO'
4
>>> symlist[4]
'YHOO'
>>>
```

Conte quantas vezes `'YHOO'` está na lista:

```python
>>> symlist.count('YHOO')
2
>>>
```

Remova a primeira ocorrência de `'YHOO'`.

```python
>>> symlist.remove('YHOO') # Remove first occurrence 'YHOO'
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'GOOG', 'RHT', 'YHOO']
>>>
```

Só para você saber, não existe um método para encontrar ou remover todas as ocorrências de um item. No entanto, veremos uma maneira elegante de fazer isso na seção 2.
