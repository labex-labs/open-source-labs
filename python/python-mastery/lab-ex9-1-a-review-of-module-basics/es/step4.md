# from module import

Reinicie Python e importe un símbolo seleccionado de un módulo.

```python
>>> ############### [ RESTART ] ###############
>>> from simplemod import foo
Cargado simplemod
>>> foo()
x es 42
>>>
```

Observe cómo esto cargó todo el módulo (observe la salida de la función print y cómo se utiliza la variable `x`).

Cuando se utiliza `from`, el objeto del módulo en sí mismo no es visible. Por ejemplo:

```python
>>> simplemod.foo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name'simplemod' is not defined
>>>
```

Asegúrese de entender que cuando exporta cosas de un módulo, son simplemente referencias de nombre. Por ejemplo, pruebe esto y explique:

```python
>>> from simplemod import x,foo
>>> x
42
>>> foo()
x es 42
>>> x = 13
>>> foo()
x es 42                   #!! Por favor, explique
>>> x
13
>>>
```
