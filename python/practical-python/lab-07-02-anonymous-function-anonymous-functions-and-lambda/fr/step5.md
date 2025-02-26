# Exercice 7.5 : Tri sur un champ

Essayez les instructions suivantes qui trient les données du portefeuille par ordre alphabétique du nom de l'action.

```python
>>> def stock_name(s):
       return s.name

>>> portfolio.sort(key=stock_name)
>>> for s in portfolio:
           print(s)

... inspectez le résultat...
>>>
```

Dans cette partie, la fonction `stock_name()` extrait le nom d'une action d'un seul élément de la liste `portfolio`. `sort()` utilise le résultat de cette fonction pour effectuer la comparaison.
