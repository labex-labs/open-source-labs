# Défi d'analyse de données avec les données de l'Autorité de transport en commun de Chicago

Maintenant que vous avez pratiqué le travail avec différentes structures de données Python et le module `collections`, il est temps de mettre ces compétences en pratique dans une tâche d'analyse de données du monde réel. Dans cette expérience, nous allons analyser les données de fréquentation des bus de l'Autorité de transport en commun de Chicago (CTA). Cette application pratique vous aidera à comprendre comment utiliser Python pour extraire des informations significatives à partir de jeux de données du monde réel.

## Compréhension des données

Tout d'abord, regardons les données de transport avec lesquelles nous allons travailler. Dans votre terminal Python, vous allez exécuter un peu de code pour charger les données et comprendre leur structure de base.

```python
>>> import readrides
>>> rows = readrides.read_rides_as_dicts('/home/labex/project/ctabus.csv')
>>> print(len(rows))
# This will show the number of records in the dataset

>>> # Let's look at the first record to understand the structure
>>> import pprint
>>> pprint.pprint(rows[0])
```

L'instruction `import readrides` importe un module personnalisé qui a une fonction pour lire les données à partir du fichier CSV. La fonction `readrides.read_rides_as_dicts` lit les données à partir du fichier CSV spécifié et convertit chaque ligne en un dictionnaire. `len(rows)` nous donne le nombre total d'enregistrements dans le jeu de données. En imprimant le premier enregistrement à l'aide de `pprint.pprint(rows[0])`, nous pouvons voir clairement la structure de chaque enregistrement.

Les données contiennent des enregistrements quotidiens de fréquentation pour différents itinéraires de bus. Chaque enregistrement comprend :

- `route` : Le numéro de l'itinéraire de bus
- `date` : La date au format "YYYY - MM - DD"
- `daytype` : Soit "W" pour un jour de semaine, "A" pour un samedi, ou "U" pour un dimanche/jour férié
- `rides` : Le nombre de passagers ce jour - là

## Tâches d'analyse

Résolvons chacune des questions du défi une par une :

### Question 1 : Combien d'itinéraires de bus existent à Chicago ?

Pour répondre à cette question, nous devons trouver tous les numéros d'itinéraire uniques dans le jeu de données. Nous utiliserons une compréhension d'ensemble pour cette tâche.

```python
>>> # Get all unique route numbers using a set comprehension
>>> unique_routes = {row['route'] for row in rows}
>>> print(len(unique_routes))
```

Une compréhension d'ensemble est un moyen concis de créer un ensemble. Dans ce cas, nous parcourons chaque ligne de la liste `rows` et extrayons la valeur `route`. Comme un ensemble ne stocke que des éléments uniques, nous obtenons un ensemble de tous les numéros d'itinéraire uniques. En imprimant la longueur de cet ensemble, nous obtenons le nombre total d'itinéraires de bus uniques.

Nous pouvons également voir quels sont certains de ces itinéraires :

```python
>>> # Print a few of the route numbers
>>> print(list(unique_routes)[:10])
```

Ici, nous convertissons l'ensemble d'itinéraires uniques en une liste et imprimons ensuite les 10 premiers éléments de cette liste.

### Question 2 : Combien de personnes ont pris le bus numéro 22 le 2 février 2011 ?

Pour cette question, nous devons filtrer les données pour trouver l'enregistrement spécifique qui correspond à l'itinéraire et à la date donnés.

```python
>>> # Find rides on route 22 on February 2, 2011
>>> target_date = "2011-02-02"
>>> target_route = "22"
>>>
>>> for row in rows:
...     if row['route'] == target_route and row['date'] == target_date:
...         print(f"Rides on route {target_route} on {target_date}: {row['rides']}")
...         break
```

Nous définissons d'abord les variables `target_date` et `target_route`. Ensuite, nous parcourons chaque ligne de la liste `rows`. Pour chaque ligne, nous vérifions si l'itinéraire et la date correspondent à nos valeurs cibles. Si une correspondance est trouvée, nous imprimons le nombre de passagers et nous sortons de la boucle car nous avons trouvé l'enregistrement que nous recherchions.

Vous pouvez modifier ce code pour vérifier n'importe quel itinéraire à n'importe quelle date en changeant les variables `target_date` et `target_route`.

### Question 3 : Quel est le nombre total de passagers par itinéraire de bus ?

