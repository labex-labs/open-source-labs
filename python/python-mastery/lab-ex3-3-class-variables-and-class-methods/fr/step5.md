# Généralisation

Une caractéristique utile des méthodes de classe est qu'on peut les utiliser pour mettre une interface de création d'instances très uniforme sur une grande variété de classes et écrire des fonctions utilitaires générales qui les utilisent.

Plus tôt, vous avez créé un fichier `reader.py` qui avait quelques fonctions pour lire des données CSV. Ajoutez la fonction `read_csv_as_instances()` suivante au fichier qui accepte une classe en entrée et utilise la méthode `from_row()` de la classe pour créer une liste d'instances :

```python
# reader.py
...

def read_csv_as_instances(filename, cls):
    '''
    Lit un fichier CSV dans une liste d'instances
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records
```

Supprimez la fonction `read_portfolio()` - vous n'en avez plus besoin. Si vous voulez lire une liste d'objets `Stock`, faites ceci :

```python
>>> # Lire un portefeuille d'instances de Stock
>>> from reader import read_csv_as_instances
>>> from stock import Stock
>>> portfolio = read_csv_as_instances('portfolio.csv', Stock)
>>> portfolio
[<__main__.Stock object at 0x100674748>,
<__main__.Stock object at 0x1006746d8>,
<__main__.Stock object at 0x1006747b8>,
<__main__.Stock object at 0x100674828>,
<__main__.Stock object at 0x100674898>,
<__main__.Stock object at 0x100674908>,
<__main__.Stock object at 0x100674978>]
>>>
```

Voici un autre exemple de la manière dont vous pourriez utiliser `read_csv_as_instances()` avec une classe complètement différente :

```python
>>> class Row:
         def __init__(self, route, date, daytype, numrides):
             self.route = route
             self.date = date
             self.daytype = daytype
             self.numrides = numrides
         @classmethod
         def from_row(cls, row):
             return cls(row[0], row[1], row[2], int(row[3]))

>>> rides = read_csv_as_instances('ctabus.csv', Row)
>>> len(rides)
577563
>>>
```

**Discussion**

Ce laboratoire illustre les deux utilisations les plus courantes des variables de classe et des méthodes de classe. Les variables de classe sont souvent utilisées pour stocker un paramètre global (par exemple, un paramètre de configuration) qui est partagé par toutes les instances. Parfois, les sous-classes hériteront de la classe de base et modifieront la configuration pour changer le comportement.

Les méthodes de classe sont le plus souvent utilisées pour implémenter des constructeurs alternatifs comme montré. Un moyen courant de repérer de telles méthodes de classe est de chercher le mot "from" dans le nom. Par exemple, voici un exemple sur les dictionnaires intégrés :

```python
>>> d = dict.fromkeys(['a','b','c'], 0)     # méthode de classe
>>> d
{'a': 0, 'c': 0, 'b': 0}
>>>
```
