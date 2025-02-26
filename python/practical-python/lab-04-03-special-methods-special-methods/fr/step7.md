# Accès aux attributs

Il existe une manière alternative d'accéder, de manipuler et de gérer les attributs.

```python
getattr(obj, 'name')          # Identique à obj.name
setattr(obj, 'name', value)   # Identique à obj.name = value
delattr(obj, 'name')          # Identique à del obj.name
hasattr(obj, 'name')          # Vérifie si l'attribut existe
```

Exemple :

```python
if hasattr(obj, 'x'):
    x = getattr(obj, 'x'):
else:
    x = None
```

*Remarque : `getattr()` a également une valeur par défaut utile pour l'*argument\*.

```python
x = getattr(obj, 'x', None)
```
