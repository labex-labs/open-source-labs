# Création d'un conteneur personnalisé - Le grand leurre

Stockage des données dans des colonnes offre une économie de mémoire bien meilleure, mais les données sont maintenant assez étranges à manipuler. En fait, aucun de nos anciens codes d'analyse de l'Exercice 2.2 ne peut fonctionner avec des colonnes. La raison pour laquelle tout est cassé est que vous avez brisé l'abstraction des données utilisée dans les exercices précédents - à savoir l'hypothèse selon laquelle les données sont stockées sous forme d'une liste de dictionnaires.

Cela peut être corrigé si vous êtes prêt à créer un objet de conteneur personnalisé qui "simule" cela. Faisons-le.

Le code d'analyse précédent suppose que les données sont stockées dans une séquence d'enregistrements. Chaque enregistrement est représenté sous forme d'un dictionnaire. Commençons par créer une nouvelle classe "Sequence". Dans cette classe, nous stockons les quatre colonnes de données qui étaient utilisées dans la fonction `read_rides_as_columns()`.

```python
# readrides.py

from collections.abc import Sequence

...

class RideData(Sequence):
    def __init__(self):
        self.routes = []      # Colonnes
        self.dates = []
        self.daytypes = []
        self.numrides = []
```

Essayez de créer une instance de `RideData`. Vous constaterez qu'elle échoue avec un message d'erreur comme celui-ci :

```python
>>> records = RideData()
Traceback (most recent call last):
...
TypeError: Can't instantiate abstract class RideData with abstract methods __getitem__, __len__
>>>
```

Lisez attentivement le message d'erreur. Il nous indique ce que nous devons implémenter. Ajoutons une méthode `__len__()` et `__getitem__()`. Dans la méthode `__getitem__()`, nous allons créer un dictionnaire. De plus, nous allons créer une méthode `append()` qui prend un dictionnaire et le décompose en 4 opérations `append()` distinctes.

```python
# readrides.py
...

class RideData(collections.Sequence):
    def __init__(self):
        # Chaque valeur est une liste avec toutes les valeurs (une colonne)
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        # Toutes les listes sont supposées avoir la même longueur
        return len(self.routes)

    def __getitem__(self, index):
        return { 'route': self.routes[index],
                 'date': self.dates[index],
                 'daytype': self.daytypes[index],
                 'rides': self.numrides[index] }

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])
```

Si vous avez fait cela correctement, vous devriez être en mesure d'insérer cet objet dans la fonction `read_rides_as_dicts()` précédemment écrite. Cela ne nécessite que de changer une seule ligne de code :

```python
# readrides.py
...

def read_rides_as_dicts(filename):
    '''
    Lire les données des trajets de bus sous forme d'une liste de dictionnaires
    '''
    records = RideData()      # <--- CHANGEZ CE CI
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Ignorer les en-têtes
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides' : rides
                }
            records.append(record)
    return records
```

Si vous avez fait cela correctement, le code ancien devrait fonctionner exactement comme avant. Par exemple :

```python
>>> rows = readrides.read_rides_as_dicts('ctabus.csv')
>>> rows
<readrides.RideData object at 0x10f5054a8>
>>> len(rows)
577563
>>> rows[0]
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
>>> rows[1]
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
>>> rows[2]
{'route': '6', 'date': '01/01/2001', 'daytype': 'U', 'rides': 6048}
>>>
```

Exécutez votre ancien code CTA de l'Exercice 2.2. Il devrait fonctionner sans modification, mais utiliser beaucoup moins de mémoire.
