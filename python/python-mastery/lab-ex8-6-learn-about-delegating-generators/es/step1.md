# Ejemplo: Recibiendo mensajes

En el Ejercicio 8.3, revisamos las definiciones de corutinas. Las corutinas eran funciones a las que se les enviaba datos. Por ejemplo:

```python
>>> from cofollow import consumer
>>> @consumer
    def printer():
        while True:
            item = yield
            print('Got:', item)

>>> p = printer()
>>> p.send('Hello')
Got: Hello
>>> p.send('World')
Got: World
>>>
```

En aquel momento, podría haber sido interesante utilizar `yield` para recibir un valor. Sin embargo, si realmente miras el código, se ve bastante extraño: ¿un `yield` sin más? ¿Qué está pasando ahí?

En el archivo `cofollow.py`, define la siguiente función:

```python
def receive(expected_type):
    msg = yield
    assert isinstance(msg, expected_type), 'Expected type %s' % (expected_type)
    return msg
```

Esta función recibe un mensaje, pero luego verifica que sea del tipo esperado. Prueba:

```python
>>> from cofollow import consumer, receive
>>> @consumer
    def print_ints():
        while True:
             val = yield from receive(int)
             print('Got:', val)

>>> p = print_ints()
>>> p.send(42)
Got: 42
>>> p.send(13)
Got: 13
>>> p.send('13')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
...
AssertionError: Expected type <class 'int'>
>>>
```

Desde el punto de vista de la legibilidad, la declaración `yield from receive(int)` es un poco más descriptiva: indica que la función se detendrá en el `yield` hasta que reciba un mensaje de un tipo dado.

Ahora, modifica todas las corutinas en `coticker.py` para utilizar la nueva función `receive()` y asegúrate de que el código del Ejercicio 8.3 todavía funcione.
