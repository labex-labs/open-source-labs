# Arbeiten mit Wörterbüchern und CSV-Daten

Beginnen wir damit, einen einfachen Datensatz über Aktienbesitz zu untersuchen. In diesem Schritt lernen Sie, wie Sie Daten aus einer CSV-Datei lesen und mithilfe von Wörterbüchern in einem strukturierten Format speichern.

Eine CSV (Comma-Separated Values, Komma-separierte Werte)-Datei ist eine gängige Methode, um tabellarische Daten zu speichern, wobei jede Zeile eine Zeile darstellt und die Werte durch Kommas getrennt sind. Wörterbücher in Python sind eine leistungsstarke Datenstruktur, die es Ihnen ermöglicht, Schlüssel-Wert-Paare zu speichern. Indem wir Wörterbücher verwenden, können wir die Daten aus der CSV-Datei auf eine sinnvollere Weise organisieren.

Erstellen Sie zunächst eine neue Python-Datei in der WebIDE, indem Sie die folgenden Schritte ausführen:

1. Klicken Sie auf die Schaltfläche "Neue Datei" in der WebIDE.
2. Benennen Sie die Datei `readport.py`.
3. Kopieren und fügen Sie den folgenden Code in die Datei ein:

```python
# readport.py

import csv

# A function that reads a file into a list of dictionaries
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)   # Skip the header row
        for row in rows:
            record = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(record)
    return portfolio
```

Dieser Code definiert eine Funktion `read_portfolio`, die mehrere wichtige Aufgaben ausführt:

1. Sie öffnet eine CSV-Datei, die durch den Parameter `filename` angegeben wird. Die Funktion `open` wird verwendet, um auf die Datei zuzugreifen, und die `with`-Anweisung stellt sicher, dass die Datei ordnungsgemäß geschlossen wird, nachdem wir sie gelesen haben.
2. Sie überspringt die Kopfzeile. Die Kopfzeile enthält normalerweise die Namen der Spalten in der CSV-Datei. Wir verwenden `next(rows)`, um den Iterator zur nächsten Zeile zu bewegen und somit die Kopfzeile zu überspringen.
3. Für jede Datenzeile erstellt sie ein Wörterbuch. Die Schlüssel des Wörterbuchs sind 'name', 'shares' und 'price'. Diese Schlüssel helfen uns, die Daten auf eine intuitivere Weise zuzugreifen.
4. Sie konvertiert die Anzahl der Aktien in Ganzzahlen und die Preise in Gleitkommazahlen. Dies ist wichtig, da die aus der CSV-Datei gelesenen Daten zunächst im String-Format vorliegen und wir numerische Werte für Berechnungen benötigen.
5. Sie fügt jedes Wörterbuch einer Liste namens `portfolio` hinzu. Diese Liste enthält alle Datensätze aus der CSV-Datei.
6. Schließlich gibt sie die vollständige Liste der Wörterbücher zurück.

Nun erstellen wir eine Datei für die Transitdaten. Erstellen Sie eine neue Datei namens `readrides.py` mit folgendem Inhalt:

```python
# readrides.py

import csv

def read_rides_as_dicts(filename):
    """
    Read the CTA bus data as a list of dictionaries
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)   # Skip header
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides
            }
            records.append(record)
    return records
```

Die Funktion `read_rides_as_dicts` funktioniert ähnlich wie die Funktion `read_portfolio`. Sie liest eine CSV-Datei, die sich auf die CTA-Busdaten bezieht, überspringt die Kopfzeile, erstellt für jede Datenzeile ein Wörterbuch und speichert diese Wörterbücher in einer Liste.

Nun testen wir die Funktion `read_portfolio`, indem wir in der WebIDE ein Terminal öffnen:

1. Klicken Sie auf das Menü "Terminal" und wählen Sie "Neues Terminal" aus.
2. Starten Sie den Python-Interpreter, indem Sie `python3` eingeben.
3. Führen Sie die folgenden Befehle aus:

```python
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')
>>> from pprint import pprint
>>> pprint(portfolio)
[{'name': 'AA', 'price': 32.2, 'shares': 100},
 {'name': 'IBM', 'price': 91.1, 'shares': 50},
 {'name': 'CAT', 'price': 83.44, 'shares': 150},
 {'name': 'MSFT', 'price': 51.23, 'shares': 200},
 {'name': 'GE', 'price': 40.37, 'shares': 95},
 {'name': 'MSFT', 'price': 65.1, 'shares': 50},
 {'name': 'IBM', 'price': 70.44, 'shares': 100}]
```

Die Funktion `pprint` (pretty print) wird hier verwendet, um die Daten in einem lesbareren Format anzuzeigen. Jedes Element in der Liste ist ein Wörterbuch, das einen Aktienbesitz darstellt. Das Wörterbuch hat die folgenden Schlüssel:

- Ein Aktiensymbol (`name`): Dies ist die Abkürzung, die zur Identifizierung der Aktie verwendet wird.
- Anzahl der gehaltenen Aktien (`shares`): Dies gibt an, wie viele Aktien der Aktie gehalten werden.
- Kaufpreis pro Aktie (`price`): Dies ist der Preis, zu dem jede Aktie gekauft wurde.

Beachten Sie, dass einige Aktien wie 'MSFT' und 'IBM' mehrmals auftauchen. Dies repräsentiert verschiedene Käufe derselben Aktie, die möglicherweise zu verschiedenen Zeiten und zu verschiedenen Preisen getätigt wurden.
