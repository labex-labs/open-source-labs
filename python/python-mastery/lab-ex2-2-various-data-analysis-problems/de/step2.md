# Verwendung von Listen-, Mengen- und Wörterbuch-Komprehensionen

Python-Komprehensionen sind eine sehr nützliche und kompakte Methode, um neue Sammlungen (Collections) auf der Grundlage bestehender zu erstellen. Sammlungen in Python können Listen, Mengen oder Wörterbücher sein, die wie Container fungieren, die verschiedene Datentypen enthalten. Komprehensionen ermöglichen es Ihnen, bestimmte Daten auszufiltern, die Daten auf irgendeine Weise zu transformieren und sie effizienter zu organisieren. In diesem Teil werden wir unsere Portfoliodaten nutzen, um zu untersuchen, wie diese Komprehensionen funktionieren.

Zunächst müssen Sie ein Python-Terminal öffnen, genau wie Sie es im vorherigen Schritt getan haben. Sobald das Terminal geöffnet ist, geben Sie die folgenden Beispiele nacheinander ein. Dieser praktische Ansatz wird Ihnen helfen, zu verstehen, wie Komprehensionen in der Praxis funktionieren.

## Listen-Komprehensionen

Eine Listen-Komprehension ist eine spezielle Syntax in Python, die eine neue Liste erstellt. Sie tut dies, indem sie einen Ausdruck auf jedes Element in einer bestehenden Sammlung anwendet.

Beginnen wir mit einem Beispiel. Zunächst importieren wir eine Funktion, um unsere Portfoliodaten zu lesen. Dann verwenden wir eine Listen-Komprehension, um bestimmte Anteile aus dem Portfolio auszufiltern.

```python
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')

# Find all holdings with more than 100 shares
>>> large_holdings = [s for s in portfolio if s['shares'] > 100]
>>> print(large_holdings)
[{'name': 'CAT', 'shares': 150, 'price': 83.44}, {'name': 'MSFT', 'shares': 200, 'price': 51.23}]
```

In diesem Code importieren wir zunächst die Funktion `read_portfolio` und verwenden sie, um die Portfoliodaten aus einer CSV-Datei zu lesen. Dann geht die Listen-Komprehension `[s for s in portfolio if s['shares'] > 100]` durch jedes Element `s` in der `portfolio`-Sammlung. Sie fügt das Element `s` nur zur neuen Liste `large_holdings` hinzu, wenn die Anzahl der Anteile in diesem Bestandteil größer als 100 ist.

Listen-Komprehensionen können auch zur Durchführung von Berechnungen verwendet werden. Hier sind einige Beispiele:

```python
# Calculate the total cost of each holding (shares * price)
>>> holding_costs = [s['shares'] * s['price'] for s in portfolio]
>>> print(holding_costs)
[3220.0, 4555.0, 12516.0, 10246.0, 3835.15, 3255.0, 7044.0]

# Calculate the total cost of the entire portfolio
>>> total_portfolio_cost = sum([s['shares'] * s['price'] for s in portfolio])
>>> print(total_portfolio_cost)
44671.15
```

Im ersten Beispiel berechnet die Listen-Komprehension `[s['shares'] * s['price'] for s in portfolio]` die Gesamtkosten jedes Bestandteils, indem sie die Anzahl der Anteile mit dem Preis für jedes Element in der `portfolio` multipliziert. Im zweiten Beispiel verwenden wir die Funktion `sum` zusammen mit der Listen-Komprehension, um die Gesamtkosten des gesamten Portfolios zu berechnen.

## Mengen-Komprehensionen

Eine Mengen-Komprehension wird verwendet, um eine Menge aus einer bestehenden Sammlung zu erstellen. Eine Menge ist eine Sammlung, die nur eindeutige Werte enthält.

Schauen wir uns an, wie es mit unseren Portfoliodaten funktioniert:

```python
# Find all unique stock names
>>> unique_stocks = {s['name'] for s in portfolio}
>>> print(unique_stocks)
{'MSFT', 'IBM', 'AA', 'GE', 'CAT'}
```

In diesem Code geht die Mengen-Komprehension `{s['name'] for s in portfolio}` durch jedes Element `s` in der `portfolio` und fügt den Aktiennamen (`s['name']`) zur Menge `unique_stocks` hinzu. Da Mengen nur eindeutige Werte speichern, erhalten wir am Ende eine Liste aller verschiedenen Aktien in unserem Portfolio ohne Duplikate.

## Wörterbuch-Komprehensionen

Eine Wörterbuch-Komprehension erstellt ein neues Wörterbuch, indem sie Ausdrücke anwendet, um Schlüssel-Wert-Paare zu erstellen.

Hier ist ein Beispiel für die Verwendung einer Wörterbuch-Komprehension, um die Gesamtanzahl der Anteile für jede Aktie in unserem Portfolio zu zählen:

```python
# Create a dictionary to count total shares for each stock
>>> totals = {s['name']: 0 for s in portfolio}
>>> for s in portfolio:
...     totals[s['name']] += s['shares']
...
>>> print(totals)
{'AA': 100, 'IBM': 150, 'CAT': 150, 'MSFT': 250, 'GE': 95}
```

In der ersten Zeile erstellt die Wörterbuch-Komprehension `{s['name']: 0 for s in portfolio}` ein Wörterbuch, in dem jeder Aktienname (`s['name']`) ein Schlüssel ist und der anfängliche Wert für jeden Schlüssel 0 ist. Dann verwenden wir eine `for`-Schleife, um durch jedes Element in der `portfolio` zu gehen. Für jedes Element addieren wir die Anzahl der Anteile (`s['shares']`) zum entsprechenden Wert im `totals`-Wörterbuch.

Diese Komprehensionen sind sehr leistungsstark, da sie es Ihnen ermöglichen, Daten mit nur wenigen Codezeilen zu transformieren und zu analysieren. Sie sind ein großartiges Werkzeug in Ihrem Python-Programmierwerkzeugkasten.
