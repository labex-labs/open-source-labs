# Vergleich verschiedener Datenstrukturen

In Python werden Datenstrukturen verwendet, um verwandte Daten zu organisieren und zu speichern. Sie sind wie Container, die verschiedene Arten von Informationen auf strukturierte Weise aufnehmen. In diesem Schritt vergleichen wir verschiedene Datenstrukturen und sehen, wie viel Speicher sie verbrauchen.

Erstellen wir eine neue Datei namens `compare_structures.py` im Verzeichnis `/home/labex/project`. Diese Datei enthält den Code, um Daten aus einer CSV-Datei zu lesen und in verschiedenen Datenstrukturen zu speichern.

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

Führen Sie das Skript aus, um die Vergleichsergebnisse zu sehen:

```bash
python3 /home/labex/project/compare_structures.py
```

Die Ausgabe zeigt den Speicherverbrauch für jede Datenstruktur sowie eine Rangliste von der speichereffizientesten bis zur am wenigsten speichereffizienten.

## Verständnis der verschiedenen Datenstrukturen

1. **Tupel**:

   - Tupel sind leichte und unveränderliche Sequenzen. Das bedeutet, dass Sie die Elemente eines Tupels nach seiner Erstellung nicht ändern können.
   - Sie greifen auf die Elemente eines Tupels über ihren numerischen Index zu, wie z. B. `record[0]`, `record[1]` usw.
   - Sie sind sehr speichereffizient, da sie eine einfache Struktur haben.
   - Allerdings können sie weniger lesbar sein, da Sie sich den Index jedes Elements merken müssen.

2. **Wörterbücher (Dictionaries)**:

   - Wörterbücher verwenden Schlüssel-Wert-Paare, was es Ihnen ermöglicht, auf die Elemente über ihre Namen zuzugreifen.
   - Sie sind lesbarer, z. B. können Sie `record['route']`, `record['date']` usw. verwenden.
   - Sie haben einen höheren Speicherverbrauch aufgrund des Hash-Tabellen-Overheads, der zum Speichern der Schlüssel-Wert-Paare verwendet wird.
   - Sie sind flexibel, da Sie Felder leicht hinzufügen oder entfernen können.

3. **Benannte Tupel (Named Tuples)**:

   - Benannte Tupel kombinieren die Effizienz von Tupeln mit der Möglichkeit, auf die Elemente über ihren Namen zuzugreifen.
   - Sie können auf die Elemente mit der Punktnotation zugreifen, wie z. B. `record.route`, `record.date` usw.
   - Sie sind unveränderlich, genau wie normale Tupel.
   - Sie sind speichereffizienter als Wörterbücher.

4. **Normale Klassen (Regular Classes)**:

   - Normale Klassen folgen einem objektorientierten Ansatz und haben benannte Attribute.
   - Sie können auf die Attribute mit der Punktnotation zugreifen, wie z. B. `record.route`, `record.date` usw.
   - Sie können Methoden zu einer normalen Klasse hinzufügen, um Verhalten zu definieren.
   - Sie verbrauchen mehr Speicher, da jede Instanz ein Instanz-Wörterbuch zum Speichern ihrer Attribute hat.

5. **Klassen mit `__slots__`**:
   - Klassen mit `__slots__` sind speichergerecht optimierte Klassen. Sie vermeiden die Verwendung eines Instanz-Wörterbuchs, was Speicher spart.
   - Sie bieten immer noch benannten Zugriff auf die Attribute, wie z. B. `record.route`, `record.date` usw.
   - Sie beschränken das Hinzufügen neuer Attribute nach der Erstellung des Objekts.
   - Sie sind speichereffizienter als normale Klassen.

## Wann welche Methode verwenden

- **Tupel**: Verwenden Sie Tupel, wenn Speicher ein kritischer Faktor ist und Sie nur einfachen indizierten Zugriff auf Ihre Daten benötigen.
- **Wörterbücher**: Verwenden Sie Wörterbücher, wenn Sie Flexibilität benötigen, z. B. wenn die Felder in Ihren Daten variieren können.
- **Benannte Tupel**: Verwenden Sie benannte Tupel, wenn Sie sowohl Lesbarkeit als auch Speichereffizienz benötigen.
- **Normale Klassen**: Verwenden Sie normale Klassen, wenn Sie Verhalten (Methoden) zu Ihren Daten hinzufügen müssen.
- **Klassen mit `__slots__`**: Verwenden Sie Klassen mit `__slots__`, wenn Sie Verhalten und maximale Speichereffizienz benötigen.

Durch die Wahl der richtigen Datenstruktur für Ihre Bedürfnisse können Sie die Leistung und den Speicherverbrauch Ihrer Python-Programme erheblich verbessern, insbesondere wenn Sie mit großen Datensätzen arbeiten.
