# Itération de base et déballage de séquences

Dans cette étape, nous allons explorer l'itération de base à l'aide de boucles `for` et le déballage de séquences en Python. L'itération est un concept fondamental en programmation, qui vous permet de parcourir chaque élément d'une séquence un par un. Le déballage de séquences, quant à lui, vous permet d'assigner les éléments individuels d'une séquence à des variables de manière pratique.

## Chargement de données depuis un fichier CSV

Commençons par charger des données depuis un fichier CSV. CSV (Comma-Separated Values, valeurs séparées par des virgules) est un format de fichier courant utilisé pour stocker des données tabulaires. Pour commencer, nous devons ouvrir un terminal dans le WebIDE et démarrer l'interpréteur Python. Cela nous permettra d'exécuter du code Python de manière interactive.

```bash
cd ~/project
python3
```

Maintenant que nous sommes dans l'interpréteur Python, nous pouvons exécuter le code Python suivant pour lire les données depuis le fichier `portfolio.csv`. Tout d'abord, nous importons le module `csv`, qui fournit des fonctionnalités pour travailler avec les fichiers CSV. Ensuite, nous ouvrons le fichier et créons un objet `csv.reader` pour lire les données. Nous utilisons la fonction `next` pour obtenir les en-têtes de colonne, et nous convertissons les données restantes en une liste. Enfin, nous utilisons la fonction `pprint` du module `pprint` pour afficher les lignes d'une manière plus lisible.

```python
import csv

f = open('portfolio.csv')
f_csv = csv.reader(f)
headers = next(f_csv)    # Obtenir les en-têtes de colonne
rows = list(f_csv)       # Convertir les données restantes en une liste
from pprint import pprint
pprint(rows)             # Afficher les lignes de manière lisible
```

Vous devriez voir une sortie similaire à ceci :

```
[['AA', '100', '32.20'],
 ['IBM', '50', '91.10'],
 ['CAT', '150', '83.44'],
 ['MSFT', '200', '51.23'],
 ['GE', '95', '40.37'],
 ['MSFT', '50', '65.10'],
 ['IBM', '100', '70.44']]
```

## Itération de base avec des boucles `for`

La déclaration `for` en Python est utilisée pour itérer sur n'importe quelle séquence de données, comme une liste, un tuple ou une chaîne de caractères. Dans notre cas, nous l'utiliserons pour itérer sur les lignes de données que nous avons chargées depuis le fichier CSV.

```python
for row in rows:
    print(row)
```

Ce code parcourra chaque ligne de la liste `rows` et l'affichera. Vous verrez chaque ligne de données de notre fichier CSV affichée une par une.

```
['AA', '100', '32.20']
['IBM', '50', '91.10']
['CAT', '150', '83.44']
['MSFT', '200', '51.23']
['GE', '95', '40.37']
['MSFT', '50', '65.10']
['IBM', '100', '70.44']
```

## Déballage de séquences dans les boucles

Python vous permet de déballer des séquences directement dans une boucle `for`. Cela est très utile lorsque vous connaissez la structure de chaque élément de la séquence. Dans notre cas, chaque ligne de la liste `rows` contient trois éléments : un nom, le nombre d'actions et le prix. Nous pouvons déballer ces éléments directement dans la boucle `for`.

```python
for name, shares, price in rows:
    print(name, shares, price)
```

Ce code déballera chaque ligne dans les variables `name`, `shares` et `price`, puis les affichera. Vous verrez les données affichées dans un format plus lisible.

```
AA 100 32.20
IBM 50 91.10
CAT 150 83.44
MSFT 200 51.23
GE 95 40.37
MSFT 50 65.10
IBM 100 70.44
```

Si vous n'avez pas besoin de certaines valeurs, vous pouvez utiliser `_` comme espace réservé pour indiquer que vous n'avez pas besoin de ces valeurs. Par exemple, si vous ne voulez afficher que le nom et le prix, vous pouvez utiliser le code suivant :

```python
for name, _, price in rows:
    print(name, price)
```

Ce code ignorera le deuxième élément de chaque ligne et n'affichera que le nom et le prix.

```
AA 32.20
IBM 91.10
CAT 83.44
MSFT 51.23
GE 40.37
MSFT 65.10
IBM 70.44
```

## Déballage étendu avec l'opérateur `*`

Pour un déballage plus avancé, vous pouvez utiliser l'opérateur `*` comme joker. Cela vous permet de collecter plusieurs éléments dans une liste. Groupons nos données par nom en utilisant cette technique.

```python
from collections import defaultdict

byname = defaultdict(list)
for name, *data in rows:
    byname[name].append(data)

# Afficher les données pour IBM
print(byname['IBM'])

# Itérer à travers les données d'IBM
for shares, price in byname['IBM']:
    print(shares, price)
```

Dans ce code, nous importons d'abord la classe `defaultdict` du module `collections`. Un `defaultdict` est un dictionnaire qui crée automatiquement une nouvelle valeur (dans ce cas, une liste vide) si la clé n'existe pas. Ensuite, nous utilisons l'opérateur `*` pour collecter tous les éléments sauf le premier dans une liste appelée `data`. Nous stockons cette liste dans le dictionnaire `byname`, groupée par nom. Enfin, nous affichons les données pour IBM et nous les parcourons pour afficher le nombre d'actions et le prix.

Sortie :

```
[['50', '91.10'], ['100', '70.44']]
50 91.10
100 00.44
```

Dans cet exemple, `*data` collecte tous les éléments sauf le premier dans une liste, que nous stockons ensuite dans un dictionnaire groupé par nom. C'est une technique puissante pour gérer des données avec des séquences de longueur variable.
