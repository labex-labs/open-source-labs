# Exercice 1.19 : Extraction et réaffectation d'éléments de liste

Essayez quelques consultations :

```python
>>> symlist[0]
'HPQ'
>>> symlist[1]
'AAPL'
>>> symlist[-1]
'GOOG'
>>> symlist[-2]
'DOA'
>>>
```

Essayez de réaffecter une valeur :

```python
>>> symlist[2] = 'AIG'
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'DOA', 'GOOG']
>>>
```

Prenez quelques tranches :

```python
>>> symlist[0:3]
['HPQ', 'AAPL', 'AIG']
>>> symlist[-2:]
['DOA', 'GOOG']
>>>
```

Créez une liste vide et ajoutez un élément à celle-ci.

```python
>>> mysyms = []
>>> mysyms.append('GOOG')
>>> mysyms
['GOOG']
```

Vous pouvez réaffecter une partie d'une liste à une autre liste. Par exemple :

```python
>>> symlist[-2:] = mysyms
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG']
>>>
```

Lorsque vous faites cela, la liste du côté gauche (`symlist`) sera redimensionnée en conséquence pour adapter la liste du côté droit (`mysyms`). Par exemple, dans l'exemple ci-dessus, les deux derniers éléments de `symlist` ont été remplacés par l'unique élément de la liste `mysyms`.
