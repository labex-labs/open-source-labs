# Conversiones

Tu nuevo tipo primitivo está casi completo. Es posible que desees darle la capacidad de trabajar con algunas conversiones comunes. Por ejemplo:

```python
>>> a = MutInt(3)
>>> int(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: int() argument must be a string, a bytes-like object or a number, not 'MutInt'
>>> float(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: float() argument must be a string, a bytes-like object or a number, not 'MutInt'
>>>
```

Puedes dar a tu clase un método `__int__()` y `__float__()` para corregir esto:

```python
from functools import total_ordering

@total_ordering
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

 ...

    def __int__(self):
        return self.value

    def __float__(self):
        return float(self.value)
```

Ahora, puedes convertir adecuadamente:

```python
>>> a = MutInt(3)
>>> int(a)
3
>>> float(a)
3.0
>>>
```

Como regla general, Python nunca convierte automáticamente los datos. Por lo tanto, aunque le diste a la clase un método `__int__()`, `MutInt` todavía no funcionará en todas las situaciones en las que se espera un entero. Por ejemplo, la indexación:

```python
>>> names = ['Dave', 'Guido', 'Paula', 'Thomas', 'Lewis']
>>> a = MutInt(1)
>>> names[a]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers or slices, not MutInt
>>>
```

Esto se puede corregir dando a `MutInt` un método `__index__()` que produce un entero. Modifica la clase de la siguiente manera:

```python
from functools import total_ordering

@total_ordering
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

 ...

    def __int__(self):
        return self.value

    __index__ = __int__     # Hacer que la indexación funcione
```

**Discusión**

Crear un nuevo tipo de dato primitivo es en realidad una de las tareas de programación más complicadas en Python. Hay muchos casos límite y problemas de bajo nivel por los que preocuparse, especialmente en cuanto a cómo tu tipo interactúa con otros tipos de Python. Probablemente lo más importante a tener en cuenta es que puedes personalizar casi todos los aspectos de cómo un objeto interactúa con el resto de Python si conoces los protocolos subyacentes. Si vas a hacer esto, es recomendable revisar el código existente en busca de algo similar a lo que estás intentando crear.
