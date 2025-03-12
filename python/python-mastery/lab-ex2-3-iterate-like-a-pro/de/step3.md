# Generatorausdrücke und Speichereffizienz

In diesem Schritt werden wir Generatorausdrücke erkunden. Diese sind unglaublich nützlich, wenn Sie in Python mit großen Datensätzen arbeiten. Sie können Ihren Code viel speichereffizienter machen, was von entscheidender Bedeutung ist, wenn Sie mit einer großen Datenmenge arbeiten.

## Verständnis von Generatorausdrücken

Ein Generatorausdruck ähnelt einer Listenkomprehension, aber es gibt einen wichtigen Unterschied. Wenn Sie eine Listenkomprehension verwenden, erstellt Python eine Liste mit allen Ergebnissen auf einmal. Dies kann viel Speicherplatz beanspruchen, insbesondere wenn Sie mit einem großen Datensatz arbeiten. Ein Generatorausdruck hingegen erzeugt die Ergebnisse nacheinander, sobald sie benötigt werden. Das bedeutet, dass er nicht alle Ergebnisse auf einmal im Speicher speichern muss, was eine beträchtliche Menge an Speicherplatz sparen kann.

Schauen wir uns ein einfaches Beispiel an, um zu verstehen, wie dies funktioniert:

```python
# Start a new Python session if needed
# python3

# List comprehension (creates a list in memory)
nums = [1, 2, 3, 4, 5]
squares_list = [x*x for x in nums]
print(squares_list)

# Generator expression (creates a generator object)
squares_gen = (x*x for x in nums)
print(squares_gen)  # This doesn't print the values, just the generator object

# Iterate through the generator to get values
for n in squares_gen:
    print(n)
```

Wenn Sie diesen Code ausführen, sehen Sie die folgende Ausgabe:

```
[1, 4, 9, 16, 25]
<generator object <genexpr> at 0x7f...>
1
4
9
16
25
```

Eine wichtige Eigenschaft von Generatoren ist, dass sie nur einmal durchlaufen werden können. Sobald Sie alle Werte in einem Generator durchlaufen haben, ist er erschöpft, und Sie können die Werte nicht erneut abrufen.

```python
# Try to iterate again over the same generator
for n in squares_gen:
    print(n)  # Nothing will be printed, as the generator is already exhausted
```

Sie können auch manuell nacheinander Werte aus einem Generator abrufen, indem Sie die `next()`-Funktion verwenden.

```python
# Create a fresh generator
squares_gen = (x*x for x in nums)

# Get values one by one
print(next(squares_gen))  # 1
print(next(squares_gen))  # 4
print(next(squares_gen))  # 9
```

Wenn es keine weiteren Werte im Generator gibt, löst der Aufruf von `next()` eine `StopIteration`-Ausnahme aus.

## Generatorfunktionen mit `yield`

Für komplexere Generatorlogik können Sie Generatorfunktionen mit der `yield`-Anweisung schreiben. Eine Generatorfunktion ist eine spezielle Art von Funktion, die `yield` verwendet, um Werte nacheinander zurückzugeben, anstatt ein einzelnes Ergebnis auf einmal zurückzugeben.

```python
def squares(nums):
    for x in nums:
        yield x*x

# Use the generator function
for n in squares(nums):
    print(n)
```

Wenn Sie diesen Code ausführen, sehen Sie die folgende Ausgabe:

```
1
4
9
16
25
```

## Reduzierung des Speicherverbrauchs mit Generatorausdrücken

Jetzt schauen wir uns an, wie Generatorausdrücke den Speicherverbrauch sparen können, wenn Sie mit großen Datensätzen arbeiten. Wir verwenden die CTA-Busdatendatei, die recht groß ist.

Zunächst versuchen wir einen speicherintensiven Ansatz:

```python
import tracemalloc
tracemalloc.start()

import readrides
rows = readrides.read_rides_as_dicts('ctabus.csv')
rt22 = [row for row in rows if row['route'] == '22']
max_row = max(rt22, key=lambda row: int(row['rides']))
print(max_row)

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")
```

Jetzt beenden Sie Python und starten Sie es neu, um es mit einem Generator-basierten Ansatz zu vergleichen:

```bash
exit() python3
```

```python
import tracemalloc
tracemalloc.start()

import csv
f = open('ctabus.csv')
f_csv = csv.reader(f)
headers = next(f_csv)

# Use generator expressions for all operations
rows = (dict(zip(headers, row)) for row in f_csv)
rt22 = (row for row in rows if row['route'] == '22')
max_row = max(rt22, key=lambda row: int(row['rides']))
print(max_row)

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")
```

Sie sollten einen deutlichen Unterschied im Speicherverbrauch zwischen diesen beiden Ansätzen bemerken. Der Generator-basierte Ansatz verarbeitet die Daten schrittweise, ohne alles auf einmal in den Speicher zu laden, was viel speichereffizienter ist.

## Generatorausdrücke mit Reduktionsfunktionen

Generatorausdrücke sind besonders nützlich, wenn sie mit Funktionen wie `sum()`, `min()`, `max()`, `any()` und `all()` kombiniert werden, die eine gesamte Sequenz verarbeiten und ein einzelnes Ergebnis produzieren.

Schauen wir uns einige Beispiele an:

```python
from readport import read_portfolio
portfolio = read_portfolio('portfolio.csv')

# Calculate the total value of the portfolio
total_value = sum(s['shares']*s['price'] for s in portfolio)
print(f"Total portfolio value: {total_value}")

# Find the minimum number of shares in any holding
min_shares = min(s['shares'] for s in portfolio)
print(f"Minimum shares in any holding: {min_shares}")

# Check if any stock is IBM
has_ibm = any(s['name'] == 'IBM' for s in portfolio)
print(f"Portfolio contains IBM: {has_ibm}")

# Check if all stocks are IBM
all_ibm = all(s['name'] == 'IBM' for s in portfolio)
print(f"All stocks are IBM: {all_ibm}")

# Count IBM shares
ibm_shares = sum(s['shares'] for s in portfolio if s['name'] == 'IBM')
print(f"Total IBM shares: {ibm_shares}")
```

Generatorausdrücke sind auch nützlich für Zeichenkettenoperationen. Hier ist, wie Sie Werte in einem Tupel verbinden können:

```python
s = ('GOOG', 100, 490.10)
# This would fail: ','.join(s)
# Use a generator expression to convert all items to strings
joined = ','.join(str(x) for x in s)
print(joined)  # Output: 'GOOG,100,490.1'
```

Der Hauptvorteil der Verwendung von Generatorausdrücken in diesen Beispielen ist, dass keine Zwischenlisten erstellt werden, was zu einem speichereffizienteren Code führt.
