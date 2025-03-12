# Pipeline de générateurs de base avec des données CSV

Dans cette étape, nous allons apprendre à créer un pipeline de traitement de base en utilisant des générateurs. Mais d'abord, comprenons ce que sont les générateurs. Les générateurs sont un type spécial d'itérateur en Python. Contrairement aux itérateurs normaux qui peuvent charger toutes les données en mémoire d'un coup, les générateurs produisent des valeurs à la demande. Cela est extrêmement utile lorsqu'il s'agit de traiter de grands flux de données car cela économise de la mémoire. Au lieu de devoir stocker l'ensemble du jeu de données en mémoire, le générateur produit des valeurs une par une au fur et à mesure que vous en avez besoin.

## Comprendre les générateurs

Un générateur est essentiellement une fonction qui renvoie un itérateur. Lorsque vous itérez sur cet itérateur, il produit une séquence de valeurs. La façon d'écrire une fonction générateur est similaire à celle d'une fonction normale, mais il y a une différence clé. Au lieu d'utiliser l'instruction `return`, une fonction générateur utilise l'instruction `yield`. L'instruction `yield` a un comportement unique. Elle met en pause la fonction et enregistre son état actuel. Lorsque la valeur suivante est demandée, la fonction reprend là où elle s'était arrêtée. Cela permet au générateur de produire des valeurs de manière incrémentielle sans avoir à recommencer depuis le début à chaque fois.

## Utilisation de la fonction `follow()`

La fonction `follow()` que vous avez créée précédemment fonctionne de manière similaire à la commande Unix `tail -f`. La commande `tail -f` surveille en continu un fichier pour détecter de nouveaux contenus, tout comme la fonction `follow()`. Maintenant, utilisons - la pour créer un simple pipeline de traitement.

### Étape 1 : Ouvrir une nouvelle fenêtre de terminal

Tout d'abord, ouvrez une nouvelle fenêtre de terminal dans le WebIDE. Vous pouvez le faire en allant dans `Terminal → New Terminal`. Cette nouvelle fenêtre de terminal sera là où nous exécuterons nos commandes Python.

### Étape 2 : Démarrer un shell interactif Python

Une fois que la nouvelle fenêtre de terminal est ouverte, démarrez un shell interactif Python. Vous pouvez le faire en entrant la commande suivante dans le terminal :

```bash
python3
```

Le shell interactif Python vous permet d'exécuter du code Python ligne par ligne et de voir immédiatement les résultats.

### Étape 3 : Importer la fonction `follow` et configurer le pipeline

Maintenant, nous allons importer la fonction `follow` et configurer un pipeline de base pour lire les données des actions. Dans le shell interactif Python, entrez le code suivant :

```python
>>> from follow import follow
>>> import csv
>>> lines = follow('stocklog.csv')
>>> rows = csv.reader(lines)
>>> for row in rows:
...     print(row)
...
```

Voici ce que chaque ligne fait :

- `from follow import follow` : Cela importe la fonction `follow` du module `follow`.
- `import csv` : Cela importe le module `csv`, qui est utilisé pour lire et écrire des fichiers CSV en Python.
- `lines = follow('stocklog.csv')` : Cela appelle la fonction `follow` avec le nom de fichier `stocklog.csv`. La fonction `follow` renvoie un générateur qui produit de nouvelles lignes au fur et à mesure qu'elles sont ajoutées au fichier.
- `rows = csv.reader(lines)` : La fonction `csv.reader()` prend les lignes générées par la fonction `follow` et les analyse en lignes de données CSV.
- La boucle `for` itère à travers ces lignes et les affiche une par une.

### Étape 4 : Vérifier la sortie

Après avoir exécuté le code, vous devriez voir une sortie similaire à ceci (vos données varieront) :

```
['BA', '98.35', '6/11/2007', '09:41.07', '0.16', '98.25', '98.35', '98.31', '158148']
['AA', '39.63', '6/11/2007', '09:41.07', '-0.03', '39.67', '39.63', '39.31', '270224']
['XOM', '82.45', '6/11/2007', '09:41.07', '-0.23', '82.68', '82.64', '82.41', '748062']
['PG', '62.95', '6/11/2007', '09:41.08', '-0.12', '62.80', '62.97', '62.61', '454327']
...
```

Cette sortie indique que vous avez créé avec succès un pipeline de données. La fonction `follow()` génère des lignes à partir du fichier, et ces lignes sont ensuite transmises à la fonction `csv.reader()`, qui les analyse en lignes de données.

Si vous avez vu assez de résultats, vous pouvez arrêter l'exécution en appuyant sur `Ctrl+C`.

## Qu'est - ce qui se passe ?

Décortiquons ce qui se passe dans ce pipeline :

1. `follow('stocklog.csv')` crée un générateur. Ce générateur suit le fichier `stocklog.csv` et produit de nouvelles lignes au fur et à mesure qu'elles sont ajoutées au fichier.
2. `csv.reader(lines)` prend les lignes générées par la fonction `follow` et les analyse en données de ligne CSV. Il comprend la structure des fichiers CSV et divise les lignes en valeurs individuelles.
3. La boucle `for` itère ensuite à travers ces lignes, les affichant une par une. Cela vous permet de voir les données dans un format lisible.

Ceci est un exemple simple d'un pipeline de traitement de données utilisant des générateurs. Dans les étapes suivantes, nous allons construire des pipelines plus complexes et utiles.
