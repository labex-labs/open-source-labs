# Das `yield from`-Statement verstehen

In diesem Schritt werden wir das `yield from`-Statement in Python untersuchen. Dieses Statement ist ein leistungsstarkes Werkzeug, wenn man mit Generatoren arbeitet, und es vereinfacht den Prozess der Delegierung von Operationen an andere Generatoren. Am Ende dieses Schritts werden Sie verstehen, was `yield from` ist, wie es funktioniert und wie es den Wertetransfer zwischen verschiedenen Generatoren handhaben kann.

## Was ist `yield from`?

Das `yield from`-Statement wurde in Python 3.3 eingeführt. Sein Hauptzweck ist es, die Delegierung von Operationen an Subgeneratoren zu vereinfachen. Ein Subgenerator ist einfach ein anderer Generator, an den ein Hauptgenerator die Arbeit delegieren kann.

Normalerweise, wenn Sie möchten, dass ein Generator Werte von einem anderen Generator ausgibt, müssen Sie eine Schleife verwenden. Beispielsweise würden Sie ohne `yield from` Code wie diesen schreiben:

```python
def delegating_generator():
    for value in subgenerator():
        yield value
```

In diesem Code verwendet der `delegating_generator` eine `for`-Schleife, um über die von `subgenerator` erzeugten Werte zu iterieren und dann jeden Wert nacheinander auszugeben.

Mit dem `yield from`-Statement wird der Code jedoch viel einfacher:

```python
def delegating_generator():
    yield from subgenerator()
```

Diese einzelne Codezeile erreicht dasselbe Ergebnis wie die Schleife im vorherigen Beispiel. Aber `yield from` ist nicht nur eine Abkürzung. Es verwaltet auch die bidirektionale Kommunikation zwischen dem Aufrufer und dem Subgenerator. Das bedeutet, dass alle an den delegierenden Generator gesendeten Werte direkt an den Subgenerator weitergeleitet werden.

## Ein einfaches Beispiel

Lassen Sie uns ein einfaches Beispiel erstellen, um zu sehen, wie `yield from` in der Praxis funktioniert.

1. Zunächst müssen wir die Datei `cofollow.py` im Editor öffnen. Dazu verwenden wir den Befehl `cd`, um in das richtige Verzeichnis zu navigieren. Führen Sie den folgenden Befehl im Terminal aus:

```bash
cd /home/labex/project
```

2. Als Nächstes fügen wir zwei Funktionen zur Datei `cofollow.py` hinzu. Die Funktion `subgen` ist ein einfacher Generator, der die Zahlen von 0 bis 4 ausgibt. Die Funktion `main_gen` verwendet `yield from`, um die Generierung dieser Zahlen an `subgen` zu delegieren und gibt dann die Zeichenkette `'Done'` aus. Fügen Sie den folgenden Code ans Ende der Datei `cofollow.py` hinzu:

```python
def subgen():
    for i in range(5):
        yield i

def main_gen():
    yield from subgen()
    yield 'Done'
```

3. Jetzt testen wir diese Funktionen. Öffnen Sie eine Python-Shell und führen Sie den folgenden Code aus:

```python
from cofollow import subgen, main_gen

# Test subgen directly
for x in subgen():
    print(x)

# Test main_gen that delegates to subgen
for x in main_gen():
    print(x)
```

Wenn Sie diesen Code ausführen, sollten Sie die folgende Ausgabe sehen:

```
0
1
2
3
4

0
1
2
3
4
Done
```

Diese Ausgabe zeigt, dass `yield from` es `main_gen` ermöglicht, alle von `subgen` erzeugten Werte direkt an den Aufrufer zu übergeben.

## Wertetransfer mit `yield from`

Eines der leistungsstärksten Merkmale von `yield from` ist seine Fähigkeit, den Wertetransfer in beide Richtungen zu handhaben. Lassen Sie uns ein komplexeres Beispiel erstellen, um dies zu demonstrieren.

1. Fügen Sie die folgenden Funktionen zur Datei `cofollow.py` hinzu:

```python
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

def caller():
    acc = accumulator()
    yield from acc
    yield 'Total accumulated'
```

Die Funktion `accumulator` ist eine Koroutine, die einen laufenden Gesamtwert verfolgt. Sie gibt den aktuellen Gesamtwert aus und wartet dann auf die Eingabe eines neuen Werts. Wenn sie `None` erhält, beendet sie die Schleife. Die Funktion `caller` erstellt eine Instanz von `accumulator` und verwendet `yield from`, um alle Sende- und Empfangsoperationen an sie zu delegieren.

2. Testen Sie diese Funktionen in einer Python-Shell:

```python
from cofollow import caller

c = caller()
print(next(c))  # Start the coroutine
print(c.send(1))  # Send value 1, get accumulated value
print(c.send(2))  # Send value 2, get accumulated value
print(c.send(3))  # Send value 3, get accumulated value
print(c.send(None))  # Send None to exit the accumulator
```

Wenn Sie diesen Code ausführen, sollten Sie die folgende Ausgabe sehen:

```
0
1
3
6
'Total accumulated'
```

Diese Ausgabe zeigt, dass `yield from` alle Sende- und Empfangsoperationen vollständig an den Subgenerator delegiert, bis dieser erschöpft ist.

Nachdem Sie nun die Grundlagen von `yield from` verstanden haben, werden wir im nächsten Schritt zu praktischeren Anwendungen übergehen.
