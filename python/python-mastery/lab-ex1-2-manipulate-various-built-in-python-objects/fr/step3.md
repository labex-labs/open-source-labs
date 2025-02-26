# Partie 3 : Manipulation de listes

Dans la première partie, vous avez travaillé avec des chaînes de caractères contenant des symboles boursiers. Par exemple :

```python
>>> symbols = 'HPQ AAPL IBM MSFT YHOO  GOOG'
>>>
```

Définissez la variable ci-dessus et divisez-la en une liste de noms en utilisant l'opération `split()` des chaînes de caractères :

```python
>>> symlist = symbols.split()
>>> symlist
['HPQ', 'AAPL', 'IBM', 'MSFT', 'YHOO', 'GOOG' ]
>>>
```

## Extraction et réaffectation d'éléments de liste

Les listes fonctionnent comme des tableaux où vous pouvez rechercher et modifier des éléments par indice numérique. Essayez quelques recherches :

```python
>>> symlist[0]
'HPQ'
>>> symlist[1]
'AAPL'
>>> symlist[-1]
'GOOG'
>>> symlist[-2]
'YHOO'
>>>
```

Essayez de réaffecter l'un des éléments :

```python
>>> symlist[2] = 'AIG'
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG' ]
>>>
```

## Boucle sur les éléments de liste

La boucle `for` fonctionne en parcourant les données dans une séquence telle qu'une liste. Vérifiez-en en tapant la boucle suivante et en observant ce qui se passe :

```python
>>> for s in symlist:
        print('s =', s)

... regardez la sortie...
```

## Tests d'appartenance

Utilisez l'opérateur `in` pour vérifier si `'AIG'`, `'AA'` et `'CAT'` sont dans la liste de symboles.

```python
>>> 'AIG' in symlist
True
>>> 'AA' in symlist
False
>>>
```

## Ajout, insertion et suppression d'éléments

Utilisez la méthode `append()` pour ajouter le symbole `'RHT'` à la fin de `symlist`.

```python
>>> symlist.append('RHT')
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']
>>>
```

Utilisez la méthode `insert()` pour insérer le symbole `'AA'` comme deuxième élément de la liste.

```python
>>> symlist.insert(1,'AA')
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']
>>>
```

Utilisez la méthode `remove()` pour supprimer `'MSFT'` de la liste.

```python
>>> symlist.remove('MSFT')
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT']
```

Essayez d'appeler `remove()` à nouveau pour voir ce qui se passe si l'élément n'est pas trouvé.

```python
>>> symlist.remove('MSFT')
... observez ce qui se passe...
>>>
```

Utilisez la méthode `index()` pour trouver la position de `'YHOO'` dans la liste.

```python
>>> symlist.index('YHOO')
4
>>> symlist[4]
'YHOO'
>>>
```

## Tri de listes

Voulez trier une liste? Utilisez la méthode `sort()`. Essayez :

```python
>>> symlist.sort()
>>> symlist
['AA', 'AAPL', 'AIG', 'GOOG', 'HPQ', 'RHT', 'YHOO']
>>>
```

Voulez trier dans l'ordre inverse? Essayez ceci :

```python
>>> symlist.sort(reverse=True)
>>> symlist
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
>>>
```

Remarque : Trier une liste modifie son contenu "in-place". C'est-à-dire que les éléments de la liste sont mélangés, mais aucun nouvelle liste n'est créée à la suite.

## Listes de tout

Les listes peuvent contenir n'importe quel type d'objet, y compris d'autres listes (par exemple, des listes imbriquées). Essayez :

```python
>>> nums = [101,102,103]
>>> items = [symlist, nums]
>>> items
[['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA'], [101, 102, 103]]
```

Prenez soin d'observer la sortie ci-dessus. `items` est une liste avec deux éléments. Chaque élément est une liste.

Essayez quelques recherches dans des listes imbriquées :

```python
>>> items[0]
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
>>> items[0][1]
'RHT'
>>> items[0][1][2]
'T'
>>> items[1]
[101, 102, 103]
>>> items[1][1]
102
>>>
```
