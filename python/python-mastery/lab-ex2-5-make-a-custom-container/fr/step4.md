# Création d'une classe de conteneur personnalisée

Dans le traitement des données, l'approche orientée colonne est excellente pour économiser de la mémoire. Cependant, cela peut poser des problèmes lorsque votre code existant s'attend à ce que les données soient sous la forme d'une liste de dictionnaires. Pour résoudre ce problème, nous allons créer une classe de conteneur personnalisée. Cette classe présentera une interface orientée ligne, ce qui signifie qu'elle ressemblera et se comportera comme une liste de dictionnaires pour votre code. Mais en interne, elle stockera les données au format orienté colonne, nous aidant ainsi à économiser de la mémoire.

1. Tout d'abord, ouvrez le fichier `readrides.py` dans l'éditeur WebIDE. Nous allons ajouter une nouvelle classe à ce fichier. Cette classe sera la base de notre conteneur personnalisé.

```python
# Add this to readrides.py
from collections.abc import Sequence

class RideData(Sequence):
    def __init__(self):
        # Each value is a list with all of the values (a column)
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        # All lists assumed to have the same length
        return len(self.routes)

    def __getitem__(self, index):
        return {'route': self.routes[index],
                'date': self.dates[index],
                'daytype': self.daytypes[index],
                'rides': self.numrides[index]}

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])
```

Dans ce code, nous définissons une classe nommée `RideData` qui hérite de `Sequence`. La méthode `__init__` initialise quatre listes vides, chacune représentant une colonne de données. La méthode `__len__` renvoie la longueur du conteneur, qui est la même que la longueur de la liste `routes`. La méthode `__getitem__` nous permet d'accéder à un enregistrement spécifique par son index, en le renvoyant sous forme de dictionnaire. La méthode `append` ajoute un nouvel enregistrement au conteneur en ajoutant des valeurs à chaque liste de colonne.

2. Maintenant, nous avons besoin d'une fonction pour lire les données de trajets en bus dans notre conteneur personnalisé. Ajoutez la fonction suivante au fichier `readrides.py`.

```python
# Add this to readrides.py
def read_rides_as_dicts(filename):
    '''
    Read the bus ride data as a list of dicts, but use our custom container
    '''
    records = RideData()
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides
            }
            records.append(record)
    return records
```

Cette fonction crée une instance de la classe `RideData` et la remplit avec les données du fichier CSV. Elle lit chaque ligne du fichier, extrait les informations pertinentes, crée un dictionnaire pour chaque enregistrement, puis l'ajoute au conteneur `RideData`. L'important est qu'elle conserve la même interface qu'une liste de dictionnaires, mais stocke les données en colonnes en interne.

3. Testons notre conteneur personnalisé dans le shell Python. Cela nous aidera à vérifier qu'il fonctionne comme prévu.

```python
import readrides

# Read the data using our custom container
rows = readrides.read_rides_as_dicts('ctabus.csv')

# Check the type of the returned object
type(rows)  # Should be readrides.RideData

# Check the length
len(rows)   # Should be 577563

# Access individual records
rows[0]     # Should return a dictionary for the first record
rows[1]     # Should return a dictionary for the second record
rows[2]     # Should return a dictionary for the third record
```

Notre conteneur personnalisé implémente avec succès l'interface `Sequence`, ce qui signifie qu'il se comporte comme une liste. Vous pouvez utiliser la fonction `len()` pour obtenir le nombre d'enregistrements dans le conteneur, et vous pouvez utiliser l'indexation pour accéder à des enregistrements individuels. Chaque enregistrement semble être un dictionnaire, même si les données sont stockées en colonnes en interne. C'est excellent car le code existant qui s'attend à une liste de dictionnaires continuera de fonctionner avec notre conteneur personnalisé sans aucune modification.

4. Enfin, mesurons l'utilisation de mémoire de notre conteneur personnalisé. Cela nous montrera combien de mémoire nous économisons par rapport à une liste de dictionnaires.

```python
import tracemalloc

tracemalloc.start()
rows = readrides.read_rides_as_dicts('ctabus.csv')
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current/1024/1024:.2f} MB")
print(f"Peak memory usage: {peak/1024/1024:.2f} MB")
tracemalloc.stop()
```

Lorsque vous exécutez ce code, vous devriez voir que l'utilisation de mémoire est similaire à celle de l'approche orientée colonne, ce qui est beaucoup moins que ce qu'une liste de dictionnaires utiliserait. Cela démontre l'avantage de notre conteneur personnalisé en termes d'efficacité mémoire.
