# Iteração: Protocolo (Iteration: Protocol)

Considere a instrução `for`.

```python
for x in obj:
    # statements
```

O que acontece por baixo dos panos?

```python
_iter = obj.__iter__()        # Get iterator object
while True:
    try:
        x = _iter.__next__()  # Get next item
        # statements ...
    except StopIteration:     # No more items
        break
```

Todos os objetos que funcionam com o `for-loop` implementam este protocolo de iteração de baixo nível.

Exemplo: Iteração manual sobre uma lista.

```python
>>> x = [1,2,3]
>>> it = x.__iter__()
>>> it
<listiterator object at 0x590b0>
>>> it.__next__()
1
>>> it.__next__()
2
>>> it.__next__()
3
>>> it.__next__()
Traceback (most recent call last):
File "<stdin>", line 1, in ? StopIteration
>>>
```
