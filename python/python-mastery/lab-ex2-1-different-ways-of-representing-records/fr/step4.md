# Comparaison de différentes structures de données

En Python, les structures de données sont utilisées pour organiser et stocker des données liées. Elles sont comme des conteneurs qui stockent différents types d'informations de manière structurée. Dans cette étape, nous allons comparer différentes structures de données et voir combien de mémoire elles utilisent.

Créons un nouveau fichier appelé `compare_structures.py` dans le répertoire `/home/labex/project`. Ce fichier contiendra le code pour lire des données à partir d'un fichier CSV et les stocker dans différentes structures de données.

```python
# compare_structures.py
import csv
import tracemalloc
from collections import namedtuple

# Define a named tuple for rides data
RideRecord = namedtuple('RideRecord', ['route', 'date', 'daytype', 'rides'])

# A named tuple is a lightweight class that allows you to access its fields by name.
# It's like a tuple, but with named attributes.

# Define a class with __slots__ for memory optimization
class SlottedRideRecord:
    __slots__ = ['route', 'date', 'daytype', 'rides']

    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

# A class with __slots__ is a memory - optimized class.
# It avoids using an instance dictionary, which saves memory.

# Define a regular class for rides data
class RegularRideRecord:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

# A regular class is an object - oriented way to represent data.
# It has named attributes and can have methods.

# Function to read data as tuples
def read_as_tuples(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)  # Skip headers
        for row in rows:
            record = (row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records

# This function reads data from a CSV file and stores it as tuples.
# Tuples are immutable sequences, and you access their elements by numeric index.

# Function to read data as dictionaries
def read_as_dicts(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # Get headers
        for row in rows:
            record = {
                'route': row[0],
                'date': row[1],
                'daytype': row[2],
                'rides': int(row[3])
            }
            records.append(record)
    return records

# This function reads data from a CSV file and stores it as dictionaries.
# Dictionaries use key - value pairs, so you can access elements by their names.

# Function to read data as named tuples
def read_as_named_tuples(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)  # Skip headers
        for row in rows:
            record = RideRecord(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records

# This function reads data from a CSV file and stores it as named tuples.
# Named tuples combine the efficiency of tuples with the readability of named access.

# Function to read data as regular class instances
def read_as_regular_classes(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)  # Skip headers
        for row in rows:
            record = RegularRideRecord(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records

# This function reads data from a CSV file and stores it as instances of a regular class.
# Regular classes allow you to add methods to your data.

# Function to read data as slotted class instances
def read_as_slotted_classes(filename):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)  # Skip headers
        for row in rows:
            record = SlottedRideRecord(row[0], row[1], row[2], int(row[3]))
            records.append(record)
    return records

# This function reads data from a CSV file and stores it as instances of a slotted class.
# Slotted classes are memory - optimized and still provide named access.

# Function to measure memory usage
def measure_memory(func, filename):
    tracemalloc.start()

    records = func(filename)

    current, peak = tracemalloc.get_traced_memory()

    # Demonstrate how to use each data structure
    first_record = records[0]
    if func.__name__ == 'read_as_tuples':
        route, date, daytype, rides = first_record
    elif func.__name__ == 'read_as_dicts':
        route = first_record['route']
        date = first_record['date']
        daytype = first_record['daytype']
        rides = first_record['rides']
    else:  # named tuples and classes
        route = first_record.route
        date = first_record.date
        daytype = first_record.daytype
        rides = first_record.rides

    print(f"Structure type: {func.__name__}")
    print(f"Record count: {len(records)}")
    print(f"Example access: Route={route}, Date={date}, Rides={rides}")
    print(f"Current memory: {current/1024/1024:.2f} MB")
    print(f"Peak memory: {peak/1024/1024:.2f} MB")
    print("-" * 50)

    tracemalloc.stop()

    return current

if __name__ == "__main__":
    filename = '/home/labex/project/ctabus.csv'

    # Run all memory tests
    print("Memory usage comparison for different data structures:\n")

    results = []
    for reader_func in [
        read_as_tuples,
        read_as_dicts,
        read_as_named_tuples,
        read_as_regular_classes,
        read_as_slotted_classes
    ]:
        memory = measure_memory(reader_func, filename)
        results.append((reader_func.__name__, memory))

    # Sort by memory usage (lowest first)
    results.sort(key=lambda x: x[1])

    print("\nRanking by memory efficiency (most efficient first):")
    for i, (name, memory) in enumerate(results, 1):
        print(f"{i}. {name}: {memory/1024/1024:.2f} MB")
```

