# Passer des tuples et des dictionnaires

Les tuples peuvent être décomposés en arguments variables.

```python
numbers = (2,3,4)
f(1, *numbers)      # Identique à f(1,2,3,4)
```

Les dictionnaires peuvent également être décomposés en arguments de mot clé.

```python
options = {
    'couleur' : 'rouge',
    'délimiteur' : ',',
    'largeur' : 400
}
f(data, **options)
# Identique à f(data, couleur='rouge', délimiteur=',', largeur=400)
```
