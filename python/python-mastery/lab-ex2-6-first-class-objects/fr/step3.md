# Exploration du modèle mémoire de Python

Le modèle mémoire de Python joue un rôle crucial dans la détermination de la manière dont les objets sont stockés en mémoire et de la façon dont ils sont référencés. Comprendre ce modèle est essentiel, surtout lorsqu'on travaille avec de grands ensembles de données, car cela peut avoir un impact significatif sur les performances et l'utilisation de la mémoire de vos programmes Python. Dans cette étape, nous allons nous concentrer spécifiquement sur la façon dont les objets de type chaîne de caractères sont gérés en Python et explorer des moyens d'optimiser l'utilisation de la mémoire pour de grands ensembles de données.

## Répétition de chaînes de caractères dans les ensembles de données

Les données des bus CTA contiennent de nombreuses valeurs répétées, telles que les noms d'itinéraires. Les valeurs répétées dans un ensemble de données peuvent entraîner une utilisation inefficace de la mémoire si elles ne sont pas gérées correctement. Pour comprendre l'ampleur de ce problème, examinons d'abord combien de chaînes d'itinéraires uniques se trouvent dans l'ensemble de données.

Tout d'abord, ouvrez un interpréteur Python. Vous pouvez le faire en exécutant la commande suivante dans votre terminal :

```bash
python3
```

Une fois l'interpréteur Python ouvert, nous allons charger les données des bus CTA et trouver les itinéraires uniques. Voici le code pour y parvenir :

```python
import reader
rows = reader.read_csv_as_dicts('ctabus.csv', [str, str, str, int])

# Find unique route names
routes = {row['route'] for row in rows}
print(f"Number of unique route names: {len(routes)}")
```

Dans ce code, nous importons d'abord le module `reader`, qui contient probablement une fonction pour lire les fichiers CSV sous forme de dictionnaires. Nous utilisons ensuite la fonction `read_csv_as_dicts` pour charger les données du fichier `ctabus.csv`. Le deuxième argument `[str, str, str, int]` spécifie les types de données pour chaque colonne du fichier CSV. Ensuite, nous utilisons une compréhension d'ensemble pour trouver tous les noms d'itinéraires uniques dans l'ensemble de données et afficher le nombre de noms d'itinéraires uniques.

La sortie devrait être :

```
Number of unique route names: 181
```

Maintenant, vérifions combien d'objets de chaîne de caractères différents sont créés pour ces itinéraires. Même s'il n'y a que 181 noms d'itinéraires uniques, Python peut créer un nouvel objet de chaîne de caractères pour chaque occurrence d'un nom d'itinéraire dans l'ensemble de données. Pour vérifier cela, nous allons utiliser la fonction `id()` pour obtenir l'identifiant unique de chaque objet de chaîne de caractères.

```python
# Count unique string object IDs
routeids = {id(row['route']) for row in rows}
print(f"Number of unique route string objects: {len(routeids)}")
```

La sortie peut vous surprendre :

```
Number of unique route string objects: 542305
```

Cela montre qu'il n'y a que 181 noms d'itinéraires uniques, mais plus de 500 000 objets de chaîne de caractères uniques. Cela se produit car Python crée un nouvel objet de chaîne de caractères pour chaque ligne, même si les valeurs sont les mêmes. Cela peut entraîner un gaspillage de mémoire important, surtout lorsqu'on travaille avec de grands ensembles de données.

## Internement de chaînes de caractères pour économiser de la mémoire

Python propose un moyen d'"interner" (réutiliser) les chaînes de caractères à l'aide de la fonction `sys.intern()`. L'internement de chaînes de caractères peut économiser de la mémoire lorsque vous avez de nombreuses chaînes de caractères dupliquées dans votre ensemble de données. Lorsque vous internez une chaîne de caractères, Python vérifie si une chaîne identique existe déjà dans le pool d'internement. Si c'est le cas, il retourne une référence à l'objet de chaîne de caractères existant au lieu de créer un nouveau.

Démontrons comment fonctionne l'internement de chaînes de caractères avec un exemple simple :

```python
import sys

# Without interning
a = 'hello world'
b = 'hello world'
print(f"a is b (without interning): {a is b}")

# With interning
a = sys.intern(a)
b = sys.intern(b)
print(f"a is b (with interning): {a is b}")
```

Dans ce code, nous créons d'abord deux variables de chaîne de caractères `a` et `b` avec la même valeur sans interner. L'opérateur `is` vérifie si deux variables font référence au même objet. Sans interner, `a` et `b` sont des objets différents, donc `a is b` retourne `False`. Ensuite, nous internons les deux chaînes de caractères à l'aide de `sys.intern()`. Après l'internement, `a` et `b` font référence au même objet dans le pool d'internement, donc `a is b` retourne `True`.

La sortie devrait être :

```
a is b (without interning): False
a is b (with interning): True
```

Maintenant, utilisons l'internement de chaînes de caractères lors de la lecture des données des bus CTA pour réduire l'utilisation de la mémoire. Nous allons également utiliser le module `tracemalloc` pour suivre l'utilisation de la mémoire avant et après l'internement.

```python
import sys
import reader
import tracemalloc

# Start memory tracking
tracemalloc.start()

# Read data with interning for the route column
rows = reader.read_csv_as_dicts('ctabus.csv', [sys.intern, str, str, int])

# Check unique route objects again
routeids = {id(row['route']) for row in rows}
print(f"Number of unique route string objects (with interning): {len(routeids)}")

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")
```

Dans ce code, nous démarrons d'abord le suivi de la mémoire à l'aide de `tracemalloc.start()`. Ensuite, nous lisons les données des bus CTA en internant les chaînes de caractères de la colonne des itinéraires en passant `sys.intern` comme type de données pour la première colonne. Ensuite, nous vérifions à nouveau le nombre d'objets de chaîne de caractères d'itinéraire uniques et affichons l'utilisation actuelle et maximale de la mémoire.

La sortie devrait être quelque chose comme :

```
Number of unique route string objects (with interning): 181
Current memory usage: 189.56 MB
Peak memory usage: 209.32 MB
```

Redémarrons l'interpréteur et essayons d'interner à la fois les chaînes d'itinéraire et de date pour voir si nous pouvons réduire encore plus l'utilisation de la mémoire.

```python
exit()
```

Relancez Python :

```bash
python3
```

```python
import sys
import reader
import tracemalloc

# Start memory tracking
tracemalloc.start()

# Read data with interning for both route and date columns
rows = reader.read_csv_as_dicts('ctabus.csv', [sys.intern, sys.intern, str, int])

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage (interning route and date): {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage (interning route and date): {peak / 1024 / 1024:.2f} MB")
```

La sortie devrait montrer une nouvelle diminution de l'utilisation de la mémoire :

```
Current memory usage (interning route and date): 170.23 MB
Peak memory usage (interning route and date): 190.05 MB
```

Cela démontre comment la compréhension du modèle mémoire de Python et l'utilisation de techniques telles que l'internement de chaînes de caractères peuvent aider à optimiser vos programmes, surtout lorsqu'on travaille avec de grands ensembles de données contenant des valeurs répétées.

Enfin, quittez l'interpréteur Python :

```python
exit()
```
