# Verständnis von Code-Duplizierung

Beginnen wir damit, uns den aktuellen Code in der Datei `reader.py` anzusehen. Beim Programmieren ist es ein wichtiger Schritt, bestehenden Code zu untersuchen, um zu verstehen, wie die Dinge funktionieren und Bereiche für Verbesserungen zu identifizieren. Sie können die Datei `reader.py` im WebIDE öffnen. Es gibt zwei Möglichkeiten, dies zu tun. Sie können auf die Datei im Dateiexplorer klicken, oder Sie können die folgenden Befehle im Terminal ausführen. Diese Befehle navigieren zunächst zum Projektverzeichnis und zeigen dann den Inhalt der Datei `reader.py` an.

```bash
cd ~/project
cat reader.py
```

Wenn Sie sich den Code ansehen, werden Sie feststellen, dass es zwei Funktionen gibt. Funktionen in Python sind Codeblöcke, die eine bestimmte Aufgabe ausführen. Hier sind die beiden Funktionen und was sie tun:

1. `csv_as_dicts()`: Diese Funktion nimmt CSV-Daten und wandelt sie in eine Liste von Dictionaries um. Ein Dictionary in Python ist eine Sammlung von Schlüssel-Wert-Paaren, die nützlich ist, um Daten strukturiert zu speichern.
2. `csv_as_instances()`: Diese Funktion nimmt CSV-Daten und wandelt sie in eine Liste von Instanzen um. Eine Instanz ist ein Objekt, das aus einer Klasse erstellt wird, die ein Bauplan für die Erstellung von Objekten ist.

Lassen Sie uns nun genauer auf diese beiden Funktionen schauen. Sie werden feststellen, dass sie ziemlich ähnlich sind. Beide Funktionen folgen diesen Schritten:

- Zunächst initialisieren sie eine leere `records`-Liste. Eine Liste in Python ist eine Sammlung von Elementen, die unterschiedlicher Typen sein können. Das Initialisieren einer leeren Liste bedeutet, eine Liste ohne Elemente zu erstellen, die zur Speicherung der verarbeiteten Daten verwendet wird.
- Dann verwenden sie `csv.reader()`, um die Eingabe zu parsen. Parsen bedeutet, die Eingabedaten zu analysieren, um sinnvolle Informationen zu extrahieren. In diesem Fall hilft uns `csv.reader()`, die CSV-Daten Zeile für Zeile zu lesen.
- Sie behandeln die Header auf die gleiche Weise. Header in einer CSV-Datei sind die erste Zeile, die normalerweise die Namen der Spalten enthält.
- Danach durchlaufen sie jede Zeile in den CSV-Daten in einer Schleife. Eine Schleife ist ein Programmierkonstrukt, das es Ihnen ermöglicht, einen Codeblock mehrmals auszuführen.
- Für jede Zeile verarbeiten sie diese, um einen Datensatz zu erstellen. Dieser Datensatz kann entweder ein Dictionary oder eine Instanz sein, je nach Funktion.
- Sie fügen den Datensatz der `records`-Liste hinzu. Hinzufügen bedeutet, ein Element ans Ende der Liste anzufügen.
- Schließlich geben sie die `records`-Liste zurück, die alle verarbeiteten Daten enthält.

Diese Duplizierung von Code ist aus mehreren Gründen ein Problem. Wenn Code dupliziert wird:

- Wird er schwieriger zu warten. Wenn Sie eine Änderung am Code vornehmen müssen, müssen Sie die gleiche Änderung an mehreren Stellen vornehmen. Dies erfordert mehr Zeit und Aufwand.
- Müssen alle Änderungen an mehreren Stellen implementiert werden. Dies erhöht die Wahrscheinlichkeit, dass Sie vergessen, die Änderung an einer der Stellen vorzunehmen, was zu inkonsistentem Verhalten führt.
- Es erhöht auch die Wahrscheinlichkeit, dass Fehler eingeführt werden. Fehler sind Fehler im Code, die dazu führen können, dass er unerwartet verhält.

Der einzige echte Unterschied zwischen diesen beiden Funktionen ist, wie sie eine Zeile in einen Datensatz umwandeln. Dies ist eine klassische Situation, in der eine höhere Funktion (higher-order function) sehr nützlich sein kann. Eine höhere Funktion ist eine Funktion, die eine andere Funktion als Argument nehmen oder eine Funktion als Ergebnis zurückgeben kann.

Lassen Sie uns einige Beispielverwendungen dieser Funktionen betrachten, um besser zu verstehen, wie sie funktionieren. Der folgende Code zeigt, wie man `csv_as_dicts()` und `csv_as_instances()` verwendet:

```python
# Example of using csv_as_dicts
with open('portfolio.csv') as f:
    portfolio = csv_as_dicts(f, [str, int, float])
print(portfolio[0])  # {'name': 'AA', 'shares': 100, 'price': 32.2}

# Example of using csv_as_instances
class Stock:
    @classmethod
    def from_row(cls, row):
        return cls(row[0], int(row[1]), float(row[2]))

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

with open('portfolio.csv') as f:
    portfolio = csv_as_instances(f, Stock)
print(portfolio[0].name, portfolio[0].shares, portfolio[0].price)  # AA 100 32.2
```

Im nächsten Schritt werden wir eine höhere Funktion erstellen, um diese Code-Duplizierung zu beseitigen. Dies wird den Code wartbarer und fehleranfälliger machen.
