# Erstellen von Algorithmus-Template-Klassen

In diesem Schritt werden wir abstrakte Basisklassen nutzen, um ein Template-Methoden-Muster (Template Method Pattern) zu implementieren. Das Ziel besteht darin, die Code-Duplizierung in der CSV-Parsing-Funktionalität zu reduzieren. Code-Duplizierung kann es schwieriger machen, Ihren Code zu warten und zu aktualisieren. Durch die Verwendung des Template-Methoden-Musters können wir eine gemeinsame Struktur für unseren CSV-Parsing-Code erstellen und den Unterklassen die Behandlung der spezifischen Details überlassen.

## Verständnis des Template-Methoden-Musters

Das Template-Methoden-Muster ist ein Verhaltensmuster (Behavioral Design Pattern). Es ist wie ein Bauplan für einen Algorithmus. In einer Methode definiert es die Gesamtstruktur oder das "Gerüst" eines Algorithmus. Allerdings implementiert es nicht alle Schritte vollständig. Stattdessen überlässt es einige Schritte den Unterklassen. Dies bedeutet, dass Unterklassen bestimmte Teile des Algorithmus neu definieren können, ohne seine Gesamtstruktur zu ändern.

In unserem Fall, wenn Sie sich die Datei `reader.py` ansehen, werden Sie feststellen, dass die Funktionen `read_csv_as_dicts()` und `read_csv_as_instances()` viel ähnlichen Code haben. Der Hauptunterschied zwischen ihnen besteht darin, wie sie aus den Zeilen der CSV-Datei Datensätze erstellen. Durch die Verwendung des Template-Methoden-Musters können wir vermeiden, den gleichen Code mehrmals zu schreiben.

## Hinzufügen der CSVParser-Basisklasse

Beginnen wir damit, eine abstrakte Basisklasse für unser CSV-Parsing hinzuzufügen. Öffnen Sie die Datei `reader.py`. Wir fügen die abstrakte Basisklasse `CSVParser` ganz oben in der Datei, direkt nach den Importanweisungen, hinzu.

```python
# reader.py
import csv
from abc import ABC, abstractmethod

class CSVParser(ABC):
    def parse(self, filename):
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = self.make_record(headers, row)
                records.append(record)
        return records

    @abstractmethod
    def make_record(self, headers, row):
        pass
```

Diese `CSVParser`-Klasse dient als Template für das CSV-Parsing. Die `parse`-Methode enthält die gemeinsamen Schritte zum Lesen einer CSV-Datei, wie das Öffnen der Datei, das Abrufen der Überschriften und das Iterieren über die Zeilen. Die spezifische Logik zum Erstellen eines Datensatzes aus einer Zeile wird in die `make_record()`-Methode abstrahiert. Da es sich um eine abstrakte Methode handelt, muss jede Klasse, die von `CSVParser` erbt, diese Methode implementieren.

## Implementieren der konkreten Parser-Klassen

Nachdem wir nun unsere Basisklasse haben, müssen wir die konkreten Parser-Klassen erstellen. Diese Klassen werden die spezifische Logik zur Datensatz-Erstellung implementieren.

```python
class DictCSVParser(CSVParser):
    def __init__(self, types):
        self.types = types

    def make_record(self, headers, row):
        return { name: func(val) for name, func, val in zip(headers, self.types, row) }

class InstanceCSVParser(CSVParser):
    def __init__(self, cls):
        self.cls = cls

    def make_record(self, headers, row):
        return self.cls.from_row(row)
```

Die `DictCSVParser`-Klasse wird verwendet, um Datensätze als Wörterbücher (Dictionaries) zu erstellen. Sie nimmt in ihrem Konstruktor eine Liste von Typen entgegen. Die `make_record`-Methode verwendet diese Typen, um die Werte in der Zeile zu konvertieren und ein Wörterbuch zu erstellen.

Die `InstanceCSVParser`-Klasse wird verwendet, um Datensätze als Instanzen einer Klasse zu erstellen. Sie nimmt in ihrem Konstruktor eine Klasse entgegen. Die `make_record`-Methode ruft die `from_row`-Methode dieser Klasse auf, um eine Instanz aus der Zeile zu erstellen.

## Refactoring der ursprünglichen Funktionen

Jetzt refaktorisieren wir die ursprünglichen Funktionen `read_csv_as_dicts()` und `read_csv_as_instances()`, um diese neuen Klassen zu verwenden.

```python
def read_csv_as_dicts(filename, types):
    '''
    Read a CSV file into a list of dictionaries with appropriate type conversion.
    '''
    parser = DictCSVParser(types)
    return parser.parse(filename)

def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances of a class.
    '''
    parser = InstanceCSVParser(cls)
    return parser.parse(filename)
```

Diese refaktorierten Funktionen haben die gleiche Schnittstelle wie die ursprünglichen. Intern verwenden sie jedoch die neuen Parser-Klassen, die wir gerade erstellt haben. Auf diese Weise haben wir die gemeinsame CSV-Parsing-Logik von der spezifischen Logik zur Datensatz-Erstellung getrennt.

## Testen Ihrer Implementierung

Überprüfen wir, ob unser refaktoriertes Code korrekt funktioniert. Erstellen Sie eine Datei namens `test_reader.py` und fügen Sie den folgenden Code hinzu.

```python
import reader
import stock

# Test the refactored read_csv_as_instances function
portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
print("First stock:", portfolio[0])

# Test the refactored read_csv_as_dicts function
portfolio_dicts = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("First stock as dict:", portfolio_dicts[0])

# Test direct use of a parser
parser = reader.DictCSVParser([str, int, float])
portfolio_dicts2 = parser.parse('portfolio.csv')
print("First stock from direct parser:", portfolio_dicts2[0])
```

Um den Test auszuführen, öffnen Sie Ihr Terminal und führen Sie den folgenden Befehl aus:

```bash
python test_reader.py
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
First stock: Stock('AA', 100, 32.2)
First stock as dict: {'name': 'AA', 'shares': 100, 'price': 32.2}
First stock from direct parser: {'name': 'AA', 'shares': 100, 'price': 32.2}
```

Wenn Sie diese Ausgabe sehen, bedeutet dies, dass Ihr refaktoriertes Code korrekt funktioniert. Sowohl die ursprünglichen Funktionen als auch die direkte Verwendung von Parsern liefern die erwarteten Ergebnisse.
