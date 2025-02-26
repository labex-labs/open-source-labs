# Métodos vinculados

Un método que aún no ha sido invocado por el operador de llamada de función `()` se conoce como un _método vinculado_. Opera en la instancia en la que se originó.

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

Los métodos vinculados a menudo son una fuente de errores inadvertidos y no obvios. Por ejemplo:

```python
>>> s = stock.Stock('GOOG', 100, 490.10)
>>> print('Cost : %0.2f' % s.cost)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: float argument required
>>>
```

O un comportamiento engañoso que es difícil de depurar.

```python
f = open(filename, 'w')
...
f.close     # Ay, no hizo nada en absoluto. `f` todavía está abierto.
```

En ambos casos, el error se produce por olvidarse de incluir los paréntesis finales. Por ejemplo, `s.cost()` o `f.close()`.
