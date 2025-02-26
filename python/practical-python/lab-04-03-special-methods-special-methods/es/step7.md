# Acceso a atributos

Existe una forma alternativa de acceder, manipular y administrar atributos.

```python
getattr(obj, 'name')          # Lo mismo que obj.name
setattr(obj, 'name', value)   # Lo mismo que obj.name = value
delattr(obj, 'name')          # Lo mismo que del obj.name
hasattr(obj, 'name')          # Comprueba si el atributo existe
```

Ejemplo:

```python
if hasattr(obj, 'x'):
    x = getattr(obj, 'x'):
else:
    x = None
```

*Nota: `getattr()` también tiene un valor predeterminado útil *arg\*.

```python
x = getattr(obj, 'x', None)
```
