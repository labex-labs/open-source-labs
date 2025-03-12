# Erkundung des collections-Moduls

In Python sind die eingebauten Container wie Listen, Wörterbücher und Mengen sehr nützlich. Allerdings geht das `collections`-Modul von Python einen Schritt weiter, indem es spezialisierte Container-Datentypen bereitstellt, die die Funktionalität dieser eingebauten Container erweitern. Werfen wir einen genaueren Blick auf einige dieser nützlichen Datentypen.

Sie werden weiterhin in Ihrem Python-Terminal arbeiten und den untenstehenden Beispielen folgen.

## Counter

Die `Counter`-Klasse ist eine Unterklasse des Wörterbuchs. Ihr Hauptzweck besteht darin, hashbare Objekte zu zählen. Sie bietet eine bequeme Möglichkeit, Elemente zu zählen und unterstützt eine Vielzahl von Operationen.

Zunächst müssen wir die `Counter`-Klasse und eine Funktion zum Lesen eines Portfolios importieren. Dann lesen wir ein Portfolio aus einer CSV-Datei.

```python
>>> from collections import Counter
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')

```

Jetzt erstellen wir ein `Counter`-Objekt, um die Anzahl der Anteile für jede Aktie anhand ihres Namens zu zählen.

```python
# Create a counter to count shares by stock name
>>> totals = Counter()
>>> for s in portfolio:
...     totals[s['name']] += s['shares']
...
>>> print(totals)
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
```

Eines der großartigen Merkmale des `Counter`-Objekts ist, dass es neue Schlüssel automatisch mit einer Anzahl von 0 initialisiert. Dies bedeutet, dass Sie nicht prüfen müssen, ob ein Schlüssel existiert, bevor Sie seine Anzahl erhöhen, was den Code zum Akkumulieren von Zählungen vereinfacht.

Counters verfügen auch über spezielle Methoden. Beispielsweise ist die `most_common()`-Methode für die Datenanalyse sehr nützlich.

```python
# Get the two stocks with the most shares
>>> most_common_stocks = totals.most_common(2)
>>> print(most_common_stocks)
[('MSFT', 250), ('IBM', 150)]
```

Darüber hinaus können Zähler mithilfe von arithmetischen Operationen kombiniert werden.

```python
# Create another counter
>>> more = Counter()
>>> more['IBM'] = 75
>>> more['AA'] = 200
>>> more['ACME'] = 30
>>> print(more)
Counter({'AA': 200, 'IBM': 75, 'ACME': 30})

# Add two counters together
>>> combined = totals + more
>>> print(combined)
Counter({'AA': 300, 'MSFT': 250, 'IBM': 225, 'CAT': 150, 'GE': 95, 'ACME': 30})
```

## defaultdict

Das `defaultdict` ähnelt einem normalen Wörterbuch, hat aber ein einzigartiges Merkmal. Es bietet einen Standardwert für Schlüssel, die noch nicht existieren. Dies kann Ihren Code vereinfachen, da Sie nicht mehr prüfen müssen, ob ein Schlüssel existiert, bevor Sie ihn verwenden.

```python
>>> from collections import defaultdict

# Group portfolio entries by stock name
>>> byname = defaultdict(list)
>>> for s in portfolio:
...     byname[s['name']].append(s)
...
>>> print(byname['IBM'])
[{'name': 'IBM', 'shares': 50, 'price': 91.1}, {'name': 'IBM', 'shares': 100, 'price': 70.44}]
>>> print(byname['AA'])
[{'name': 'AA', 'shares': 100, 'price': 32.2}]
```

Wenn Sie ein `defaultdict(list)` erstellen, erstellt es automatisch eine neue leere Liste für jeden neuen Schlüssel. So können Sie direkt an den Wert eines Schlüssels anhängen, auch wenn der Schlüssel vorher nicht existierte. Dies beseitigt die Notwendigkeit, zu prüfen, ob der Schlüssel existiert, und manuell eine leere Liste zu erstellen.

Sie können auch andere Standard-Fabrikfunktionen verwenden. Beispielsweise können Sie `int`, `float` oder sogar Ihre eigene benutzerdefinierte Funktion verwenden.

```python
# Use defaultdict with int to count items
>>> word_counts = defaultdict(int)
>>> words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
>>> for word in words:
...     word_counts[word] += 1
...
>>> print(word_counts)
defaultdict(<class 'int'>, {'apple': 3, 'orange': 2, 'banana': 1})
```

Diese spezialisierten Container-Typen aus dem `collections`-Modul können Ihren Code kompakter und effizienter machen, wenn Sie mit Daten arbeiten.
