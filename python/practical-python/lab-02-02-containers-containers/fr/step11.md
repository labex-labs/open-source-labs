# Exercice 2.6 : Dictionnaires comme conteneur

Un dictionnaire est un moyen pratique de suivre des éléments lorsque vous voulez rechercher des éléments en utilisant un index autre qu'un entier. Dans l'interpréteur Python, essayez de manipuler un dictionnaire :

```python
>>> prices = { }
>>> prices['IBM'] = 92.45
>>> prices['MSFT'] = 45.12
>>> prices
... regardez le résultat...
>>> prices['IBM']
92.45
>>> prices['AAPL']
... regardez le résultat...
>>> 'AAPL' in prices
False
>>>
```

Le fichier `prices.csv` contient une série de lignes avec des prix d'actions. Le fichier ressemble à ceci :

```csv
"AA",9.22
"AXP",24.85
"BA",44.85
"BAC",11.27
"C",3.72
...
```

Écrivez une fonction `read_prices(filename)` qui lit un ensemble de prix comme celui-ci dans un dictionnaire où les clés du dictionnaire sont les noms d'actions et les valeurs dans le dictionnaire sont les prix d'actions.

Pour ce faire, commencez par un dictionnaire vide et commencez à insérer des valeurs dedans tout comme vous l'avez fait ci-dessus. Cependant, vous lisez maintenant les valeurs à partir d'un fichier.

Nous utiliserons cette structure de données pour rechercher rapidement le prix d'un nom d'action donné.

Plusieurs petits conseils que vous aurez besoin pour cette partie. Tout d'abord, assurez-vous d'utiliser le module `csv` tout comme vous l'avez fait auparavant - il n'est pas nécessaire de réinventer la roue ici.

```python
>>> import csv
>>> f = open('/home/labex/project/prices.csv', 'r')
>>> rows = csv.reader(f)
>>> for row in rows:
        print(row)


['AA', '9.22']
['AXP', '24.85']
...
[]
>>>
```

L'autre petite complication est que le fichier `prices.csv` peut avoir quelques lignes vides. Remarquez comment la dernière ligne de données ci-dessus est une liste vide - ce qui signifie qu'aucune donnée n'était présente sur cette ligne.

Il y a une possibilité que cela fasse planter votre programme avec une exception. Utilisez les instructions `try` et `except` pour le capturer en conséquence. Pensée : serait-il mieux de protéger contre les données invalides avec une instruction `if` au lieu de cela?

Une fois que vous avez écrit votre fonction `read_prices()`, testez-la de manière interactive pour vous assurer qu'elle fonctionne :

```python
>>> prices = read_prices('/home/labex/project/prices.csv')
>>> prices['IBM']
106.28
>>> prices['MSFT']
20.89
>>>
```