Utilisons un `Counter` pour calculer le nombre total de passagers par itinéraire. Un `Counter` est une sous - classe de dictionnaire du module `collections` qui est utilisée pour compter les objets hachables.

```python
>>> from collections import Counter
>>>
>>> # Initialize a counter
>>> total_rides_by_route = Counter()
>>>
>>> # Sum up rides for each route
>>> for row in rows:
...     total_rides_by_route[row['route']] += row['rides']
...
>>> # View the top 5 routes by total ridership
>>> for route, rides in total_rides_by_route.most_common(5):
...     print(f"Route {route}: {rides:,} total rides")
```

Nous importons d'abord la classe `Counter` du module `collections`. Ensuite, nous initialisons un compteur vide appelé `total_rides_by_route`. Lorsque nous parcourons chaque ligne de la liste `rows`, nous ajoutons le nombre de passagers pour chaque itinéraire au compteur. Enfin, nous utilisons la méthode `most_common(5)` pour obtenir les 5 itinéraires avec le plus grand nombre total de passagers et imprimons les résultats.

### Question 4 : Quels sont les cinq itinéraires de bus qui ont connu la plus forte augmentation de fréquentation sur dix ans de 2001 à 2011 ?

C'est une tâche plus complexe. Nous devons comparer la fréquentation en 2001 avec celle de 2011 pour chaque itinéraire.

```python
>>> # Create dictionaries to store total annual rides by route
>>> rides_2001 = Counter()
>>> rides_2011 = Counter()
>>>
>>> # Collect data for each year
>>> for row in rows:
...     if row['date'].startswith('2001-'):
...         rides_2001[row['route']] += row['rides']
...     elif row['date'].startswith('2011-'):
...         rides_2011[row['route']] += row['rides']
...
>>> # Calculate increases
>>> increases = {}
>>> for route in unique_routes:
...     if route in rides_2001 and route in rides_2011:
...         increase = rides_2011[route] - rides_2001[route]
...         increases[route] = increase
...
>>> # Find the top 5 routes with the biggest increases
>>> import heapq
>>> top_5_increases = heapq.nlargest(5, increases.items(), key=lambda x: x[1])
>>>
>>> # Display the results
>>> print("Top 5 routes with the greatest ridership increase from 2001 to 2011:")
>>> for route, increase in top_5_increases:
...     print(f"Route {route}: increased by {increase:,} rides")
...     print(f"  2001 rides: {rides_2001[route]:,}")
...     print(f"  2011 rides: {rides_2011[route]:,}")
...     print()
```

Nous créons d'abord deux objets `Counter`, `rides_2001` et `rides_2011`, pour stocker le nombre total de passagers pour chaque itinéraire en 2001 et 2011 respectivement. Lorsque nous parcourons chaque ligne de la liste `rows`, nous vérifions si la date commence par '2001 -' ou '2011 -' et ajoutons les passagers au compteur approprié.

Ensuite, nous créons un dictionnaire vide `increases` pour stocker l'augmentation de la fréquentation pour chaque itinéraire. Nous parcourons les itinéraires uniques et calculons l'augmentation en soustrayant le nombre de passagers en 2001 du nombre de passagers en 2011 pour chaque itinéraire.

Pour trouver les 5 itinéraires avec les plus grandes augmentations, nous utilisons la fonction `heapq.nlargest`. Cette fonction prend le nombre d'éléments à retourner (5 dans ce cas), l'itérable (`increases.items()`) et une fonction clé (`lambda x: x[1]`) qui spécifie comment comparer les éléments.

Enfin, nous imprimons les résultats, montrant le numéro de l'itinéraire, l'augmentation de la fréquentation et le nombre de passagers en 2001 et 2011.

Cette analyse identifie quels itinéraires de bus ont connu la plus forte croissance de la fréquentation au cours de la décennie, ce qui pourrait indiquer des changements dans les modèles de population, des améliorations des services ou d'autres tendances intéressantes.

Vous pouvez étendre ces analyses de nombreuses manières. Par exemple, vous pourriez :

- Analyser les modèles de fréquentation en fonction du jour de la semaine
- Trouver les itinéraires dont la fréquentation diminue
- Comparer les variations saisonnières de la fréquentation

Les techniques que vous avez apprises dans ce laboratoire fournissent une base solide pour ce type d'exploration et d'analyse de données.
