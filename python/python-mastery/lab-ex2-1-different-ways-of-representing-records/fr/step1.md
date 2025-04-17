# Exploration du jeu de données

Commençons notre exploration en examinant de près le jeu de données (dataset) avec lequel nous allons travailler. Le fichier `ctabus.csv` est un fichier CSV (Comma-Separated Values, valeurs séparées par des virgules). Les fichiers CSV sont une méthode courante pour stocker des données tabulaires, où chaque ligne représente une rangée, et les valeurs à l'intérieur d'une rangée sont séparées par des virgules. Ce fichier particulier contient des données quotidiennes sur l'achalandage du réseau de bus de la Chicago Transit Authority (CTA), couvrant la période du 1er janvier 2001 au 31 août 2013.

Dézippez le fichier et supprimez le fichier zip :

```bash
cd /home/labex/project
unzip ctabus.csv.zip
rm ctabus.csv.zip
```

Pour comprendre la structure de ce fichier, nous allons d'abord y jeter un coup d'œil. Nous utiliserons Python pour lire le fichier et afficher quelques lignes. Ouvrez un terminal et exécutez le code Python suivant :

```python
f = open('/home/labex/project/ctabus.csv')
print(next(f))  # Lit la ligne d'en-tête (header)
print(next(f))  # Lit la première ligne de données
print(next(f))  # Lit la deuxième ligne de données
f.close()
```

Dans ce code, nous ouvrons d'abord le fichier en utilisant la fonction `open` et l'assignons à la variable `f`. La fonction `next` est utilisée pour lire la ligne suivante du fichier. Nous l'utilisons trois fois : la première fois pour lire la ligne d'en-tête (header), qui contient généralement les noms des colonnes dans le jeu de données (dataset). La deuxième et la troisième fois, nous lisons respectivement la première et la deuxième ligne de données. Enfin, nous fermons le fichier en utilisant la méthode `close` pour libérer les ressources du système.

Vous devriez voir une sortie similaire à ceci :

```
route,date,daytype,rides

3,01/01/2001,U,7354

4,01/01/2001,U,9288
```

Cette sortie montre que le fichier a 4 colonnes de données. Décomposons ce que chaque colonne représente :

1. `route` : Il s'agit du nom ou du numéro de la ligne de bus. C'est la première colonne (Colonne 0) dans le jeu de données (dataset).
2. `date` : C'est une chaîne de caractères (string) de date au format MM/JJ/AAAA. C'est la deuxième colonne (Colonne 1).
3. `daytype` : C'est un code de type de jour, qui est la troisième colonne (Colonne 2).
   - U = Dimanche/Jour férié (Sunday/Holiday)
   - A = Samedi (Saturday)
   - W = Jour de semaine (Weekday)
4. `rides` : Cette colonne enregistre le nombre total de passagers sous forme d'entier (integer). C'est la quatrième colonne (Colonne 3).

La colonne `rides` nous indique combien de personnes sont montées dans un bus sur une ligne spécifique un jour donné. Par exemple, d'après la sortie ci-dessus, nous pouvons voir que 7 354 personnes ont pris le bus numéro 3 le 1er janvier 2001.

Maintenant, découvrons combien de lignes contient le fichier. Connaître le nombre de lignes nous donnera une idée de la taille de notre jeu de données (dataset). Exécutez le code Python suivant :

```python
with open('/home/labex/project/ctabus.csv') as f:
    line_count = sum(1 for line in f)
    print(f"Total lines in the file: {line_count}")
```

Dans ce code, nous utilisons l'instruction `with` pour ouvrir le fichier. L'avantage d'utiliser `with` est qu'il se charge automatiquement de fermer le fichier lorsque nous avons terminé de l'utiliser. Nous utilisons ensuite une expression génératrice `(1 for line in f)` pour créer une séquence de 1, un pour chaque ligne du fichier. La fonction `sum` additionne tous ces 1, ce qui nous donne le nombre total de lignes dans le fichier. Enfin, nous affichons le résultat.

Cela devrait afficher environ 577 564 lignes, ce qui signifie que nous avons affaire à un jeu de données (dataset) important. Ce grand jeu de données (dataset) nous fournira de nombreuses données à analyser et à partir desquelles tirer des conclusions.
