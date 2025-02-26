# Les Trois Opérations

L'ensemble du système d'objets Python ne comporte que trois opérations principales : la lecture, l'écriture et la suppression d'attributs. Normalement, on y accède via le point (.) comme ceci :

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.name    # lecture
'GOOG'
>>> s.shares = 50    # écriture
>>> del s.shares     # suppression
>>>
```

Les trois opérations sont également disponibles sous forme de fonctions. Par exemple :

```python
>>> getattr(s, 'name')            # Identique à s.name
'GOOG'
>>> setattr(s,'shares', 50)      # Identique à s.shares = 50
>>> delattr(s,'shares')          # Identique à del s.shares
>>>
```

Une fonction supplémentaire, `hasattr()`, peut être utilisée pour vérifier si un attribut existe dans un objet :

```python
>>> hasattr(s, 'name')
True
>>> hasattr(s, 'blah')
False
>>>
```
