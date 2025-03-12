# Travailler avec les listes en Python

Les listes sont un type de structure de données en Python. Une structure de données est une façon d'organiser et de stocker des données de manière à ce qu'elles puissent être utilisées efficacement. Les listes sont très polyvalentes car elles peuvent stocker différents types d'éléments, comme des nombres, des chaînes de caractères ou même d'autres listes. Dans cette étape, nous allons apprendre à effectuer diverses opérations sur les listes.

## Création de listes à partir de chaînes de caractères

Pour commencer à travailler avec les listes en Python, nous devons d'abord ouvrir une session interactive Python. C'est comme un environnement spécial où nous pouvons écrire et exécuter du code Python immédiatement. Pour démarrer cette session, tapez la commande suivante dans votre terminal :

```bash
python3
```

Une fois que vous êtes dans la session interactive Python, nous allons créer une liste à partir d'une chaîne de caractères. Une chaîne de caractères n'est qu'une séquence de caractères. Nous allons définir une chaîne de caractères qui contient quelques symboles de titres boursiers séparés par des espaces. Ensuite, nous allons convertir cette chaîne de caractères en une liste. Chaque symbole de titre boursier deviendra un élément de la liste.

```python
>>> symbols = 'HPQ AAPL IBM MSFT YHOO GOOG'
>>> symlist = symbols.split()    # Diviser la chaîne de caractères aux espaces
>>> symlist
['HPQ', 'AAPL', 'IBM', 'MSFT', 'YHOO', 'GOOG']
```

La méthode `split()` est utilisée pour diviser la chaîne de caractères en parties chaque fois qu'il y a un espace. Chaque partie devient ensuite un élément de la nouvelle liste.

## Accès et modification des éléments de la liste

Tout comme les chaînes de caractères, les listes prennent en charge l'indexation. L'indexation signifie que nous pouvons accéder à des éléments individuels de la liste en fonction de leur position. En Python, le premier élément d'une liste a un index de 0, le deuxième a un index de 1, et ainsi de suite. Nous pouvons également utiliser l'indexation négative pour accéder aux éléments depuis la fin de la liste. Le dernier élément a un index de -1, l'avant-dernier a un index de -2, et ainsi de suite.

Contrairement aux chaînes de caractères, les éléments de la liste peuvent être modifiés. Cela signifie que nous pouvons changer la valeur d'un élément de la liste.

```python
>>> symlist[0]    # Premier élément
'HPQ'
>>> symlist[1]    # Deuxième élément
'AAPL'
>>> symlist[-1]   # Dernier élément
'GOOG'
>>> symlist[-2]   # Avant-dernier élément
'YHOO'

>>> symlist[2] = 'AIG'    # Remplacer le troisième élément
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG']
```

## Itération à travers les listes

Souvent, nous devons effectuer la même opération sur chaque élément d'une liste. Nous pouvons utiliser une boucle `for` pour ce faire. Une boucle `for` nous permet de parcourir chaque élément de la liste un par un et d'effectuer une action spécifique sur celui-ci.

```python
>>> for s in symlist:
...     print('s =', s)
...
```

Lorsque vous exécutez ce code, vous verrez chaque élément de la liste affiché avec l'étiquette `s =`.

```
s = HPQ
s = AAPL
s = AIG
s = MSFT
s = YHOO
s = GOOG
```

## Vérification de l'appartenance

Parfois, nous devons vérifier si un élément particulier existe dans une liste. Nous pouvons utiliser l'opérateur `in` pour ce faire. L'opérateur `in` retourne `True` si l'élément est dans la liste et `False` s'il n'est pas présent.

```python
>>> 'AIG' in symlist
True
>>> 'AA' in symlist
False
>>> 'CAT' in symlist
False
```

## Ajout et suppression d'éléments

Les listes ont des méthodes intégrées qui nous permettent d'ajouter et de supprimer des éléments. La méthode `append()` ajoute un élément à la fin de la liste. La méthode `insert()` insère un élément à une position spécifique de la liste. La méthode `remove()` supprime un élément de la liste en fonction de sa valeur.

```python
>>> symlist.append('RHT')    # Ajouter un élément à la fin
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']

>>> symlist.insert(1, 'AA')    # Insérer à une position spécifique
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']

>>> symlist.remove('MSFT')    # Supprimer par valeur
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT']
```

Si vous essayez de supprimer un élément qui n'existe pas dans la liste, Python lèvera une erreur.

```python
>>> symlist.remove('MSFT')
```

Vous verrez un message d'erreur comme celui-ci :

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
```

Nous pouvons également trouver la position d'un élément dans la liste en utilisant la méthode `index()`.

```python
>>> symlist.index('YHOO')
4
>>> symlist[4]    # Vérifier l'élément à cette position
'YHOO'
```

## Tri des listes

Les listes peuvent être triées en place, ce qui signifie que la liste originale est modifiée. Nous pouvons trier une liste par ordre alphabétique ou en ordre inverse.

```python
>>> symlist.sort()    # Trier par ordre alphabétique
>>> symlist
['AA', 'AAPL', 'AIG', 'GOOG', 'HPQ', 'RHT', 'YHOO']

>>> symlist.sort(reverse=True)    # Trier en ordre inverse
>>> symlist
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
```

## Listes imbriquées

Les listes peuvent contenir tout type d'objet, y compris d'autres listes. Cela s'appelle une liste imbriquée.

```python
>>> nums = [101, 102, 103]
>>> items = [symlist, nums]
>>> items
[['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA'], [101, 102, 103]]
```

Pour accéder aux éléments d'une liste imbriquée, nous utilisons plusieurs indices. Le premier index sélectionne l'élément de la liste externe, et le deuxième index sélectionne l'élément de la liste interne.

```python
>>> items[0]    # Premier élément (la liste symlist)
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
>>> items[0][1]    # Deuxième élément de symlist
'RHT'
>>> items[0][1][2]    # Troisième caractère de 'RHT'
'T'
>>> items[1]    # Deuxième élément (la liste nums)
[101, 102, 103]
>>> items[1][1]    # Deuxième élément de nums
102
```

Lorsque vous avez terminé de travailler dans la session interactive Python, vous pouvez la quitter en tapant :

```python
>>> exit()
```
