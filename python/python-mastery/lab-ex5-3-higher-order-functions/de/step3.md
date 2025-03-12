# Refactoring bestehender Funktionen

Jetzt haben wir eine höhere Funktion (Higher-Order Function) namens `convert_csv()` erstellt. Höhere Funktionen sind Funktionen, die andere Funktionen als Argumente nehmen oder Funktionen als Ergebnisse zurückgeben können. Sie sind ein mächtiges Konzept in Python, das uns helfen kann, modulareren und wiederverwendbaren Code zu schreiben. In diesem Abschnitt werden wir diese höhere Funktion nutzen, um die ursprünglichen Funktionen `csv_as_dicts()` und `csv_as_instances()` zu refaktorisieren. Refactoring ist der Prozess, bestehenden Code zu strukturieren, ohne sein externes Verhalten zu ändern, um seine interne Struktur zu verbessern, wie z. B. die Eliminierung von Code-Duplizierung.

Beginnen wir damit, die Datei `reader.py` im WebIDE zu öffnen. Wir werden die Funktionen wie folgt aktualisieren:

1. Zunächst ersetzen wir die Funktion `csv_as_dicts()`. Diese Funktion wird verwendet, um Zeilen von CSV-Daten in eine Liste von Dictionaries umzuwandeln. Hier ist der neue Code:

```python
def csv_as_dicts(lines, types, *, headers=None):
    '''
    Convert lines of CSV data into a list of dictionaries
    '''
    def dict_converter(headers, row):
        return {name: func(val) for name, func, val in zip(headers, types, row)}

    return convert_csv(lines, dict_converter, headers=headers)
```

In diesem Code definieren wir eine innere Funktion `dict_converter`, die `headers` und `row` als Argumente nimmt. Sie verwendet eine Dictionary-Comprehension, um ein Dictionary zu erstellen, bei dem die Schlüssel die Spaltenüberschriften sind und die Werte das Ergebnis der Anwendung der entsprechenden Typkonvertierungsfunktion auf die Werte in der Zeile sind. Dann rufen wir die Funktion `convert_csv()` mit der Funktion `dict_converter` als Argument auf.

2. Als Nächstes ersetzen wir die Funktion `csv_as_instances()`. Diese Funktion wird verwendet, um Zeilen von CSV-Daten in eine Liste von Instanzen einer gegebenen Klasse umzuwandeln. Hier ist der neue Code:

```python
def csv_as_instances(lines, cls, *, headers=None):
    '''
    Convert lines of CSV data into a list of instances
    '''
    def instance_converter(headers, row):
        return cls.from_row(row)

    return convert_csv(lines, instance_converter, headers=headers)
```

In diesem Code definieren wir eine innere Funktion `instance_converter`, die `headers` und `row` als Argumente nimmt. Sie ruft die Klassenmethode `from_row` der gegebenen Klasse `cls` auf, um eine Instanz aus der Zeile zu erstellen. Dann rufen wir die Funktion `convert_csv()` mit der Funktion `instance_converter` als Argument auf.

Nachdem wir diese Funktionen refaktoriert haben, müssen wir sie testen, um sicherzustellen, dass sie weiterhin wie erwartet funktionieren. Dazu führen wir die folgenden Befehle in einer Python-Shell aus:

```bash
cd ~/project
python3 -i reader.py
```

Der Befehl `cd ~/project` wechselt das aktuelle Arbeitsverzeichnis in das `project`-Verzeichnis. Der Befehl `python3 -i reader.py` führt die Datei `reader.py` im interaktiven Modus aus, was bedeutet, dass wir weiterhin Python-Code ausführen können, nachdem die Datei ausgeführt wurde.

Sobald die Python-Shell geöffnet ist, führen wir den folgenden Code aus, um die refaktorierten Funktionen zu testen:

```python
# Define a simple Stock class for testing
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        return cls(row[0], int(row[1]), float(row[2]))

    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'

# Test csv_as_dicts
with open('portfolio.csv') as f:
    portfolio_dicts = csv_as_dicts(f, [str, int, float])
print("First dictionary:", portfolio_dicts[0])

# Test csv_as_instances
with open('portfolio.csv') as f:
    portfolio_instances = csv_as_instances(f, Stock)
print("First instance:", portfolio_instances[0])
```

In diesem Code definieren wir zunächst eine einfache Klasse `Stock` zum Testen. Die Methode `__init__` initialisiert die Attribute einer `Stock`-Instanz. Die Klassenmethode `from_row` erstellt eine `Stock`-Instanz aus einer Zeile von CSV-Daten. Die Methode `__repr__` liefert eine String-Repräsentation der `Stock`-Instanz.

Dann testen wir die Funktion `csv_as_dicts()`, indem wir die Datei `portfolio.csv` öffnen und sie zusammen mit einer Liste von Typkonvertierungsfunktionen an die Funktion übergeben. Wir geben das erste Dictionary in der resultierenden Liste aus.

Schließlich testen wir die Funktion `csv_as_instances()`, indem wir die Datei `portfolio.csv` öffnen und sie zusammen mit der Klasse `Stock` an die Funktion übergeben. Wir geben die erste Instanz in der resultierenden Liste aus.

Wenn alles korrekt funktioniert, sollten Sie eine Ausgabe ähnlich der folgenden sehen:

```
First dictionary: {'name': 'AA', 'shares': 100, 'price': 32.2}
First instance: Stock(AA, 100, 32.2)
```

Diese Ausgabe zeigt, dass unsere refaktorierten Funktionen korrekt funktionieren. Wir haben die Code-Duplizierung erfolgreich eliminiert, während wir die gleiche Funktionalität beibehalten haben.

Um die Python-Shell zu verlassen, können Sie `exit()` eingeben oder Strg+D drücken.
