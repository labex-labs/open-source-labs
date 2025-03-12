# Exploration du module collections

En Python, les conteneurs intégrés tels que les listes, les dictionnaires et les ensembles sont très utiles. Cependant, le module `collections` de Python va plus loin en fournissant des types de données de conteneurs spécialisés qui étendent les fonctionnalités de ces conteneurs intégrés. Examinons de plus près certains de ces types de données utiles.

Vous continuerez à travailler dans votre terminal Python et suivrez les exemples ci - dessous.

## Counter

La classe `Counter` est une sous - classe du dictionnaire. Son objectif principal est de compter les objets hachables. Elle offre un moyen pratique de compter les éléments et prend en charge diverses opérations.

Tout d'abord, nous devons importer la classe `Counter` et une fonction pour lire un portefeuille. Ensuite, nous allons lire un portefeuille à partir d'un fichier CSV.

```python
>>> from collections import Counter
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')

```

Maintenant, nous allons créer un objet `Counter` pour compter le nombre d'actions pour chaque action en fonction de son nom.

```python
# Create a counter to count shares by stock name
>>> totals = Counter()
>>> for s in portfolio:
...     totals[s['name']] += s['shares']
...
>>> print(totals)
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
```

L'une des grandes caractéristiques de l'objet `Counter` est qu'il initialise automatiquement les nouvelles clés avec un compte de 0. Cela signifie que vous n'avez pas besoin de vérifier si une clé existe avant d'incrémenter son compte, ce qui simplifie le code pour accumuler les comptes.

Les objets `Counter` ont également des méthodes spéciales. Par exemple, la méthode `most_common()` est très utile pour l'analyse de données.

```python
# Get the two stocks with the most shares
>>> most_common_stocks = totals.most_common(2)
>>> print(most_common_stocks)
[('MSFT', 250), ('IBM', 150)]
```

De plus, les objets `Counter` peuvent être combinés à l'aide d'opérations arithmétiques.

```python
# Create another counter
>>> more = Counter()
>>> more['IBM'] = 75
>>> more['AA'] = 200
>>> more['ACME'] = 30
>>> print(more)
Counter({'AA': 200, 'IBM': 75, 'ACME': 30})

# Add two counters together
>>> combined = totals + more
>>> print(combined)
Counter({'AA': 300, 'MSFT': 250, 'IBM': 225, 'CAT': 150, 'GE': 95, 'ACME': 30})
```

## defaultdict

Le `defaultdict` est similaire à un dictionnaire classique, mais il a une caractéristique unique. Il fournit une valeur par défaut pour les clés qui n'existent pas encore. Cela peut simplifier votre code, car vous n'avez plus besoin de vérifier si une clé existe avant de l'utiliser.

```python
>>> from collections import defaultdict

# Group portfolio entries by stock name
>>> byname = defaultdict(list)
>>> for s in portfolio:
...     byname[s['name']].append(s)
...
>>> print(byname['IBM'])
[{'name': 'IBM', 'shares': 50, 'price': 91.1}, {'name': 'IBM', 'shares': 100, 'price': 70.44}]
>>> print(byname['AA'])
[{'name': 'AA', 'shares': 100, 'price': 32.2}]
```

Lorsque vous créez un `defaultdict(list)`, il crée automatiquement une nouvelle liste vide pour chaque nouvelle clé. Ainsi, vous pouvez directement ajouter un élément à la valeur d'une clé même si la clé n'existait pas auparavant. Cela élimine le besoin de vérifier si la clé existe et de créer manuellement une liste vide.

Vous pouvez également utiliser d'autres fonctions de fabrique par défaut. Par exemple, vous pouvez utiliser `int`, `float` ou même votre propre fonction personnalisée.

```python
# Use defaultdict with int to count items
>>> word_counts = defaultdict(int)
>>> words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
>>> for word in words:
...     word_counts[word] += 1
...
>>> print(word_counts)
defaultdict(<class 'int'>, {'apple': 3, 'orange': 2, 'banana': 1})
```

Ces types de conteneurs spécialisés du module `collections` peuvent rendre votre code plus concis et efficace lorsque vous travaillez avec des données.
