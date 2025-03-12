# Die Erkundung des Python-Speichermodells

Das Python-Speichermodell spielt eine entscheidende Rolle bei der Bestimmung, wie Objekte im Speicher gespeichert und referenziert werden. Das Verständnis dieses Modells ist besonders wichtig, wenn Sie mit großen Datensätzen arbeiten, da es die Leistung und den Speicherverbrauch Ihrer Python-Programme erheblich beeinflussen kann. In diesem Schritt werden wir uns speziell darauf konzentrieren, wie Zeichenkettenobjekte in Python behandelt werden, und Möglichkeiten zur Optimierung des Speicherverbrauchs für große Datensätze untersuchen.

## Zeichenkettenwiederholungen in Datensätzen

Die CTA-Bus-Daten enthalten viele wiederholte Werte, wie z.B. Routennamen. Wiederholte Werte in einem Datensatz können zu einem ineffizienten Speicherverbrauch führen, wenn sie nicht richtig behandelt werden. Um das Ausmaß dieses Problems zu verstehen, lassen Sie uns zunächst untersuchen, wie viele eindeutige Routenzeichenketten es im Datensatz gibt.

Zunächst öffnen Sie einen Python-Interpreter. Sie können dies tun, indem Sie den folgenden Befehl in Ihrem Terminal ausführen:

```bash
python3
```

Sobald der Python-Interpreter geöffnet ist, laden wir die CTA-Bus-Daten und finden die eindeutigen Routen. Hier ist der Code, um dies zu erreichen:

```python
import reader
rows = reader.read_csv_as_dicts('ctabus.csv', [str, str, str, int])

# Find unique route names
routes = {row['route'] for row in rows}
print(f"Number of unique route names: {len(routes)}")
```

In diesem Code importieren wir zunächst das `reader`-Modul, das vermutlich eine Funktion zum Lesen von CSV-Dateien als Wörterbücher enthält. Dann verwenden wir die `read_csv_as_dicts`-Funktion, um die Daten aus der `ctabus.csv`-Datei zu laden. Das zweite Argument `[str, str, str, int]` gibt die Datentypen für jede Spalte in der CSV-Datei an. Danach verwenden wir eine Mengenkomprehension, um alle eindeutigen Routennamen im Datensatz zu finden und geben die Anzahl der eindeutigen Routennamen aus.

Die Ausgabe sollte sein:

```
Number of unique route names: 181
```

Jetzt überprüfen wir, wie viele verschiedene Zeichenkettenobjekte für diese Routen erstellt werden. Auch wenn es nur 181 eindeutige Routennamen gibt, kann Python für jedes Vorkommen eines Routennamens im Datensatz ein neues Zeichenkettenobjekt erstellen. Um dies zu überprüfen, verwenden wir die `id()`-Funktion, um die eindeutige Kennung jedes Zeichenkettenobjekts zu erhalten.

```python
# Count unique string object IDs
routeids = {id(row['route']) for row in rows}
print(f"Number of unique route string objects: {len(routeids)}")
```

Die Ausgabe mag Sie überraschen:

```
Number of unique route string objects: 542305
```

Dies zeigt, dass es nur 181 eindeutige Routennamen gibt, aber über 500.000 eindeutige Zeichenkettenobjekte. Dies geschieht, weil Python für jede Zeile ein neues Zeichenkettenobjekt erstellt, auch wenn die Werte gleich sind. Dies kann zu einem erheblichen Speicherverschwendung führen, insbesondere wenn Sie mit großen Datensätzen arbeiten.

## Zeichenketten-Interning zur Speichersparnis

Python bietet eine Möglichkeit, Zeichenketten zu "internieren" (wiederzuverwenden) mithilfe der `sys.intern()`-Funktion. Das Zeichenketten-Interning kann Speicher sparen, wenn Sie viele doppelte Zeichenketten in Ihrem Datensatz haben. Wenn Sie eine Zeichenkette internieren, überprüft Python, ob bereits eine identische Zeichenkette im Intern-Pool existiert. Wenn dies der Fall ist, gibt es eine Referenz auf das vorhandene Zeichenkettenobjekt zurück, anstatt ein neues zu erstellen.

Lassen Sie uns demonstrieren, wie das Zeichenketten-Interning mit einem einfachen Beispiel funktioniert:

```python
import sys

# Without interning
a = 'hello world'
b = 'hello world'
print(f"a is b (without interning): {a is b}")

# With interning
a = sys.intern(a)
b = sys.intern(b)
print(f"a is b (with interning): {a is b}")
```

In diesem Code erstellen we zunächst zwei Zeichenkettenvariablen `a` und `b` mit demselben Wert ohne Interning. Der `is`-Operator überprüft, ob zwei Variablen auf dasselbe Objekt verweisen. Ohne Interning sind `a` und `b` verschiedene Objekte, daher gibt `a is b` `False` zurück. Dann internieren wir beide Zeichenketten mit `sys.intern()`. Nach dem Interning verweisen `a` und `b` auf dasselbe Objekt im Intern-Pool, daher gibt `a is b` `True` zurück.

Die Ausgabe sollte sein:

```
a is b (without interning): False
a is b (with interning): True
```

Jetzt verwenden wir das Zeichenketten-Interning beim Lesen der CTA-Bus-Daten, um den Speicherverbrauch zu reduzieren. Wir verwenden auch das `tracemalloc`-Modul, um den Speicherverbrauch vor und nach dem Interning zu verfolgen.

```python
import sys
import reader
import tracemalloc

# Start memory tracking
tracemalloc.start()

# Read data with interning for the route column
rows = reader.read_csv_as_dicts('ctabus.csv', [sys.intern, str, str, int])

# Check unique route objects again
routeids = {id(row['route']) for row in rows}
print(f"Number of unique route string objects (with interning): {len(routeids)}")

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")
```

In diesem Code starten wir zunächst die Speicherüberwachung mit `tracemalloc.start()`. Dann lesen wir die CTA-Bus-Daten mit Interning für die Routenspalte, indem wir `sys.intern` als Datentyp für die erste Spalte übergeben. Danach überprüfen wir erneut die Anzahl der eindeutigen Routenzeichenkettenobjekte und geben den aktuellen und maximalen Speicherverbrauch aus.

Die Ausgabe sollte in etwa so aussehen:

```
Number of unique route string objects (with interning): 181
Current memory usage: 189.56 MB
Peak memory usage: 209.32 MB
```

Lassen Sie uns den Interpreter neu starten und versuchen, sowohl die Routen- als auch die Datumszeichenketten zu internieren, um zu sehen, ob wir den Speicherverbrauch weiter reduzieren können.

```python
exit()
```

Starten Sie Python erneut:

```bash
python3
```

```python
import sys
import reader
import tracemalloc

# Start memory tracking
tracemalloc.start()

# Read data with interning for both route and date columns
rows = reader.read_csv_as_dicts('ctabus.csv', [sys.intern, sys.intern, str, int])

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage (interning route and date): {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage (interning route and date): {peak / 1024 / 1024:.2f} MB")
```

Die Ausgabe sollte eine weitere Verringerung des Speicherverbrauchs zeigen:

```
Current memory usage (interning route and date): 170.23 MB
Peak memory usage (interning route and date): 190.05 MB
```

Dies zeigt, wie das Verständnis des Python-Speichermodells und die Verwendung von Techniken wie dem Zeichenketten-Interning helfen können, Ihre Programme zu optimieren, insbesondere wenn Sie mit großen Datensätzen mit wiederholten Werten arbeiten.

Schließlich beenden Sie den Python-Interpreter:

```python
exit()
```
