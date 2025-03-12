# Spaltenorientierte Datenspeicherung

Bisher haben wir CSV-Daten als Liste von Zeilenwörterbüchern gespeichert. Das bedeutet, dass jede Zeile in der CSV-Datei als ein Wörterbuch dargestellt wird, wobei die Schlüssel die Spaltenüberschriften und die Werte die entsprechenden Daten in dieser Zeile sind. Bei der Arbeit mit großen Datensätzen kann diese Methode jedoch ineffizient sein. Die Speicherung von Daten in einem spaltenorientierten Format kann eine bessere Wahl sein. Bei einem spaltenorientierten Ansatz wird die Daten jeder Spalte in einer separaten Liste gespeichert. Dies kann den Speicherverbrauch erheblich reduzieren, da ähnliche Datentypen zusammengefasst werden, und es kann auch die Leistung für bestimmte Operationen wie die Aggregation von Daten nach Spalten verbessern.

## Erstellen eines spaltenorientierten Datenlesers

Jetzt werden wir eine neue Datei erstellen, die uns helfen wird, CSV-Daten in einem spaltenorientierten Format zu lesen. Erstellen Sie eine neue Datei mit dem Namen `colreader.py` im Projektverzeichnis mit dem folgenden Code:

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

Dieser Code macht zwei wichtige Dinge:

1. Er definiert eine `DataCollection`-Klasse. Diese Klasse speichert Daten in Spalten, ermöglicht es uns aber, auf die Daten zuzugreifen, als ob es sich um eine Liste von Zeilenwörterbüchern handeln würde. Dies ist nützlich, da es einen vertrauten Weg bietet, mit den Daten zu arbeiten.
2. Er definiert eine `read_csv_as_columns`-Funktion. Diese Funktion liest CSV-Daten aus einer Datei und speichert sie in einer spaltenorientierten Struktur. Sie konvertiert auch jedes Feld in der CSV-Datei gemäß den von uns angegebenen Typen.

## Testen des spaltenorientierten Lesers

Lassen Sie uns unseren spaltenorientierten Leser mit den CTA-Bus-Daten testen. Zunächst öffnen Sie einen Python-Interpreter. Sie können dies tun, indem Sie den folgenden Befehl in Ihrem Terminal ausführen:

```bash
python3
```

Sobald der Python-Interpreter geöffnet ist, führen Sie den folgenden Code aus:

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

Die Ausgabe sollte so aussehen:

```
Number of rows: 577563
First 3 rows:
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
{'route': '6', 'date': '01/01/2001', 'daytype': 'U', 'rides': 6048}
Current memory usage: 38.67 MB
Peak memory usage: 103.42 MB
```

Jetzt vergleichen wir dies mit unserem vorherigen zeilenorientierten Ansatz. Führen Sie den folgenden Code im gleichen Python-Interpreter aus:

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

Die Ausgabe sollte in etwa so aussehen:

```
Current memory usage (row-oriented): 170.23 MB
Peak memory usage (row-oriented): 190.05 MB
```

Wie Sie sehen können, verwendet der spaltenorientierte Ansatz erheblich weniger Speicher!

Lassen Sie uns auch testen, ob wir die Daten weiterhin wie zuvor analysieren können. Führen Sie den folgenden Code aus:

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

Die Ausgabe sollte sein:

```
Number of unique routes: 181
Top 5 routes by total rides:
Route 9: 158,545,826 rides
Route 49: 129,872,910 rides
Route 77: 120,086,065 rides
Route 79: 109,348,708 rides
Route 4: 91,405,538 rides
```

Schließlich beenden Sie den Python-Interpreter, indem Sie den folgenden Befehl ausführen:

```python
exit()
```

Wir können sehen, dass der spaltenorientierte Ansatz nicht nur Speicher spart, sondern auch die gleichen Analysen wie zuvor ermöglicht. Dies zeigt, wie unterschiedliche Datenspeicherstrategien einen erheblichen Einfluss auf die Leistung haben können, während sie weiterhin die gleiche Schnittstelle für die Arbeit mit den Daten bieten.
