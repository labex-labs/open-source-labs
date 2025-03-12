# Verständnis der Übergabe von Funktionsargumenten

In Python sind Funktionen ein grundlegendes Konzept, das es Ihnen ermöglicht, eine Reihe von Anweisungen zusammenzufassen, um eine bestimmte Aufgabe auszuführen. Wenn Sie eine Funktion aufrufen, müssen Sie ihr oft einige Daten zur Verfügung stellen, die wir Argumente nennen. Python bietet verschiedene Möglichkeiten, diese Argumente an Funktionen zu übergeben. Diese Flexibilität ist unglaublich nützlich, da sie Ihnen hilft, saubereren und wartbareren Code zu schreiben. Bevor wir diese Techniken auf unser Projekt anwenden, schauen wir uns diese Argumentübergabekonventionen genauer an.

## Erstellen einer Sicherungskopie Ihrer Arbeit

Bevor wir mit den Änderungen an unserer `stock.py`-Datei beginnen, ist es eine gute Praxis, eine Sicherungskopie zu erstellen. Auf diese Weise können wir immer zurück zur ursprünglichen Version gehen, wenn etwas während unserer Experimente schief geht. Um eine Sicherungskopie zu erstellen, öffnen Sie ein Terminal und führen Sie den folgenden Befehl aus:

```bash
cp stock.py orig_stock.py
```

Dieser Befehl verwendet den `cp` (Kopieren)-Befehl im Terminal. Er nimmt die `stock.py`-Datei und erstellt eine Kopie davon mit dem Namen `orig_stock.py`. Auf diese Weise stellen wir sicher, dass unsere ursprüngliche Arbeit sicher aufbewahrt wird.

## Erkundung der Übergabe von Funktionsargumenten

In Python gibt es mehrere Möglichkeiten, Funktionen mit verschiedenen Argumenttypen aufzurufen. Lassen Sie uns jede dieser Methoden im Detail untersuchen.

### 1. Positionsabhängige Argumente

Die einfachste Art, Argumente an eine Funktion zu übergeben, ist die positionsabhängige Übergabe. Wenn Sie eine Funktion definieren, geben Sie eine Liste von Parametern an. Wenn Sie die Funktion aufrufen, stellen Sie Werte für diese Parameter in der gleichen Reihenfolge bereit, wie sie definiert sind.

Hier ist ein Beispiel:

```python
def calculate(x, y, z):
    return x + y + z

# Call with positional arguments
result = calculate(1, 2, 3)
print(result)  # Output: 6
```

In diesem Beispiel nimmt die `calculate`-Funktion drei Parameter entgegen: `x`, `y` und `z`. Wenn wir die Funktion mit `calculate(1, 2, 3)` aufrufen, wird der Wert `1` an `x` zugewiesen, `2` an `y` und `3` an `z`. Die Funktion addiert dann diese Werte und gibt das Ergebnis zurück.

### 2. Schlüsselwortargumente

Zusätzlich zu positionsabhängigen Argumenten können Sie auch Argumente anhand ihrer Namen angeben. Dies wird die Verwendung von Schlüsselwortargumenten genannt. Wenn Sie Schlüsselwortargumente verwenden, müssen Sie sich nicht um die Reihenfolge der Argumente kümmern.

Hier ist ein Beispiel:

```python
# Call with a mix of positional and keyword arguments
result = calculate(1, z=3, y=2)
print(result)  # Output: 6
```

In diesem Beispiel übergeben wir zunächst das positionsabhängige Argument `1` für `x`. Dann verwenden wir Schlüsselwortargumente, um die Werte für `y` und `z` anzugeben. Die Reihenfolge der Schlüsselwortargumente spielt keine Rolle, solange Sie die richtigen Namen angeben.

### 3. Entpacken von Sequenzen und Wörterbüchern

Python bietet eine bequeme Möglichkeit, Sequenzen und Wörterbücher als Argumente zu übergeben, indem Sie die `*`- und `**`-Syntax verwenden. Dies wird Entpacken genannt.

Hier ist ein Beispiel für das Entpacken eines Tupels in positionsabhängige Argumente:

```python
# Unpacking a tuple into positional arguments
args = (1, 2, 3)
result = calculate(*args)
print(result)  # Output: 6
```

In diesem Beispiel haben wir ein Tupel `args`, das die Werte `1`, `2` und `3` enthält. Wenn wir den `*`-Operator vor `args` im Funktionsaufruf verwenden, entpackt Python das Tupel und übergibt seine Elemente als positionsabhängige Argumente an die `calculate`-Funktion.

Hier ist ein Beispiel für das Entpacken eines Wörterbuchs in Schlüsselwortargumente:

```python
# Unpacking a dictionary into keyword arguments
kwargs = {'y': 2, 'z': 3}
result = calculate(1, **kwargs)
print(result)  # Output: 6
```

In diesem Beispiel haben wir ein Wörterbuch `kwargs`, das die Schlüssel-Wert-Paare `'y': 2` und `'z': 3` enthält. Wenn wir den `**`-Operator vor `kwargs` im Funktionsaufruf verwenden, entpackt Python das Wörterbuch und übergibt seine Schlüssel-Wert-Paare als Schlüsselwortargumente an die `calculate`-Funktion.

### 4. Akzeptieren von variablen Argumenten

Manchmal möchten Sie möglicherweise eine Funktion definieren, die eine beliebige Anzahl von Argumenten akzeptieren kann. Python ermöglicht Ihnen dies, indem Sie die `*`- und `**`-Syntax in der Funktionsdefinition verwenden.

Hier ist ein Beispiel für eine Funktion, die eine beliebige Anzahl von positionsabhängigen Argumenten akzeptiert:

```python
# Accept any number of positional arguments
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2))           # Output: 3
print(sum_all(1, 2, 3, 4, 5))  # Output: 15
```

In diesem Beispiel verwendet die `sum_all`-Funktion den Parameter `*args`, um eine beliebige Anzahl von positionsabhängigen Argumenten zu akzeptieren. Der `*`-Operator sammelt alle positionsabhängigen Argumente in einem Tupel namens `args`. Die Funktion verwendet dann die integrierte `sum`-Funktion, um alle Elemente im Tupel aufzusummieren.

Hier ist ein Beispiel für eine Funktion, die eine beliebige Anzahl von Schlüsselwortargumenten akzeptiert:

```python
# Accept any number of keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Python", year=1991)
# Output:
# name: Python
# year: 1991
```

In diesem Beispiel verwendet die `print_info`-Funktion den Parameter `**kwargs`, um eine beliebige Anzahl von Schlüsselwortargumenten zu akzeptieren. Der `**`-Operator sammelt alle Schlüsselwortargumente in einem Wörterbuch namens `kwargs`. Die Funktion iteriert dann über die Schlüssel-Wert-Paare im Wörterbuch und gibt sie aus.

Diese Techniken werden uns helfen, flexiblere und wiederverwendbare Code-Strukturen in den folgenden Schritten zu erstellen. Um uns mit diesen Konzepten vertrauter zu machen, öffnen wir den Python-Interpreter und probieren einige dieser Beispiele aus.

```bash
python3
```

Sobald Sie sich im Python-Interpreter befinden, versuchen Sie, die obigen Beispiele einzugeben. Dies gibt Ihnen praktische Erfahrung mit diesen Argumentübergabetechniken.
