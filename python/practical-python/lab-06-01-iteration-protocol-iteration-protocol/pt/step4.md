# Exercício 6.1: Iteração Ilustrada (Iteration Illustrated)

Crie a seguinte lista:

```python
a = [1,9,4,25,16]
```

Itere manualmente sobre esta lista. Chame `__iter__()` para obter um iterador e chame o método `__next__()` para obter elementos sucessivos.

```python
>>> i = a.__iter__()
>>> i
<listiterator object at 0x64c10>
>>> i.__next__()
1
>>> i.__next__()
9
>>> i.__next__()
4
>>> i.__next__()
25
>>> i.__next__()
16
>>> i.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
```

A função embutida `next()` é um atalho para chamar o método `__next__()` de um iterador. Tente usá-la em um arquivo:

```python
>>> f = open('portfolio.csv')
>>> f.__iter__()    # Note: This returns the file itself
<_io.TextIOWrapper name='portfolio.csv' mode='r' encoding='UTF-8'>
>>> next(f)
'name,shares,price\n'
>>> next(f)
'"AA",100,32.20\n'
>>> next(f)
'"IBM",50,91.10\n'
>>>
```

Continue chamando `next(f)` até chegar ao final do arquivo. Observe o que acontece.
