# Changement de votre orientation (vers les colonnes)

Vous pouvez souvent économiser beaucoup de mémoire si vous changez votre vision des données. Par exemple, qu'arrive-t-il si vous lisez toutes les données de bus dans des colonnes à l'aide de cette fonction?

```python
# readrides.py

...

def read_rides_as_columns(filename):
    '''
    Lire les données des trajets de bus dans 4 listes, représentant les colonnes
    '''
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Ignorer les en-têtes
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)
```

En théorie, cette fonction devrait économiser beaucoup de mémoire. Analysons-la avant de l'essayer.

Tout d'abord, le fichier de données contenait 577563 lignes de données où chaque ligne contenait quatre valeurs. Si chaque ligne est stockée sous forme de dictionnaire, alors ces dictionnaires ont une taille minimale de 240 octets.

```python
>>> nrows = 577563     # Nombre de lignes dans le fichier original
>>> nrows * 240
138615120
>>>
```

Donc, ce sont 138 Mo seulement pour les dictionnaires eux-mêmes. Cela ne comprend pas aucune des valeurs effectivement stockées dans les dictionnaires.

En passant aux colonnes, les données sont stockées dans 4 listes séparées.\
Chaque liste nécessite 8 octets par élément pour stocker un pointeur. Voici donc une estimation approximative des besoins en liste :

```python
>>> nrows * 4 * 8
18482016
>>>
```

Cela représente environ 18 Mo d'en-tête de liste. Donc, passer à une orientation colonne devrait économiser environ 120 Mo de mémoire seulement en éliminant toutes les informations supplémentaires qui doivent être stockées dans les dictionnaires.

Essayez d'utiliser cette fonction pour lire les données de bus et regardez l'utilisation de la mémoire.

```python
>>> import tracemalloc
>>> tracemalloc.start()
>>> columns = read_rides_as_columns('ctabus.csv')
>>> tracemalloc.get_traced_memory()
... regardez le résultat...
>>>
```

Le résultat reflète-t-il les économies de mémoire attendues de nos calculs approximatifs ci-dessus?
