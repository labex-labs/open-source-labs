# Erstellung eines universellen CSV-Readers

In diesem letzten Schritt werden wir eine universelle Funktion erstellen. Diese Funktion kann CSV-Dateien lesen und Objekte jeder Klasse erstellen, die die `from_row()`-Klassenmethode implementiert hat. Dies zeigt uns die Stärke der Verwendung von Klassenmethoden als einheitliche Schnittstelle. Eine einheitliche Schnittstelle bedeutet, dass verschiedene Klassen auf die gleiche Weise verwendet werden können, was unseren Code flexibler und leichter zu verwalten macht.

## Änderung der read_portfolio()-Funktion

Zuerst werden wir die `read_portfolio()`-Funktion in der Datei `stock.py` aktualisieren. Wir verwenden unsere neue `from_row()`-Klassenmethode. Öffnen Sie die Datei `stock.py` und ändern Sie die `read_portfolio()`-Funktion wie folgt:

```python
def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of Stock instances
    '''
    import csv
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skip header
        for row in rows:
            portfolio.append(Stock.from_row(row))
    return portfolio
```

Diese neue Version der Funktion ist einfacher. Sie übergibt die Verantwortung für die Typkonvertierung an die `Stock`-Klasse, wo sie tatsächlich hingehört. Typkonvertierung bedeutet, die Daten von einem Typ in einen anderen zu ändern, wie z. B. einen String in eine Ganzzahl umzuwandeln. Dadurch machen wir unseren Code besser organisiert und leichter zu verstehen.

## Erstellung eines universellen CSV-Readers

Jetzt werden wir in der Datei `reader.py` eine allgemeinere Funktion erstellen. Diese Funktion kann CSV-Daten lesen und Instanzen jeder Klasse erstellen, die eine `from_row()`-Klassenmethode hat.

Öffnen Sie die Datei `reader.py` und fügen Sie die folgende Funktion hinzu:

```python
def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances of the given class.

    Args:
        filename: Name of the CSV file
        cls: Class to instantiate (must have from_row class method)

    Returns:
        List of class instances
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skip header
        for row in rows:
            records.append(cls.from_row(row))
    return records
```

Diese Funktion nimmt zwei Eingaben entgegen: einen Dateinamen und eine Klasse. Sie gibt dann eine Liste von Instanzen dieser Klasse zurück, die aus den Daten in der CSV-Datei erstellt wurden. Dies ist sehr nützlich, da wir es mit verschiedenen Klassen verwenden können, solange sie die `from_row()`-Methode haben.

## Testen des universellen CSV-Readers

Erstellen wir eine Testdatei, um zu sehen, wie unser universeller Reader funktioniert. Erstellen Sie eine Datei namens `test_csv_reader.py` mit folgendem Inhalt:

```python
# test_csv_reader.py
from reader import read_csv_as_instances
from stock import Stock
from decimal_stock import DStock

# Read portfolio as Stock instances
portfolio = read_csv_as_instances('portfolio.csv', Stock)
print(f"Portfolio contains {len(portfolio)} stocks")
print(f"First stock: {portfolio[0].name}, {portfolio[0].shares} shares at ${portfolio[0].price}")

# Read portfolio as DStock instances (with Decimal prices)
decimal_portfolio = read_csv_as_instances('portfolio.csv', DStock)
print(f"\nDecimal portfolio contains {len(decimal_portfolio)} stocks")
print(f"First stock: {decimal_portfolio[0].name}, {decimal_portfolio[0].shares} shares at ${decimal_portfolio[0].price}")

# Define a new class for reading the bus data
class BusRide:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

    @classmethod
    def from_row(cls, row):
        return cls(row[0], row[1], row[2], int(row[3]))

# Read some bus data (just the first 5 records for brevity)
print("\nReading bus data...")
import csv
with open('ctabus.csv') as f:
    rows = csv.reader(f)
    headers = next(rows)  # Skip header
    bus_rides = []
    for i, row in enumerate(rows):
        if i >= 5:  # Only read 5 records for the example
            break
        bus_rides.append(BusRide.from_row(row))

# Display the bus data
for ride in bus_rides:
    print(f"Route: {ride.route}, Date: {ride.date}, Type: {ride.daytype}, Rides: {ride.rides}")
```

Führen Sie diese Datei aus, um die Ergebnisse zu sehen. Öffnen Sie Ihr Terminal und verwenden Sie die folgenden Befehle:

```bash
cd ~/project
python test_csv_reader.py
```

Sie sollten eine Ausgabe sehen, die zeigt, dass die Portfolio-Daten sowohl als `Stock`- als auch als `DStock`-Instanzen geladen wurden, und die Buslinien-Daten als `BusRide`-Instanzen geladen wurden. Dies beweist, dass unser universeller Reader mit verschiedenen Klassen funktioniert.

## Wichtige Vorteile dieses Ansatzes

Dieser Ansatz zeigt mehrere mächtige Konzepte:

1. **Trennung von Anliegen**: Das Lesen von Daten ist von der Erstellung von Objekten getrennt. Dies bedeutet, dass der Code zum Lesen der CSV-Datei nicht mit dem Code zur Erstellung von Objekten vermischt ist. Es macht den Code leichter zu verstehen und zu warten.
2. **Polymorphismus**: Der gleiche Code kann mit verschiedenen Klassen arbeiten, die die gleiche Schnittstelle folgen. In unserem Fall kann unser universeller Reader jede Klasse verwenden, solange sie die `from_row()`-Methode hat.
3. **Flexibilität**: Wir können leicht ändern, wie Daten konvertiert werden, indem wir verschiedene Klassen verwenden. Beispielsweise können wir `Stock` oder `DStock` verwenden, um die Portfolio-Daten unterschiedlich zu verarbeiten.
4. **Erweiterbarkeit**: Wir können neue Klassen hinzufügen, die mit unserem Reader funktionieren, ohne den Reader-Code zu ändern. Dies macht unseren Code zukunftssicherer.

Dies ist ein gängiges Muster in Python, das den Code modularer, wiederverwendbarer und wartbarer macht.

## Abschließende Anmerkungen zu Klassenmethoden

Klassenmethoden werden in Python oft als alternative Konstruktoren verwendet. Man kann sie normalerweise daran erkennen, dass ihre Namen oft das Wort "from" enthalten. Beispielsweise:

```python
# Some examples from Python's built-in types
dict.fromkeys(['a', 'b', 'c'], 0)  # Create a dict with default values
datetime.datetime.fromtimestamp(1627776000)  # Create datetime from timestamp
int.from_bytes(b'\x00\x01', byteorder='big')  # Create int from bytes
```

Indem Sie dieser Konvention folgen, machen Sie Ihren Code lesbarer und konsistenter mit Python's eingebauten Bibliotheken. Dies hilft anderen Entwicklern, Ihren Code leichter zu verstehen.
