# Behandlung von Ausnahmen in Generatoren

In diesem Schritt werden wir lernen, wie man Ausnahmen in Generatoren und Koroutinen behandelt. Zunächst aber verstehen wir, was Ausnahmen sind. Eine Ausnahme ist ein Ereignis, das während der Ausführung eines Programms auftritt und den normalen Ablauf der Programm-Anweisungen unterbricht. In Python können wir die Methode `throw()` verwenden, um Ausnahmen in Generatoren und Koroutinen zu behandeln.

## Verständnis von Koroutinen

Eine Koroutine ist eine spezielle Art von Generator. Im Gegensatz zu normalen Generatoren, die hauptsächlich Werte ausgeben, können Koroutinen sowohl Werte verbrauchen (mit der Methode `send()`) als auch Werte ausgeben. Die Datei `cofollow.py` enthält eine einfache Implementierung einer Koroutine.

Öffnen wir die Datei `cofollow.py` im WebIDE-Editor. Hier ist der Code darin:

```python
def consumer(func):
    def start(*args,**kwargs):
        c = func(*args,**kwargs)
        next(c)
        return c
    return start

@consumer
def printer():
    while True:
        item = yield
        print(item)
```

Jetzt zerlegen wir diesen Code. Der `consumer` ist ein Dekorator. Ein Dekorator ist eine Funktion, die eine andere Funktion als Argument nimmt, ihr einige Funktionen hinzufügt und dann die modifizierte Funktion zurückgibt. In diesem Fall bewegt der `consumer`-Dekorator den Generator automatisch zur ersten `yield`-Anweisung. Dies ist wichtig, da es den Generator darauf vorbereitet, Werte zu empfangen.

Die Koroutine `printer()` wird mit dem `@consumer`-Dekorator definiert. Innerhalb der Funktion `printer()` haben wir eine unendliche `while`-Schleife. Die Anweisung `item = yield` ist der Punkt, an dem die Magie geschieht. Sie pausiert die Ausführung der Koroutine und wartet darauf, einen Wert zu empfangen. Wenn ein Wert an die Koroutine gesendet wird, wird die Ausführung fortgesetzt und der empfangene Wert wird ausgegeben.

## Hinzufügen von Ausnahmebehandlung zur Koroutine

Jetzt werden wir die Koroutine `printer()` modifizieren, um Ausnahmen zu behandeln. Wir werden die Funktion `printer()` in `cofollow.py` wie folgt aktualisieren:

```python
@consumer
def printer():
    while True:
        try:
            item = yield
            print(item)
        except Exception as e:
            print('ERROR: %r' % e)
```

Der `try`-Block enthält den Code, der eine Ausnahme auslösen könnte. In unserem Fall ist es der Code, der den Wert empfängt und ausgibt. Wenn in dem `try`-Block eine Ausnahme auftritt, springt die Ausführung zum `except`-Block. Der `except`-Block fängt die Ausnahme auf und gibt eine Fehlermeldung aus. Nach diesen Änderungen speichern wir die Datei.

## Experimentieren mit Ausnahmebehandlung in Koroutinen

Fangen wir an, zu experimentieren, indem wir Ausnahmen in die Koroutine werfen. Öffnen Sie ein Terminal und starten Sie den Python-Interpreter mit den folgenden Befehlen:

```bash
cd ~/project
python3
```

### Experiment 1: Grundlegende Verwendung einer Koroutine

```python
>>> from cofollow import printer
>>> p = printer()
>>> p.send('hello')  # Send a value to the coroutine
hello
>>> p.send(42)  # Send another value
42
```

Hier importieren wir zunächst die Koroutine `printer` aus dem Modul `cofollow`. Dann erstellen wir eine Instanz der Koroutine `printer` namens `p`. Wir verwenden die Methode `send()`, um Werte an die Koroutine zu senden. Wie Sie sehen können, verarbeitet die Koroutine die von uns gesendeten Werte ohne Probleme.

### Experiment 2: Werfen einer Ausnahme in die Koroutine

```python
>>> p.throw(ValueError('It failed'))  # Throw an exception into the coroutine
ERROR: ValueError('It failed')
```

In diesem Experiment verwenden wir die Methode `throw()`, um eine `ValueError`-Ausnahme in die Koroutine einzufügen. Der `try-except`-Block in der Koroutine `printer()` fängt die Ausnahme auf und gibt eine Fehlermeldung aus. Dies zeigt, dass unsere Ausnahmebehandlung wie erwartet funktioniert.

### Experiment 3: Werfen einer echten Ausnahme in die Koroutine

```python
>>> try:
...     int('n/a')  # This will raise a ValueError
... except ValueError as e:
...     p.throw(e)  # Throw the caught exception into the coroutine
...
ERROR: ValueError("invalid literal for int() with base 10: 'n/a'")
```

Hier versuchen wir zunächst, die Zeichenkette `'n/a'` in eine Ganzzahl umzuwandeln, was eine `ValueError`-Ausnahme auslöst. Wir fangen diese Ausnahme auf und verwenden dann die Methode `throw()`, um sie an die Koroutine zu übergeben. Die Koroutine fängt die Ausnahme auf und gibt die Fehlermeldung aus.

### Experiment 4: Überprüfen, dass die Koroutine weiterhin läuft

```python
>>> p.send('still working')  # The coroutine continues to run after handling exceptions
still working
```

Nachdem die Ausnahmen behandelt wurden, senden wir einen weiteren Wert an die Koroutine mit der Methode `send()`. Die Koroutine ist immer noch aktiv und kann den neuen Wert verarbeiten. Dies zeigt, dass unsere Koroutine auch nach dem Auftreten von Fehlern weiterhin laufen kann.

## Wichtige Erkenntnisse

1. Generatoren und Koroutinen können Ausnahmen am Punkt der `yield`-Anweisung behandeln. Dies bedeutet, dass wir Fehler fangen und behandeln können, die auftreten, wenn die Koroutine auf einen Wert wartet oder ihn verarbeitet.
2. Die Methode `throw()` ermöglicht es Ihnen, Ausnahmen in einen Generator oder eine Koroutine einzufügen. Dies ist nützlich für Tests und für die Behandlung von Fehlern, die außerhalb der Koroutine auftreten.
3. Die richtige Behandlung von Ausnahmen in Generatoren ermöglicht es Ihnen, robuste, fehlertolerante Generatoren zu erstellen, die auch bei Fehlern weiterhin laufen können. Dies macht Ihren Code zuverlässiger und einfacher zu warten.

Um den Python-Interpreter zu beenden, können Sie `exit()` eingeben oder `Strg+D` drücken.
