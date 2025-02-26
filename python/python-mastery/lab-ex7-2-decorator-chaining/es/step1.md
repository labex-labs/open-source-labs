# Copiando metadatos

Cuando una función se envuelve con un decorador, a menudo se pierde información sobre el nombre de la función, las cadenas de documentación y otros detalles. Verifíquelo:

```python
>>> @logged
    def add(x,y):
        'Adds two things'
        return x+y

>>> add
<function wrapper at 0x4439b0>
>>> help(add)
... mira la salida...
>>>
```

Corrige la definición del decorador `logged` para que copie adecuadamente los metadatos de la función. Para hacer esto, utiliza el decorador `@wraps(func)` como se muestra en las notas.

Una vez que hayas terminado, asegúrate de que el decorador conserve el nombre de la función y la cadena de documentación.

```python
>>> @logged
    def add(x,y):
        'Adds two things'
        return x+y

>>> add
<function add at 0x4439b0>
>>> add.__doc__
'Adds two things'
>>>
```

Corrige el decorador `@validated` que escribiste anteriormente para que también conserve los metadatos utilizando `@wraps(func)`.
