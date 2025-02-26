# Une liste de tuples

En pratique, vous pouvez lire les données dans une liste et convertir chaque ligne en une autre structure de données. Voici un programme `readrides.py` qui lit tout le fichier dans une liste de tuples en utilisant le module `csv` :

```python
# readrides.py

import csv

def read_rides_as_tuples(filename):
    '''
    Lit les données de trajet en bus sous forme d'une liste de tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Ignore les en-têtes
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    rows = read_rides_as_tuples('/home/labex/project/ctabus.csv')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
```

Exécutez ce programme en utilisant `python3 -i readrides.py` et examinez le contenu résultant de `rows`. Vous devriez obtenir une liste de tuples comme ceci :

```python
>>> len(rows)
577563
>>> rows[0]
('3', '01/01/2001', 'U', 7354)
>>> rows[1]
('4', '01/01/2001', 'U', 9288)
```

Examinez l'utilisation de mémoire résultante. Elle devrait être considérablement plus élevée que dans l'étape 2.
