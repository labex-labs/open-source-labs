# Exercice 7.6 : Tri sur un champ avec lambda

Essayez de trier le portefeuille selon le nombre d'actions en utilisant une expression `lambda` :

```python
>>> portfolio.sort(key=lambda s: s.shares)
>>> for s in portfolio:
        print(s)

... inspectez le résultat...
>>>
```

Essayez de trier le portefeuille selon le prix de chaque action

```python
>>> portfolio.sort(key=lambda s: s.price)
>>> for s in portfolio:
        print(s)

... inspectez le résultat...
>>>
```

Note : `lambda` est un raccourci pratique car il vous permet de définir directement une fonction de traitement spéciale dans l'appel à `sort()` contrairement à devoir définir une fonction séparée en premier lieu.
