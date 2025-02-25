# Exercice 1.25 : Listes de tout

Les listes peuvent contenir n'importe quel type d'objet, y compris d'autres listes (par exemple, des listes imbriquées). Essayez :

```python
>>> nums = [101, 102, 103]
>>> items = ['spam', symlist, nums]
>>> items
['spam', ['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA'], [101, 102, 103]]
```

Prenez soin de bien examiner la sortie ci-dessus. `items` est une liste avec trois éléments. Le premier élément est une chaîne de caractères, mais les deux autres éléments sont des listes.

Vous pouvez accéder aux éléments des listes imbriquées en utilisant plusieurs opérations d'indexation.

```python
>>> items[0]
'spam'
>>> items[0][0]
's'
>>> items[1]
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
>>> items[1][1]
'RHT'
>>> items[1][1][2]
'T'
>>> items[2]
[101, 102, 103]
>>> items[2][1]
102
>>>
```

Même si techniquement il est possible de créer des structures de liste très complexes, en règle générale, il est préférable de garder les choses simples. Habituellement, les listes contiennent des éléments de la même sorte de valeur. Par exemple, une liste composée entièrement de nombres ou une liste de chaînes de caractères. Mélanger différents types de données dans la même liste est souvent un bon moyen de vous faire exploser la tête, il est donc préférable de l'éviter.
