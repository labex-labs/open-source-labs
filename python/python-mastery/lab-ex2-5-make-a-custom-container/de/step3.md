# Optimierung des Speichers mit spaltenorientierten Daten

Bei der traditionellen Datenspeicherung speichern wir oft jeden Datensatz als separates Wörterbuch (Dictionary), was als zeilenorientierter Ansatz bezeichnet wird. Dieser Ansatz kann jedoch eine beträchtliche Menge an Speicher verbrauchen. Eine Alternative besteht darin, die Daten spaltenweise zu speichern. Im spaltenorientierten Ansatz erstellen wir für jedes Attribut eine separate Liste, und jede Liste enthält alle Werte für dieses spezifische Attribut. Dies kann uns helfen, Speicher zu sparen.

1. Zunächst müssen Sie in Ihrem Projektverzeichnis eine neue Python - Datei erstellen. Diese Datei wird den Code zum Lesen von Daten in spaltenorientierter Weise enthalten. Benennen Sie die Datei `readrides.py`. Sie können die folgenden Befehle im Terminal ausführen, um dies zu erreichen:

```bash
cd ~/project
touch readrides.py
```

Der Befehl `cd ~/project` wechselt das aktuelle Verzeichnis in Ihr Projektverzeichnis, und der Befehl `touch readrides.py` erstellt eine neue leere Datei namens `readrides.py`.

2. Öffnen Sie als Nächstes die Datei `readrides.py` im WebIDE - Editor. Fügen Sie dann den folgenden Python - Code in die Datei ein. Dieser Code definiert eine Funktion `read_rides_as_columns`, die Busfahrtdaten aus einer CSV - Datei liest und sie in vier separaten Listen speichert, wobei jede Liste eine Spalte der Daten darstellt.

```python
# readrides.py
import csv
import sys
import tracemalloc

def read_rides_as_columns(filename):
    '''
    Read the bus ride data into 4 lists, representing columns
    '''
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)
```

In diesem Code importieren wir zunächst die erforderlichen Module `csv`, `sys` und `tracemalloc`. Das Modul `csv` wird verwendet, um CSV - Dateien zu lesen, `sys` kann für systembezogene Operationen verwendet werden (wird in dieser Funktion jedoch nicht verwendet), und `tracemalloc` wird für die Speicheranalyse verwendet. Innerhalb der Funktion initialisieren wir vier leere Listen, um verschiedene Spalten der Daten zu speichern. Dann öffnen wir die Datei, überspringen die Kopfzeile und iterieren durch jede Zeile in der Datei, indem wir die entsprechenden Werte an die passenden Listen anhängen. Schließlich geben wir ein Wörterbuch zurück, das diese vier Listen enthält.

3. Analysieren wir nun, warum der spaltenorientierte Ansatz Speicher sparen kann. Wir tun dies in der Python - Shell. Führen Sie den folgenden Code aus:

```python
import readrides
import tracemalloc

# Estimate memory for row-oriented approach
nrows = 577563     # Number of rows in original file
dict_overhead = 240  # Approximate dictionary overhead in bytes
row_memory = nrows * dict_overhead
print(f"Estimated memory for row-oriented data: {row_memory} bytes ({row_memory/1024/1024:.2f} MB)")

# Estimate memory for column-oriented approach
pointer_size = 8   # Size of a pointer in bytes on 64-bit systems
column_memory = nrows * 4 * pointer_size  # 4 columns with one pointer per entry
print(f"Estimated memory for column-oriented data: {column_memory} bytes ({column_memory/1024/1024:.2f} MB)")

# Estimate savings
savings = row_memory - column_memory
print(f"Estimated memory savings: {savings} bytes ({savings/1024/1024:.2f} MB)")
```

In diesem Code importieren wir zunächst das gerade erstellte Modul `readrides` und das Modul `tracemalloc`. Dann schätzen wir den Speicherverbrauch für den zeilenorientierten Ansatz ab. Wir gehen davon aus, dass jedes Wörterbuch einen Overhead von 240 Bytes hat, und multiplizieren diesen mit der Anzahl der Zeilen in der ursprünglichen Datei, um den gesamten Speicherverbrauch für die zeilenorientierten Daten zu erhalten. Für den spaltenorientierten Ansatz gehen wir davon aus, dass auf einem 64 - Bit - System jeder Zeiger 8 Bytes benötigt. Da wir 4 Spalten haben und pro Eintrag einen Zeiger, berechnen wir den gesamten Speicherverbrauch für die spaltenorientierten Daten. Schließlich berechnen wir die Speichereinsparung, indem wir den Speicherverbrauch des spaltenorientierten Ansatzes vom Speicherverbrauch des zeilenorientierten Ansatzes subtrahieren.

Diese Berechnung zeigt, dass der spaltenorientierte Ansatz im Vergleich zum zeilenorientierten Ansatz mit Wörterbüchern etwa 120 MB Speicher sparen sollte.

4. Überprüfen wir dies, indem wir den tatsächlichen Speicherverbrauch mit dem Modul `tracemalloc` messen. Führen Sie den folgenden Code aus:

```python
# Start tracking memory
tracemalloc.start()

# Read the data
columns = readrides.read_rides_as_columns('ctabus.csv')

# Get current and peak memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current/1024/1024:.2f} MB")
print(f"Peak memory usage: {peak/1024/1024:.2f} MB")

# Stop tracking memory
tracemalloc.stop()
```

In diesem Code starten wir zunächst die Speicherüberwachung mit `tracemalloc.start()`. Dann rufen wir die Funktion `read_rides_as_columns` auf, um die Daten aus der Datei `ctabus.csv` zu lesen. Danach verwenden wir `tracemalloc.get_traced_memory()`, um den aktuellen und den maximalen Speicherverbrauch zu erhalten. Schließlich stoppen wir die Speicherüberwachung mit `tracemalloc.stop()`.

Die Ausgabe zeigt Ihnen den tatsächlichen Speicherverbrauch Ihrer spaltenorientierten Datenstruktur. Dieser sollte deutlich geringer sein als unsere theoretische Schätzung für den zeilenorientierten Ansatz.

Die erheblichen Speichereinsparungen resultieren aus der Eliminierung des Overheads von Tausenden von Wörterbuchobjekten. Jedes Wörterbuch in Python hat einen festen Overhead, unabhängig davon, wie viele Elemente es enthält. Durch die Verwendung der spaltenorientierten Speicherung benötigen wir nur wenige Listen anstelle von Tausenden von Wörterbüchern.
