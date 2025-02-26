# Combinando todo

En el Ejercicio 6.1, creaste una clase `Structure` que definía un `__init__()`, `__setattr__()` y `__repr__()` generalizados. Esa clase requiría que un usuario definiera una variable de clase `_fields` de la siguiente manera:

```python
class Stock(Structure):
    _fields = ('name','shares','price')
```

El problema de esta clase es que la función `__init__()` no tenía una firma de argumentos útil para los fines de la ayuda y la pasaje de argumentos con palabras clave. En el Ejercicio 6.2, hiciste un truco astuto que implicaba una función especial `self._init()`. Por ejemplo:

```python
class Stock(Structure):
    _fields = ('name','shares', 'price')
    def __init__(self, name, shares, price):
        self._init()
  ...
```

Esto dio una firma útil, pero ahora la clase es un poco extraña porque el usuario tiene que proporcionar tanto la variable `_fields` como el método `__init__()`.

Tu tarea es eliminar la variable `_fields` utilizando algunas técnicas de inspección de funciones. Primero, observa que puedes obtener la firma de argumentos de `Stock` de la siguiente manera:

```python
>>> import inspect
>>> sig = inspect.signature(Stock)
>>> tuple(sig.parameters)
('name','shares', 'price')
>>>
```

Quizás podrías establecer la variable `_fields` a partir de la firma de argumentos de `__init__()`. Agrega un método de clase `set_fields(cls)` a `Structure` que inspeccione la función `__init__()` y establezca la variable `_fields` adecuadamente. Debes usar tu nueva función de la siguiente manera:

```python
class Stock(Structure):
    def __init__(self, name, shares, price):
        self._init()

  ...

Stock.set_fields()
```

La clase resultante debería funcionar de la misma manera que antes:

```python
>>> s = Stock(name='GOOG', shares=100, price=490.1)
>>> s
Stock('GOOG',100,490.1)
>>> s.shares = 50
>>> s.share = 50
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "structure.py", line 12, in __setattr__
    raise AttributeError('No attribute %s' % name)
AttributeError: No attribute share
>>>
```

Vuelve a verificar la clase `Stock` ligeramente modificada con tus pruebas unitarias. Todavía habrá fallos, pero nada debería cambiar con respecto al ejercicio anterior.

En este momento, todo sigue siendo un poco "truquero", pero estás avanzando. Tienes una clase de estructura de `Stock` con una función `__init__()` útil, hay una cadena de representación útil y el método `__setattr__()` restringe el conjunto de nombres de atributos. El paso extra de tener que invocar `set_fields()` es un poco extraño, pero volveremos a eso.
