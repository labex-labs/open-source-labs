# Exploration de l'ensemble de données

Commençons notre parcours en examinant de près l'ensemble de données avec lequel nous allons travailler. Le fichier `ctabus.csv` est un fichier CSV (Comma-Separated Values, valeurs séparées par des virgules). Les fichiers CSV sont un moyen courant de stocker des données tabulaires, où chaque ligne représente une ligne du tableau et les valeurs au sein d'une ligne sont séparées par des virgules. Ce fichier particulier contient les données de fréquentation quotidienne du réseau de bus de la Chicago Transit Authority (CTA), couvrant la période du 1er janvier 2001 au 31 août 2013.

Pour comprendre la structure de ce fichier, nous allons d'abord jeter un coup d'œil à l'intérieur. Nous utiliserons Python pour lire le fichier et afficher quelques lignes. Ouvrez un terminal et exécutez le code Python suivant :

```python
f = open('/home/labex/project/ctabus.csv')
print(next(f))  # Read the header line
print(next(f))  # Read the first data line
print(next(f))  # Read the second data line
f.close()
```

Dans ce code, nous ouvrons d'abord le fichier à l'aide de la fonction `open` et l'attribuons à la variable `f`. La fonction `next` est utilisée pour lire la ligne suivante du fichier. Nous l'utilisons trois fois : la première fois pour lire la ligne d'en-tête, qui contient généralement les noms des colonnes de l'ensemble de données. La deuxième et la troisième fois, nous lisons respectivement la première et la deuxième ligne de données. Enfin, nous fermons le fichier à l'aide de la méthode `close` pour libérer les ressources système.

Vous devriez voir une sortie similaire à ceci :

```
route,date,daytype,rides

3,01/01/2001,U,7354

4,01/01/2001,U,9288
```

Cette sortie montre que le fichier a 4 colonnes de données. Analysons ce que chaque colonne représente :

1. `route` : Il s'agit du nom ou du numéro de la ligne de bus. C'est la première colonne (Colonne 0) de l'ensemble de données.
2. `date` : C'est une chaîne de caractères représentant une date au format MM/DD/YYYY. C'est la deuxième colonne (Colonne 1).
3. `daytype` : C'est un code indiquant le type de jour, qui est la troisième colonne (Colonne 2).
   - U = Dimanche/Jour férié
   - A = Samedi
   - W = Jour de semaine
4. `rides` : Cette colonne enregistre le nombre total de passagers sous forme d'entier. C'est la quatrième colonne (Colonne 3).

La colonne `rides` nous indique combien de personnes ont pris un bus sur une ligne spécifique à une date donnée. Par exemple, à partir de la sortie ci-dessus, nous pouvons voir que 7 354 personnes ont pris le bus numéro 3 le 1er janvier 2001.

Maintenant, trouvons combien de lignes il y a dans le fichier. Savoir le nombre de lignes nous donnera une idée de la taille de notre ensemble de données. Exécutez le code Python suivant :

```python
with open('/home/labex/project/ctabus.csv') as f:
    line_count = sum(1 for line in f)
    print(f"Total lines in the file: {line_count}")
```

Dans ce code, nous utilisons l'instruction `with` pour ouvrir le fichier. L'avantage d'utiliser `with` est qu'il prend automatiquement en charge la fermeture du fichier une fois que nous avons terminé. Nous utilisons ensuite une expression génératrice `(1 for line in f)` pour créer une séquence de 1, un pour chaque ligne du fichier. La fonction `sum` additionne tous ces 1, nous donnant le nombre total de lignes du fichier. Enfin, nous affichons le résultat.

Cela devrait afficher environ 577 564 lignes, ce qui signifie que nous avons affaire à un ensemble de données important. Cet ensemble de données volumineux nous fournira suffisamment de données pour analyser et tirer des informations.
