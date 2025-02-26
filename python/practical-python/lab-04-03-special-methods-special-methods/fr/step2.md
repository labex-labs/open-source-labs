# Méthodes spéciales pour les conversions de chaînes de caractères

Les objets ont deux représentations sous forme de chaîne de caractères.

```python
>>> from datetime import date
>>> d = date(2012, 12, 21)
>>> print(d)
2012-12-21
>>> d
datetime.date(2012, 12, 21)
>>>
```

La fonction `str()` est utilisée pour créer une sortie imprimable agréable:

```python
>>> str(d)
'2012-12-21'
>>>
```

La fonction `repr()` est utilisée pour créer une représentation plus détaillée pour les programmeurs.

```python
>>> repr(d)
'datetime.date(2012, 12, 21)'
>>>
```

Ces fonctions, `str()` et `repr()`, utilisent une paire de méthodes spéciales dans la classe pour produire la chaîne de caractères à afficher.

```python
class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Utilisée avec `str()`
    def __str__(self):
        return f'{self.year}-{self.month}-{self.day}'

    # Utilisée avec `repr()`
    def __repr__(self):
        return f'Date({self.year},{self.month},{self.day})'
```

_Nota: La convention pour `__repr__()` est de retourner une chaîne de caractères qui, lorsqu'elle est passée à `eval()`, recréera l'objet sous-jacent. Si cela n'est pas possible, une représentation facilement lisible est utilisée à la place._
