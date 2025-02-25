# Comentario

A medida que empiezas a experimentar con el intérprete, a menudo quieres saber más sobre las operaciones admitidas por diferentes objetos. Por ejemplo, ¿cómo descubres qué operaciones están disponibles en una cadena?

Dependiendo de tu entorno de Python, es posible que puedas ver una lista de los métodos disponibles a través de la finalización con tabulación. Por ejemplo, prueba a escribir esto:

```python
>>> s = 'hello world'
>>> s.<tab key>
>>>
```

Si pulsar la tecla Tab no produce ningún efecto, puedes recurrir a la función integrada `dir()`. Por ejemplo:

```python
>>> s = 'hello'
>>> dir(s)
['__add__', '__class__', '__contains__',..., 'find', 'format',
'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace',
'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition',
'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit',
'rstrip','split','splitlines','startswith','strip','swapcase',
'title', 'translate', 'upper', 'zfill']
>>>
```

`dir()` produce una lista de todas las operaciones que pueden aparecer después del `(.)`. Utiliza el comando `help()` para obtener más información sobre una operación específica:

```python
>>> help(s.upper)
Ayuda sobre la función integrada upper:

upper(...)
    S.upper() -> string

    Devuelve una copia de la cadena S convertida a mayúsculas.
>>>
```
