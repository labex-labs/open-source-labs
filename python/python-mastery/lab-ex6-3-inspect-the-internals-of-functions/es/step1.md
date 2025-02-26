# Inspeccionando funciones

Define una función simple:

```python
>>> def add(x,y):
       'Adds two things'
       return x+y

>>>
```

Haz un `dir()` en la función para ver sus atributos.

```python
>>> dir(add)
... mira el resultado...
>>>
```

Obtén información básica como el nombre de la función, el nombre del módulo que la define y la cadena de documentación.

```python
>>> add.__name__
'add'
>>> add.__module__
'__main__'
>>> add.__doc__
'Adds two things'
>>>
```

El atributo `__code__` de una función tiene información de bajo nivel sobre la implementación de la función. Intenta ver esto y determinar el número de argumentos requeridos y los nombres de las variables locales.
