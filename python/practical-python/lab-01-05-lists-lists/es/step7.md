# Ejercicio 1.19: Extracción y reasignación de elementos de una lista

Intenta algunas búsquedas:

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

Intenta reasignar un valor:

```python
>>> symlist[2] = 'AIG'
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'DOA', 'GOOG']
>>>
```

Toma algunos segmentos:

```python
>>> symlist[0:3]
['HPQ', 'AAPL', 'AIG']
>>> symlist[-2:]
['DOA', 'GOOG']
>>>
```

Crea una lista vacía y agrega un elemento a ella.

```python
>>> mysyms = []
>>> mysyms.append('GOOG')
>>> mysyms
['GOOG']
```

Puedes reasignar una parte de una lista a otra lista. Por ejemplo:

```python
>>> symlist[-2:] = mysyms
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG']
>>>
```

Cuando haces esto, la lista del lado izquierdo (`symlist`) se redimensionará adecuadamente para que quepa el lado derecho (`mysyms`). Por ejemplo, en el ejemplo anterior, los últimos dos elementos de `symlist` se reemplazaron por el único elemento de la lista `mysyms`.