Exécutez le script pour voir les résultats de la comparaison :

```bash
python3 /home/labex/project/compare_structures.py
```

La sortie affichera l'utilisation mémoire de chaque structure de données, ainsi qu'un classement de la plus à la moins efficace en termes de mémoire.

## Compréhension des différentes structures de données

1. **Tuples** :

   - Les tuples sont des séquences légères et immuables. Cela signifie qu'une fois que vous avez créé un tuple, vous ne pouvez pas modifier ses éléments.
   - Vous accédez aux éléments d'un tuple par leur index numérique, comme `record[0]`, `record[1]`, etc.
   - Ils sont très efficaces en termes de mémoire car ils ont une structure simple.
   - Cependant, ils peuvent être moins lisibles car vous devez vous souvenir de l'index de chaque élément.

2. **Dictionnaires** :

   - Les dictionnaires utilisent des paires clé - valeur, ce qui vous permet d'accéder aux éléments par leur nom.
   - Ils sont plus lisibles, par exemple, vous pouvez utiliser `record['route']`, `record['date']`, etc.
   - Ils ont une utilisation mémoire plus élevée en raison du surcoût de la table de hachage utilisée pour stocker les paires clé - valeur.
   - Ils sont flexibles car vous pouvez facilement ajouter ou supprimer des champs.

3. **Tuples nommés** :

   - Les tuples nommés combinent l'efficacité des tuples avec la capacité d'accéder aux éléments par nom.
   - Vous pouvez accéder aux éléments en utilisant la notation pointée, comme `record.route`, `record.date`, etc.
   - Ils sont immuables, tout comme les tuples ordinaires.
   - Ils sont plus efficaces en termes de mémoire que les dictionnaires.

4. **Classes ordinaires** :

   - Les classes ordinaires suivent une approche orientée objet et ont des attributs nommés.
   - Vous pouvez accéder aux attributs en utilisant la notation pointée, comme `record.route`, `record.date`, etc.
   - Vous pouvez ajouter des méthodes à une classe ordinaire pour définir un comportement.
   - Elles utilisent plus de mémoire car chaque instance a un dictionnaire d'instance pour stocker ses attributs.

5. **Classes avec `__slots__`** :
   - Les classes avec `__slots__` sont des classes optimisées en termes de mémoire. Elles évitent d'utiliser un dictionnaire d'instance, ce qui économise de la mémoire.
   - Elles offrent toujours un accès nommé aux attributs, comme `record.route`, `record.date`, etc.
   - Elles limitent l'ajout de nouveaux attributs après la création de l'objet.
   - Elles sont plus efficaces en termes de mémoire que les classes ordinaires.

## Quand utiliser chaque approche

- **Tuples** : Utilisez les tuples lorsque la mémoire est un facteur critique et que vous n'avez besoin que d'un accès indexé simple à vos données.
- **Dictionnaires** : Utilisez les dictionnaires lorsque vous avez besoin de flexibilité, par exemple, lorsque les champs de vos données peuvent varier.
- **Tuples nommés** : Utilisez les tuples nommés lorsque vous avez besoin à la fois de lisibilité et d'efficacité mémoire.
- **Classes ordinaires** : Utilisez les classes ordinaires lorsque vous avez besoin d'ajouter un comportement (méthodes) à vos données.
- **Classes avec `__slots__`** : Utilisez les classes avec `__slots__` lorsque vous avez besoin de comportement et de l'efficacité mémoire maximale.

En choisissant la bonne structure de données pour vos besoins, vous pouvez améliorer considérablement les performances et l'utilisation mémoire de vos programmes Python, en particulier lorsque vous travaillez avec de grands ensembles de données.
