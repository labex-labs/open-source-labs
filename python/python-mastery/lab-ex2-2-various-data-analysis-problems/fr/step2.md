# Utilisation des compréhensions de listes, d'ensembles et de dictionnaires

Les compréhensions en Python sont un moyen très utile et concis de créer de nouvelles collections à partir d'existantes. Les collections en Python peuvent être des listes, des ensembles ou des dictionnaires, qui sont comme des conteneurs pour différents types de données. Les compréhensions vous permettent de filtrer certaines données, de les transformer d'une certaine manière et de les organiser plus efficacement. Dans cette partie, nous allons utiliser nos données de portefeuille pour explorer le fonctionnement de ces compréhensions.

Tout d'abord, vous devez ouvrir un terminal Python, comme vous l'avez fait à l'étape précédente. Une fois le terminal ouvert, vous allez entrer les exemples suivants un par un. Cette approche pratique vous aidera à comprendre le fonctionnement des compréhensions dans la pratique.

## Compréhensions de listes

Une compréhension de liste est une syntaxe spéciale en Python qui crée une nouvelle liste. Elle le fait en appliquant une expression à chaque élément d'une collection existante.

Commençons par un exemple. Tout d'abord, nous allons importer une fonction pour lire nos données de portefeuille. Ensuite, nous utiliserons une compréhension de liste pour filtrer certains titres du portefeuille.

```python
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')

# Find all holdings with more than 100 shares
>>> large_holdings = [s for s in portfolio if s['shares'] > 100]
>>> print(large_holdings)
[{'name': 'CAT', 'shares': 150, 'price': 83.44}, {'name': 'MSFT', 'shares': 200, 'price': 51.23}]
```

Dans ce code, nous importons d'abord la fonction `read_portfolio` et l'utilisons pour lire les données du portefeuille à partir d'un fichier CSV. Ensuite, la compréhension de liste `[s for s in portfolio if s['shares'] > 100]` parcourt chaque élément `s` de la collection `portfolio`. Elle n'inclut l'élément `s` dans la nouvelle liste `large_holdings` que si le nombre d'actions de ce titre est supérieur à 100.

Les compréhensions de listes peuvent également être utilisées pour effectuer des calculs. Voici quelques exemples :

```python
# Calculate the total cost of each holding (shares * price)
>>> holding_costs = [s['shares'] * s['price'] for s in portfolio]
>>> print(holding_costs)
[3220.0, 4555.0, 12516.0, 10246.0, 3835.15, 3255.0, 7044.0]

# Calculate the total cost of the entire portfolio
>>> total_portfolio_cost = sum([s['shares'] * s['price'] for s in portfolio])
>>> print(total_portfolio_cost)
44671.15
```

Dans le premier exemple, la compréhension de liste `[s['shares'] * s['price'] for s in portfolio]` calcule le coût total de chaque titre en multipliant le nombre d'actions par le prix pour chaque élément du `portfolio`. Dans le deuxième exemple, nous utilisons la fonction `sum` avec la compréhension de liste pour calculer le coût total de l'ensemble du portefeuille.

## Compréhensions d'ensembles

Une compréhension d'ensemble est utilisée pour créer un ensemble à partir d'une collection existante. Un ensemble est une collection qui ne contient que des valeurs uniques.

Voyons comment cela fonctionne avec nos données de portefeuille :

```python
# Find all unique stock names
>>> unique_stocks = {s['name'] for s in portfolio}
>>> print(unique_stocks)
{'MSFT', 'IBM', 'AA', 'GE', 'CAT'}
```

Dans ce code, la compréhension d'ensemble `{s['name'] for s in portfolio}` parcourt chaque élément `s` du `portfolio` et ajoute le nom de l'action (`s['name']`) à l'ensemble `unique_stocks`. Comme les ensembles ne stockent que des valeurs uniques, nous obtenons une liste de toutes les différentes actions de notre portefeuille sans doublons.

## Compréhensions de dictionnaires

Une compréhension de dictionnaire crée un nouveau dictionnaire en appliquant des expressions pour créer des paires clé - valeur.

Voici un exemple d'utilisation d'une compréhension de dictionnaire pour compter le nombre total d'actions pour chaque action de notre portefeuille :

```python
# Create a dictionary to count total shares for each stock
>>> totals = {s['name']: 0 for s in portfolio}
>>> for s in portfolio:
...     totals[s['name']] += s['shares']
...
>>> print(totals)
{'AA': 100, 'IBM': 150, 'CAT': 150, 'MSFT': 250, 'GE': 95}
```

Dans la première ligne, la compréhension de dictionnaire `{s['name']: 0 for s in portfolio}` crée un dictionnaire où chaque nom d'action (`s['name']`) est une clé, et la valeur initiale de chaque clé est 0. Ensuite, nous utilisons une boucle `for` pour parcourir chaque élément du `portfolio`. Pour chaque élément, nous ajoutons le nombre d'actions (`s['shares']`) à la valeur correspondante dans le dictionnaire `totals`.

Ces compréhensions sont très puissantes car elles vous permettent de transformer et d'analyser des données avec seulement quelques lignes de code. Elles sont un excellent outil à avoir dans votre boîte à outils de programmation Python.
