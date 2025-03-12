# Hinzufügen von Fehlerbehandlung

Wenn Sie mit realen Daten arbeiten, ist es sehr üblich, Inkonsistenzen oder Fehler zu finden. Beispielsweise können die Daten fehlende Werte, falsche Formate oder andere Probleme aufweisen. Python bietet Mechanismen zur Ausnahmebehandlung (Exception Handling), um diese Situationen elegant zu bewältigen. Die Ausnahmebehandlung ermöglicht es Ihrem Programm, auch dann weiterlaufen zu können, wenn es auf einen Fehler stößt, anstatt abrupt abzustürzen.

## Das Problem verstehen

Schauen wir uns die Datei `portfolio3.dat` an. Diese Datei enthält einige Daten über ein Portfolio, wie das Aktiensymbol, die Anzahl der Aktien und den Preis pro Aktie. Um den Inhalt dieser Datei anzuzeigen, können wir den folgenden Befehl verwenden:

```bash
cat /home/labex/project/portfolio3.dat
```

Wenn Sie diesen Befehl ausführen, werden Sie feststellen, dass einige Zeilen in der Datei Striche (`-`) anstelle von Zahlen für die Anzahl der Aktien enthalten. Hier ist ein Beispiel für das, was Sie sehen könnten:

```
AA 100 32.20
IBM 50 91.10
C - 53.08
...
```

Wenn wir versuchen, unseren aktuellen Code auf diese Datei anzuwenden, wird er abstürzen. Der Grund dafür ist, dass unser Code erwartet, die Anzahl der Aktien in eine Ganzzahl umzuwandeln, aber er kann einen Strich (`-`) nicht in eine Ganzzahl umwandeln. Versuchen wir, den Code auszuführen und sehen, was passiert:

```bash
python3 -c "import sys; sys.path.append('/home/labex/project'); from pcost import portfolio_cost; print(portfolio_cost('/home/labex/project/portfolio3.dat'))"
```

Sie werden eine Fehlermeldung wie diese sehen:

```
ValueError: invalid literal for int() with base 10: '-'
```

Dieser Fehler tritt auf, weil Python den `-`-Zeichen nicht in eine Ganzzahl umwandeln kann, wenn es versucht, `int(fields[1])` auszuführen.

## Einführung in die Ausnahmebehandlung

Python's Ausnahmebehandlung verwendet `try`- und `except`-Blöcke. Der `try`-Block enthält den Code, der eine Ausnahme auslösen könnte. Eine Ausnahme ist ein Fehler, der während der Ausführung eines Programms auftritt. Der `except`-Block enthält den Code, der ausgeführt wird, wenn im `try`-Block eine Ausnahme auftritt.

Hier ist ein Beispiel dafür, wie `try`- und `except`-Blöcke funktionieren:

```python
try:
    # Code that might raise an exception
    result = risky_operation()
except ExceptionType as e:
    # Code to handle the exception
    print(f"An error occurred: {e}")
```

Wenn Python den Code im `try`-Block ausführt und eine Ausnahme auftritt, springt die Ausführung sofort zum passenden `except`-Block. Der `ExceptionType` im `except`-Block gibt den Typ der Ausnahme an, die wir behandeln möchten. Die Variable `e` enthält Informationen über die Ausnahme, wie die Fehlermeldung.

## Modifizieren der Funktion mit Ausnahmebehandlung

Lassen Sie uns unsere `pcost.py`-Datei aktualisieren, um Fehler in den Daten zu behandeln. Wir verwenden die `try`- und `except`-Blöcke, um Zeilen mit fehlerhaften Daten zu überspringen und eine Warnmeldung anzuzeigen.

```python
def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    Handles lines with bad data by skipping them and showing a warning.

    Args:
        filename: The name of the portfolio file

    Returns:
        The total cost of the portfolio as a float
    """
    total_cost = 0.0

    # Open the file and read through each line
    with open(filename, 'r') as f:
        for line in f:
            fields = line.split()
            try:
                # Extract the data (symbol, shares, price)
                shares = int(fields[1])
                price = float(fields[2])
                # Add the cost to our running total
                total_cost += shares * price
            except ValueError as e:
                # Print a warning for lines that can't be parsed
                print(f"Couldn't parse: '{line}'")
                print(f"Reason: {e}")

    return total_cost

# Call the function with the portfolio3.dat file
if __name__ == '__main__':
    cost = portfolio_cost('/home/labex/project/portfolio3.dat')
    print(cost)
```

In diesem aktualisierten Code öffnen wir zunächst die Datei und lesen sie Zeile für Zeile. Für jede Zeile teilen wir sie in Felder auf. Dann versuchen wir, die Anzahl der Aktien in eine Ganzzahl und den Preis in eine Fließkommazahl umzuwandeln. Wenn diese Umwandlung fehlschlägt (d.h., wenn ein `ValueError` auftritt), geben wir eine Warnmeldung aus und überspringen diese Zeile. Andernfalls berechnen wir die Kosten der Aktien und addieren sie zur Gesamtkosten.

## Testen der aktualisierten Funktion

Jetzt lassen wir das aktualisierte Programm mit der problematischen Datei laufen. Zunächst müssen wir in das Projektverzeichnis navigieren und dann das Python-Skript ausführen.

```bash
cd /home/labex/project
python3 pcost.py
```

Sie sollten eine Ausgabe wie diese sehen:

```
Couldn't parse: 'C - 53.08
'
Reason: invalid literal for int() with base 10: '-'
Couldn't parse: 'DIS - 34.20
'
Reason: invalid literal for int() with base 10: '-'
44671.15
```

Das Programm macht jetzt Folgendes:

1. Es versucht, jede Zeile der Datei zu verarbeiten.
2. Wenn eine Zeile ungültige Daten enthält, fängt es den `ValueError` ab.
3. Es gibt eine hilfreiche Meldung über das Problem aus.
4. Es setzt die Verarbeitung der restlichen Datei fort.
5. Es gibt die Gesamtkosten basierend auf den gültigen Zeilen zurück.

Dieser Ansatz macht unser Programm viel robuster, wenn es mit unvollkommenen Daten umgeht. Es kann Fehler elegant behandeln und dennoch nützliche Ergebnisse liefern.
