# Accès uniforme

Le dernier exemple montre comment mettre une interface plus uniforme sur un objet. Si vous ne le faites pas, un objet peut être difficile à utiliser :

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> a = s.cost() # Méthode
49010.0
>>> b = s.shares # Attribut de données
100
>>>
```

Pourquoi est-il nécessaire d'utiliser `()` pour `cost`, mais pas pour `shares`? Une propriété peut résoudre ce problème.
