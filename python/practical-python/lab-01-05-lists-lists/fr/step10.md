# Exercice 1.22 : Ajout, insertion et suppression d'éléments

Utilisez la méthode `append()` pour ajouter le symbole `'RHT'` à la fin de `symlist`.

```python
>>> symlist.append('RHT') # ajoute 'RHT'
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']
>>>
```

Utilisez la méthode `insert()` pour insérer le symbole `'AA'` comme deuxième élément de la liste.

```python
>>> symlist.insert(1, 'AA') # Insère 'AA' comme deuxième élément de la liste
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']
>>>
```

Utilisez la méthode `remove()` pour supprimer `'MSFT'` de la liste.

```python
>>> symlist.remove('MSFT') # Supprime 'MSFT'
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT']
>>>
```

Ajoutez une entrée dupliquée pour `'YHOO'` à la fin de la liste.

_Nota : Il est tout à fait normal qu'une liste contienne des valeurs dupliquées._

```python
>>> symlist.append('YHOO') # Ajoute 'YHOO'
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT', 'YHOO']
>>>
```

Utilisez la méthode `index()` pour trouver la première position de `'YHOO'` dans la liste.

```python
>>> symlist.index('YHOO') # Trouve le premier indice de 'YHOO'
4
>>> symlist[4]
'YHOO'
>>>
```

Comptez combien de fois `'YHOO'` est dans la liste :

```python
>>> symlist.count('YHOO')
2
>>>
```

Supprimez la première occurrence de `'YHOO'`.

```python
>>> symlist.remove('YHOO') # Supprime la première occurrence de 'YHOO'
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'GOOG', 'RHT', 'YHOO']
>>>
```

Pour que vous le sachiez, il n'y a pas de méthode pour trouver ou supprimer toutes les occurrences d'un élément. Cependant, nous verrons une manière élégante de le faire dans la section 2.
