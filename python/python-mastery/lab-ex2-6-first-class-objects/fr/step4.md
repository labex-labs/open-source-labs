# Stockage de données orienté colonnes

Jusqu'à présent, nous avons stocké les données CSV sous forme de liste de dictionnaires de lignes. Cela signifie que chaque ligne du fichier CSV est représentée sous forme de dictionnaire, où les clés sont les en-têtes de colonne et les valeurs sont les données correspondantes de cette ligne. Cependant, lorsqu'on travaille avec de grands ensembles de données, cette méthode peut être inefficace. Stocker les données dans un format orienté colonnes peut être un meilleur choix. Dans une approche orientée colonnes, les données de chaque colonne sont stockées dans une liste distincte. Cela peut réduire considérablement l'utilisation de la mémoire car les types de données similaires sont regroupés, et cela peut également améliorer les performances pour certaines opérations telles que l'agrégation de données par colonne.

## Création d'un lecteur de données orienté colonnes

Maintenant, nous allons créer un nouveau fichier qui nous aidera à lire les données CSV dans un format orienté colonnes. Créez un nouveau fichier nommé `colreader.py` dans le répertoire du projet avec le code suivant :

```python
import csv

class DataCollection:
    def __init__(self, headers, columns):
        """
        Initialize a column-oriented data collection.

        Parameters:
        headers (list): Column header names
        columns (dict): Dictionary mapping header names to column data lists
        """
        self.headers = headers
        self.columns = columns
        self._length = len(columns[headers[0]]) if headers else 0

    def __len__(self):
        """Return the number of rows in the collection."""
        return self._length

    def __getitem__(self, index):
        """
        Get a row by index, presented as a dictionary.

        Parameters:
        index (int): Row index

        Returns:
        dict: Dictionary representing the row at the given index
        """
        if isinstance(index, int):
            if index < 0 or index >= self._length:
                raise IndexError("Index out of range")

            return {header: self.columns[header][index] for header in self.headers}
        else:
            raise TypeError("Index must be an integer")

def read_csv_as_columns(filename, types):
    """
    Read a CSV file into a column-oriented data structure, converting each field
    according to the types provided.

    Parameters:
    filename (str): Name of the CSV file to read
    types (list): List of type conversion functions for each column

    Returns:
    DataCollection: Column-oriented data collection representing the CSV data
    """
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)  # Get the column headers

        # Initialize columns
        columns = {header: [] for header in headers}

        # Read data into columns
        for row in rows:
            # Convert values according to the specified types
            converted_values = [func(val) for func, val in zip(types, row)]

            # Add each value to its corresponding column
            for header, value in zip(headers, converted_values):
                columns[header].append(value)

    return DataCollection(headers, columns)
```

Ce code fait deux choses importantes :

1. Il définit une classe `DataCollection`. Cette classe stocke les données par colonnes, mais elle nous permet d'accéder aux données comme si c'était une liste de dictionnaires de lignes. Cela est utile car il offre un moyen familier de travailler avec les données.
2. Il définit une fonction `read_csv_as_columns`. Cette fonction lit les données CSV à partir d'un fichier et les stocke dans une structure orientée colonnes. Elle convertit également chaque champ du fichier CSV selon les types que nous fournissons.

## Test du lecteur de données orienté colonnes

Testons notre lecteur de données orienté colonnes en utilisant les données des bus CTA. Tout d'abord, ouvrez un interpréteur Python. Vous pouvez le faire en exécutant la commande suivante dans votre terminal :

```bash
python3
```

Une fois l'interpréteur Python ouvert, exécutez le code suivant :

```python
import colreader
import tracemalloc
from sys import intern

# Start memory tracking
tracemalloc.start()

# Read data into column-oriented structure with string interning
data = colreader.read_csv_as_columns('ctabus.csv', [intern, intern, intern, int])

# Check that we can access the data like a list of dictionaries
print(f"Number of rows: {len(data)}")
print("First 3 rows:")
for i in range(3):
    print(data[i])

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")
```

La sortie devrait ressembler à ceci :

```
Number of rows: 577563
First 3 rows:
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
{'route': '6', 'date': '01/01/2001', 'daytype': 'U', 'rides': 6048}
Current memory usage: 38.67 MB
Peak memory usage: 103.42 MB
```

Maintenant, comparons cela avec notre approche précédente orientée lignes. Exécutez le code suivant dans le même interpréteur Python :

```python
import reader
import tracemalloc
from sys import intern

# Reset memory tracking
tracemalloc.reset_peak()

# Read data into row-oriented structure with string interning
rows = reader.read_csv_as_dicts('ctabus.csv', [intern, intern, intern, int])

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage (row-oriented): {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage (row-oriented): {peak / 1024 / 1024:.2f} MB")
```

La sortie devrait être quelque chose comme ceci :

```
Current memory usage (row-oriented): 170.23 MB
Peak memory usage (row-oriented): 190.05 MB
```

Comme vous pouvez le voir, l'approche orientée colonnes utilise considérablement moins de mémoire !

Testons également que nous pouvons toujours analyser les données comme avant. Exécutez le code suivant :

```python
# Find all unique routes in the column-oriented data
routes = {row['route'] for row in data}
print(f"Number of unique routes: {len(routes)}")

# Count rides per route (first 5)
from collections import defaultdict
route_rides = defaultdict(int)
for row in data:
    route_rides[row['route']] += row['rides']

# Show the top 5 routes by total rides
top_routes = sorted(route_rides.items(), key=lambda x: x[1], reverse=True)[:5]
print("Top 5 routes by total rides:")
for route, rides in top_routes:
    print(f"Route {route}: {rides:,} rides")
```

La sortie devrait être :

```
Number of unique routes: 181
Top 5 routes by total rides:
Route 9: 158,545,826 rides
Route 49: 129,872,910 rides
Route 77: 120,086,065 rides
Route 79: 109,348,708 rides
Route 4: 91,405,538 rides
```

Enfin, quittez l'interpréteur Python en exécutant la commande suivante :

```python
exit()
```

Nous pouvons voir que l'approche orientée colonnes non seulement économise de la mémoire, mais nous permet également d'effectuer les mêmes analyses que précédemment. Cela montre comment différentes stratégies de stockage de données peuvent avoir un impact significatif sur les performances tout en offrant la même interface pour travailler avec les données.
