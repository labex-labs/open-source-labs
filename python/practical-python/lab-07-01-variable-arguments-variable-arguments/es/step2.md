# Argumentos variables de palabras clave (\*\*kwargs)

Una función también puede aceptar cualquier número de argumentos de palabras clave. Por ejemplo:

```python
def f(x, y, **kwargs):
 ...
```

Llamada a la función.

```python
f(2, 3, flag=True, mode='fast', header='debug')
```

Las palabras clave adicionales se pasan en un diccionario.

```python
def f(x, y, **kwargs):
    # x -> 2
    # y -> 3
    # kwargs -> { 'flag': True,'mode': 'fast', 'header': 'debug' }
```
