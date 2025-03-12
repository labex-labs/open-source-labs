# Utilisation des fonctions `enumerate()` et `zip()`

Dans cette étape, nous allons explorer deux fonctions intégrées incroyablement utiles en Python, essentielles pour l'itération : `enumerate()` et `zip()`. Ces fonctions peuvent considérablement simplifier votre code lorsque vous travaillez avec des séquences.

## Compter avec `enumerate()`

Lorsque vous itérez sur une séquence, vous aurez souvent besoin de suivre l'index ou la position de chaque élément. C'est là que la fonction `enumerate()` est pratique. La fonction `enumerate()` prend une séquence en entrée et renvoie des paires (index, valeur) pour chaque élément de cette séquence.

Si vous avez suivi dans l'interpréteur Python de l'étape précédente, vous pouvez continuer à l'utiliser. Sinon, démarrez une nouvelle session. Voici comment vous pouvez configurer les données si vous commencez à zéro :

```python
# Si vous démarrez une nouvelle session, rechargez d'abord les données :
# import csv
# f = open('portfolio.csv')
# f_csv = csv.reader(f)
# headers = next(f_csv)
# rows = list(f_csv)

# Utilisez enumerate pour obtenir les numéros de ligne
for rowno, row in enumerate(rows):
    print(rowno, row)
```

Lorsque vous exécutez le code ci - dessus, la fonction `enumerate(rows)` générera des paires d'un index (commençant à 0) et de la ligne correspondante de la séquence `rows`. La boucle `for` déballera ensuite ces paires dans les variables `rowno` et `row`, et nous les afficherons.

Sortie :

```
0 ['AA', '100', '32.20']
1 ['IBM', '50', '91.10']
2 ['CAT', '150', '83.44']
3 ['MSFT', '200', '51.23']
4 ['GE', '95', '40.37']
5 ['MSFT', '50', '65.10']
6 ['IBM', '100', '70.44']
```

Nous pouvons rendre le code encore plus lisible en combinant `enumerate()` avec le déballage. Le déballage nous permet d'assigner directement les éléments d'une séquence à des variables individuelles.

```python
for rowno, (name, shares, price) in enumerate(rows):
    print(rowno, name, shares, price)
```

Dans ce code, nous utilisons une paire supplémentaire de parenthèses autour de `(name, shares, price)` pour déballer correctement les données de la ligne. `enumerate(rows)` nous donne toujours l'index et la ligne, mais maintenant nous déballons la ligne dans les variables `name`, `shares` et `price`.

Sortie :

```
0 AA 100 32.20
1 IBM 50 91.10
2 CAT 150 83.44
3 MSFT 200 51.23
4 GE 95 40.37
5 MSFT 50 65.10
6 IBM 100 70.44
```

## Mise en paires de données avec `zip()`

La fonction `zip()` est un autre outil puissant en Python. Elle est utilisée pour combiner les éléments correspondants de plusieurs séquences. Lorsque vous passez plusieurs séquences à `zip()`, elle crée un itérateur qui produit des tuples, où chaque tuple contient des éléments de chacune des séquences d'entrée à la même position.

Voyons comment nous pouvons utiliser `zip()` avec les données `headers` et `row` avec lesquelles nous avons travaillé.

```python
# Rappelez-vous la variable headers de plus tôt
print(headers)  # Devrait afficher ['name', 'shares', 'price']

# Obtenez la première ligne
row = rows[0]
print(row)      # Devrait afficher ['AA', '100', '32.20']

# Utilisez zip pour associer les noms de colonnes aux valeurs
for col, val in zip(headers, row):
    print(col, val)
```

Dans ce code, `zip(headers, row)` prend la séquence `headers` et la séquence `row` et met en paires leurs éléments correspondants. La boucle `for` déballera ensuite ces paires dans `col` (pour le nom de colonne de `headers`) et `val` (pour la valeur de `row`), et nous les afficherons.

Sortie :

```
['name', 'shares', 'price']
['AA', '100', '32.20']
name AA
shares 100
price 32.20
```

Un usage très courant de `zip()` est de créer des dictionnaires à partir de paires clé - valeur. En Python, un dictionnaire est une collection de paires clé - valeur.

```python
# Créez un dictionnaire à partir des en-têtes et des valeurs de ligne
record = dict(zip(headers, row))
print(record)
```

Ici, `zip(headers, row)` crée des paires de noms de colonnes et de valeurs, et la fonction `dict()` prend ces paires et les transforme en un dictionnaire.

Sortie :

```
{'name': 'AA', 'shares': '100', 'price': '32.20'}
```

Nous pouvons étendre cette idée pour convertir toutes les lignes de notre séquence `rows` en dictionnaires.

```python
# Convertissez toutes les lignes en dictionnaires
for row in rows:
    record = dict(zip(headers, row))
    print(record)
```

Dans cette boucle, pour chaque ligne de `rows`, nous utilisons `zip(headers, row)` pour créer des paires clé - valeur, puis `dict()` pour transformer ces paires en un dictionnaire. Cette technique est très courante dans les applications de traitement de données, en particulier lorsque vous travaillez avec des fichiers CSV où la première ligne contient les en-têtes.

Sortie :

```
{'name': 'AA', 'shares': '100', 'price': '32.20'}
{'name': 'IBM', 'shares': '50', 'price': '91.10'}
{'name': 'CAT', 'shares': '150', 'price': '83.44'}
{'name': 'MSFT', 'shares': '200', 'price': '51.23'}
{'name': 'GE', 'shares': '95', 'price': '40.37'}
{'name': 'MSFT', 'shares': '50', 'price': '65.10'}
{'name': 'IBM', 'shares': '100', 'price': '70.44'}
```
