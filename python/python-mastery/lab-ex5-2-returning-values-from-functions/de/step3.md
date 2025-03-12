# Arbeiten mit Futures für parallele Programmierung

In Python bietet die Sprache nützliche Werkzeuge wie Threads und Prozesse, wenn Sie Funktionen gleichzeitig oder parallel ausführen müssen. Hier aber liegt ein häufiges Problem: Wie können Sie den Wert erhalten, den eine Funktion zurückgibt, wenn sie in einem anderen Thread läuft? Hier kommt das Konzept eines `Future` (Zukunftswert) ins Spiel.

Ein `Future` ist wie ein Platzhalter für ein Ergebnis, das später verfügbar sein wird. Es ist eine Möglichkeit, einen Wert darzustellen, den eine Funktion in Zukunft produzieren wird, noch bevor die Funktion fertig gelaufen ist. Lassen Sie uns dieses Konzept anhand eines einfachen Beispiels besser verstehen.

### Schritt 1: Erstellen einer neuen Datei

Zunächst müssen Sie eine neue Python - Datei erstellen. Wir nennen sie `futures_demo.py`. Sie können den folgenden Befehl in Ihrem Terminal ausführen, um diese Datei zu erstellen:

```
touch ~/project/futures_demo.py
```

### Schritt 2: Hinzufügen des grundlegenden Funktionscodes

Öffnen Sie nun die Datei `futures_demo.py` und fügen Sie den folgenden Python - Code hinzu. Dieser Code definiert eine einfache Funktion und zeigt, wie ein normaler Funktionsaufruf funktioniert.

```python
import time
import threading
from concurrent.futures import Future, ThreadPoolExecutor

def worker(x, y):
    """A function that takes time to complete"""
    print('Starting work...')
    time.sleep(5)  # Simulate a time-consuming task
    print('Work completed')
    return x + y

# Part 1: Normal function call
print("--- Part 1: Normal function call ---")
result = worker(2, 3)
print(f"Result: {result}")
```

In diesem Code nimmt die Funktion `worker` zwei Zahlen, addiert sie, aber simuliert zuerst eine zeitintensive Aufgabe, indem sie für 5 Sekunden anhält. Wenn Sie diese Funktion auf normale Weise aufrufen, wartet das Programm, bis die Funktion fertig ist, und erhält dann den Rückgabewert.

### Schritt 3: Ausführen des grundlegenden Codes

Speichern Sie die Datei und führen Sie sie mit dem folgenden Befehl in Ihrem Terminal aus:

```
python ~/project/futures_demo.py
```

Sie sollten eine Ausgabe wie die folgende sehen:

```
--- Part 1: Normal function call ---
Starting work...
Work completed
Result: 5
```

Dies zeigt, dass ein normaler Funktionsaufruf wartet, bis die Funktion fertig ist, und dann das Ergebnis zurückgibt.

### Schritt 4: Ausführen der Funktion in einem separaten Thread

Schauen wir uns nun an, was passiert, wenn wir die Funktion `worker` in einem separaten Thread ausführen. Fügen Sie den folgenden Code zur Datei `futures_demo.py` hinzu:

```python
# Part 2: Running in a separate thread (problem: no way to get result)
print("\n--- Part 2: Running in a separate thread ---")
t = threading.Thread(target=worker, args=(2, 3))
t.start()
print("Main thread continues while worker runs...")
t.join()  # Wait for the thread to complete
print("Worker thread finished, but we don't have its return value!")
```

Hier verwenden wir die Klasse `threading.Thread`, um die Funktion `worker` in einem neuen Thread zu starten. Der Hauptthread wartet nicht, bis die Funktion `worker` fertig ist, sondern setzt seine Ausführung fort. Wenn der `worker` - Thread fertig ist, haben wir jedoch keine einfache Möglichkeit, den Rückgabewert zu erhalten.

### Schritt 5: Ausführen des threaded - Codes

Speichern Sie die Datei erneut und führen Sie sie mit demselben Befehl aus:

```
python ~/project/futures_demo.py
```

Sie werden bemerken, dass der Hauptthread weiterläuft, der `worker` - Thread läuft, aber wir nicht auf den Rückgabewert der Funktion `worker` zugreifen können.

### Schritt 6: Manuelles Verwenden eines `Future`

