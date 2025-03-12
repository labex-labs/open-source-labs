# Comprendre les objets de première classe en Python

En Python, tout est considéré comme un objet. Cela inclut les fonctions et les types. Que signifie cela ? Eh bien, cela signifie que vous pouvez stocker des fonctions et des types dans des structures de données, les passer en tant qu'arguments à d'autres fonctions et même les retourner depuis d'autres fonctions. C'est un concept très puissant, et nous allons l'explorer en utilisant le traitement de données CSV comme exemple.

## Explorer les types de première classe

Tout d'abord, lançons l'interpréteur Python. Ouvrez un nouveau terminal dans le WebIDE et tapez la commande suivante. Cette commande lancera l'interpréteur Python, où nous allons exécuter notre code Python.

```bash
python3
```

Lorsque nous travaillons avec des fichiers CSV en Python, nous avons souvent besoin de convertir les chaînes de caractères que nous lisons à partir de ces fichiers en types de données appropriés. Par exemple, un nombre dans un fichier CSV peut être lu comme une chaîne de caractères, mais nous voulons l'utiliser comme un entier ou un nombre à virgule flottante dans notre code Python. Pour ce faire, nous pouvons créer une liste de fonctions de conversion.

```python
coltypes = [str, int, float]
```

Remarquez que nous créons une liste qui contient les fonctions de type réelles, pas des chaînes de caractères. En Python, les types sont des objets de première classe, ce qui signifie que nous pouvons les traiter comme n'importe quel autre objet. Nous pouvons les mettre dans des listes, les passer d'un endroit à un autre et les utiliser dans notre code.

Maintenant, lisons des données à partir d'un fichier CSV de portefeuille pour voir comment nous pouvons utiliser ces fonctions de conversion.

```python
import csv
f = open('portfolio.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
print(row)
```

Lorsque vous exécutez ce code, vous devriez voir une sortie similaire à la suivante. Ceci est la première ligne de données du fichier CSV, représentée sous forme de liste de chaînes de caractères.

```
['AA', '100', '32.20']
```

Ensuite, nous allons utiliser la fonction `zip`. La fonction `zip` prend plusieurs itérables (comme des listes ou des tuples) et associe leurs éléments. Nous l'utiliserons pour associer chaque valeur de la ligne à sa fonction de conversion de type correspondante.

```python
r = list(zip(coltypes, row))
print(r)
```

Cela produira la sortie suivante. Chaque paire contient une fonction de type et une valeur sous forme de chaîne de caractères provenant du fichier CSV.

```
[(<class 'str'>, 'AA'), (<class 'int'>, '100'), (<class 'float'>, '32.20')]
```

Maintenant que nous avons ces paires, nous pouvons appliquer chaque fonction pour convertir les valeurs en leurs types appropriés.

```python
record = [func(val) for func, val in zip(coltypes, row)]
print(record)
```

La sortie montrera que les valeurs ont été converties en leurs types appropriés. La chaîne de caractères 'AA' reste une chaîne de caractères, '100' devient l'entier 100 et '32.20' devient le nombre à virgule flottante 32.2.

```
['AA', 100, 32.2]
```

Nous pouvons également combiner ces valeurs avec leurs noms de colonnes pour créer un dictionnaire. Un dictionnaire est une structure de données utile en Python qui nous permet de stocker des paires clé - valeur.

```python
record_dict = dict(zip(headers, record))
print(record_dict)
```

La sortie sera un dictionnaire où les clés sont les noms de colonnes et les valeurs sont les données converties.

```
{'name': 'AA', 'shares': 100, 'price': 32.2}
```

Vous pouvez effectuer toutes ces étapes dans une seule compréhension. Une compréhension est un moyen concis de créer des listes, des dictionnaires ou des ensembles en Python.

```python
result = {name: func(val) for name, func, val in zip(headers, coltypes, row)}
print(result)
```

La sortie sera le même dictionnaire que précédemment.

```
{'name': 'AA', 'shares': 100, 'price': 32.2}
```

Lorsque vous avez terminé de travailler dans l'interpréteur Python, vous pouvez le quitter en tapant la commande suivante.

```python
exit()
```

Cette démonstration montre comment le traitement des fonctions en tant qu'objets de première classe en Python permet des techniques de traitement de données puissantes. En étant capable de traiter les types et les fonctions comme des objets, nous pouvons écrire un code plus flexible et concis.
