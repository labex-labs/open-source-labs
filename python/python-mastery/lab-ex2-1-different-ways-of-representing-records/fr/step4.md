# Utilisation de la mémoire pour les autres structures de données

Python propose de nombreux choix différents pour représenter des structures de données. Par exemple :

```python
# Un tuple
row = (route, date, daytype, rides)

# Un dictionnaire
row = {
    'route': route,
    'date': date,
    'daytype': daytype,
    'rides': rides,
}

# Une classe
class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

# Un tuple nommé
from collections import namedtuple
Row = namedtuple('Row', ['route', 'date', 'daytype', 'rides'])

# Une classe avec __slots__
class Row:
    __slots__ = ['route', 'date', 'daytype', 'rides']
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides
```

Votre tâche est la suivante : Créez différentes versions de la fonction `read_rides()` qui utilisent chacune de ces structures de données pour représenter une seule ligne de données. Ensuite, déterminez l'utilisation de mémoire résultante de chaque option. Trouvez laquelle des approches offre le stockage le plus efficace si vous travailliez avec beaucoup de données d'un coup.
