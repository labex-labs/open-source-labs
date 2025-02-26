# Attributzugriff

Es gibt eine alternative Möglichkeit, Attribute zuzugreifen, zu manipulieren und zu verwalten.

```python
getattr(obj, 'name')          # Entspricht obj.name
setattr(obj, 'name', value)   # Entspricht obj.name = value
delattr(obj, 'name')          # Entspricht del obj.name
hasattr(obj, 'name')          # Testet, ob das Attribut existiert
```

Beispiel:

```python
if hasattr(obj, 'x'):
    x = getattr(obj, 'x'):
else:
    x = None
```

*Hinweis: `getattr()` hat auch einen nützlichen Standardwert *arg\*.

```python
x = getattr(obj, 'x', None)
```
