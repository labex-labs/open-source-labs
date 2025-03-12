# Verwendung der `map()`-Funktion

In Python ist eine höhere Funktion (Higher-Order Function) eine Funktion, die eine andere Funktion als Argument nehmen oder eine Funktion als Ergebnis zurückgeben kann. Python's `map()`-Funktion ist ein hervorragendes Beispiel für eine höhere Funktion. Sie ist ein mächtiges Werkzeug, das es Ihnen ermöglicht, eine gegebene Funktion auf jedes Element in einem iterierbaren Objekt, wie z. B. einer Liste oder einem Tupel, anzuwenden. Nachdem die Funktion auf jedes Element angewendet wurde, gibt sie einen Iterator der Ergebnisse zurück. Diese Eigenschaft macht `map()` perfekt für die Verarbeitung von Datenfolgen, wie z. B. Zeilen in einer CSV-Datei.

Die grundlegende Syntax der `map()`-Funktion lautet wie folgt:

```python
map(function, iterable, ...)
```

Hierbei ist die `function` die Operation, die Sie auf jedes Element in der `iterable` ausführen möchten. Die `iterable` ist eine Sequenz von Elementen, wie z. B. eine Liste oder ein Tupel.

Schauen wir uns ein einfaches Beispiel an. Angenommen, Sie haben eine Liste von Zahlen und möchten jede Zahl in dieser Liste quadrieren. Sie können die `map()`-Funktion verwenden, um dies zu erreichen. So geht's:

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
```

In diesem Beispiel definieren wir zunächst eine Liste namens `numbers`. Dann verwenden wir die `map()`-Funktion. Die `lambda`-Funktion `lambda x: x * x` ist die Operation, die wir auf jedes Element in der `numbers`-Liste ausführen möchten. Die `map()`-Funktion wendet diese `lambda`-Funktion auf jede Zahl in der Liste an. Da `map()` einen Iterator zurückgibt, wandeln wir ihn mit der `list()`-Funktion in eine Liste um. Schließlich geben wir die `squared`-Liste aus, die die quadrierten Werte der ursprünglichen Zahlen enthält.

Jetzt schauen wir uns an, wie wir die `map()`-Funktion verwenden können, um unsere `convert_csv()`-Funktion zu modifizieren. Zuvor haben wir eine `for`-Schleife verwendet, um über die Zeilen in den CSV-Daten zu iterieren. Jetzt ersetzen wir diese `for`-Schleife durch die `map()`-Funktion.

```python
def convert_csv(lines, conversion_func, *, headers=None):
    '''
    Convert lines of CSV data using the provided conversion function
    '''
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)

    # Use map to apply conversion_func to each row
    records = list(map(lambda row: conversion_func(headers, row), rows))
    return records
```

Diese aktualisierte Version der `convert_csv()`-Funktion macht genau dasselbe wie die vorherige Version, aber sie verwendet die `map()`-Funktion anstelle einer `for`-Schleife. Die `lambda`-Funktion innerhalb der `map()` nimmt jede Zeile aus den CSV-Daten und wendet die `conversion_func` zusammen mit den Spaltenüberschriften darauf an.

Lassen Sie uns diese aktualisierte Funktion testen, um sicherzustellen, dass sie korrekt funktioniert. Öffnen Sie zunächst Ihr Terminal und navigieren Sie in das Projektverzeichnis. Starten Sie dann die interaktive Python-Shell mit der `reader.py`-Datei.

```bash
cd ~/project
python3 -i reader.py
```

Sobald Sie sich in der Python-Shell befinden, führen Sie den folgenden Code aus, um die aktualisierte `convert_csv()`-Funktion zu testen:

```python
# Test the updated convert_csv function
with open('portfolio.csv') as f:
    result = convert_csv(f, make_dict)
print(result[0])  # Should print the first dictionary

# Test that csv_as_dicts still works
with open('portfolio.csv') as f:
    portfolio = csv_as_dicts(f, [str, int, float])
print(portfolio[0])  # Should print the first dictionary with converted types
```

Nachdem Sie diesen Code ausgeführt haben, sollten Sie eine Ausgabe ähnlich der folgenden sehen:

```
{'name': 'AA', 'shares': '100', 'price': '32.20'}
{'name': 'AA', 'shares': 100, 'price': 32.2}
```

Diese Ausgabe zeigt, dass die aktualisierte `convert_csv()`-Funktion, die die `map()`-Funktion verwendet, korrekt funktioniert, und die Funktionen, die darauf basieren, weiterhin wie erwartet funktionieren.

Die Verwendung der `map()`-Funktion hat mehrere Vorteile:

1. Sie kann kompakter sein als eine `for`-Schleife. Anstatt mehrere Codezeilen für eine `for`-Schleife zu schreiben, können Sie dasselbe Ergebnis mit einer einzigen Zeile mit `map()` erreichen.
2. Sie kommuniziert klar, dass Sie jedes Element in einer Sequenz transformieren möchten. Wenn Sie `map()` sehen, wissen Sie sofort, dass Sie eine Funktion auf jedes Element in einem iterierbaren Objekt anwenden.
3. Sie kann speichereffizienter sein, da sie einen Iterator zurückgibt. Ein Iterator generiert Werte on-the-fly, was bedeutet, dass er nicht alle Ergebnisse auf einmal im Speicher speichert. In unserem Beispiel haben wir den von `map()` zurückgegebenen Iterator in eine Liste umgewandelt, aber in einigen Fällen können Sie direkt mit dem Iterator arbeiten, um Speicher zu sparen.

Um die Python-Shell zu verlassen, können Sie `exit()` eingeben oder Strg+D drücken.
