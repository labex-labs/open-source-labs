# Croissance des dictionnaires/classes

Les dictionnaires Python (et les classes) permettent de stocker jusqu'à 5 valeurs avant que leur mémoire réservée ne soit doublée. Investiguez en créant un dictionnaire et en y ajoutant quelques autres valeurs :

```python
>>> row = { 'route': '22', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354 }
>>> sys.getsizeof(row)
>>> sys.getsizeof(row)
240
>>> row['a'] = 1
>>> sys.getsizeof(row)
240
>>> row['b'] = 2
>>> sys.getsizeof(row)
368
>>>
```

La mémoire diminue-t-elle si vous supprimez l'élément que vous venez d'ajouter?

Nourriture pour la réflexion : Si vous créez un grand nombre d'enregistrements, représenter chaque enregistrement sous forme de dictionnaire peut ne pas être la méthode la plus efficace - vous pourriez payer un lourd prix pour la commodité d'avoir un dictionnaire. Il pourrait être préférable de considérer l'utilisation de tuples, de tuples nommés ou de classes qui définissent `__slots__`.