Um das Problem des Abrufs des Rückgabewerts aus einem Thread zu lösen, können wir ein `Future` - Objekt verwenden. Fügen Sie den folgenden Code zur Datei `futures_demo.py` hinzu:

```python
# Part 3: Using a Future to get the result
print("\n--- Part 3: Using a Future manually ---")

def do_work_with_future(x, y, future):
    """Wrapper that sets the result in the Future"""
    result = worker(x, y)
    future.set_result(result)

# Create a Future object
fut = Future()

# Start a thread that will set the result in the Future
t = threading.Thread(target=do_work_with_future, args=(2, 3, fut))
t.start()

print("Main thread continues...")
print("Waiting for the result...")
# Block until the result is available
result = fut.result()  # This will wait until set_result is called
print(f"Got the result: {result}")
```

In diesem Code erstellen wir ein `Future` - Objekt und übergeben es an eine neue Funktion `do_work_with_future`. Diese Funktion ruft die Funktion `worker` auf und setzt dann das Ergebnis im `Future` - Objekt. Der Hauptthread kann dann die Methode `result()` des `Future` - Objekts verwenden, um das Ergebnis zu erhalten, wenn es verfügbar ist.

### Schritt 7: Ausführen des Codes mit `Future`

Speichern Sie die Datei und führen Sie sie erneut aus:

```
python ~/project/futures_demo.py
```

Jetzt werden Sie sehen, dass wir erfolgreich den Rückgabewert aus der Funktion erhalten können, die im Thread läuft.

### Schritt 8: Verwenden von `ThreadPoolExecutor`

Die Klasse `ThreadPoolExecutor` in Python erleichtert die Arbeit mit parallelen Aufgaben noch weiter. Fügen Sie den folgenden Code zur Datei `futures_demo.py` hinzu:

```python
# Part 4: Using ThreadPoolExecutor (easier way)
print("\n--- Part 4: Using ThreadPoolExecutor ---")
with ThreadPoolExecutor() as executor:
    # Submit the work to the executor
    future = executor.submit(worker, 2, 3)

    print("Main thread continues after submitting work...")
    print("Checking if the future is done:", future.done())

    # Get the result (will wait if not ready)
    result = future.result()
    print("Now the future is done:", future.done())
    print(f"Final result: {result}")
```

Der `ThreadPoolExecutor` kümmert sich um die Erstellung und Verwaltung der `Future` - Objekte für Sie. Sie müssen nur die Funktion und ihre Argumente übermitteln, und er gibt ein `Future` - Objekt zurück, das Sie verwenden können, um das Ergebnis zu erhalten.

### Schritt 9: Ausführen des vollständigen Codes

Speichern Sie die Datei ein letztes Mal und führen Sie sie aus:

```
python ~/project/futures_demo.py
```

### Erklärung

1. **Normaler Funktionsaufruf**: Wenn Sie eine Funktion auf normale Weise aufrufen, wartet das Programm, bis die Funktion fertig ist, und erhält direkt den Rückgabewert.
2. **Thread - Problem**: Das Ausführen einer Funktion in einem separaten Thread hat einen Nachteil. Es gibt keine integrierte Möglichkeit, den Rückgabewert der Funktion zu erhalten, die in diesem Thread läuft.
3. **Manuelles Future**: Indem wir ein `Future` - Objekt erstellen und es an den Thread übergeben, können wir das Ergebnis im `Future` setzen und dann das Ergebnis aus dem Hauptthread abrufen.
4. **ThreadPoolExecutor**: Diese Klasse vereinfacht die parallele Programmierung. Sie kümmert sich um die Erstellung und Verwaltung der `Future` - Objekte für Sie, was es einfacher macht, Funktionen parallel auszuführen und ihre Rückgabewerte zu erhalten.

`Future` - Objekte haben mehrere nützliche Methoden:

- `result()`: Diese Methode wird verwendet, um das Ergebnis der Funktion zu erhalten. Wenn das Ergebnis noch nicht bereit ist, wird sie warten, bis es es ist.
- `done()`: Mit dieser Methode können Sie prüfen, ob die Berechnung der Funktion abgeschlossen ist.
- `add_done_callback()`: Mit dieser Methode können Sie eine Funktion registrieren, die aufgerufen wird, wenn das Ergebnis bereit ist.

Dieses Muster ist in der parallelen Programmierung sehr wichtig, insbesondere wenn Sie Ergebnisse von Funktionen erhalten müssen, die parallel laufen.
