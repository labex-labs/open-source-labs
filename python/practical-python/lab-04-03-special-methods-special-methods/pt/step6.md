# Métodos Vinculados (Bound Methods)

Um método que ainda não foi invocado pelo operador de chamada de função `()` é conhecido como um _método vinculado_ (bound method). Ele opera na instância onde se originou.

```python
>>> s = stock.Stock('GOOG', 100, 490.10)
>>> s
<Stock object at 0x590d0>
>>> c = s.cost
>>> c
<bound method Stock.cost of <Stock object at 0x590d0>>
>>> c()
49010.0
>>>
```

Métodos vinculados são frequentemente uma fonte de erros descuidados e não óbvios. Por exemplo:

```python
>>> s = stock.Stock('GOOG', 100, 490.10)
>>> print('Cost : %0.2f' % s.cost)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: float argument required
>>>
```

Ou um comportamento traiçoeiro que é difícil de depurar.

```python
f = open(filename, 'w')
...
f.close     # Oops, Didn't do anything at all. `f` still open.
```

Em ambos os casos, o erro é causado por esquecer de incluir os parênteses finais. Por exemplo, `s.cost()` ou `f.close()`.
