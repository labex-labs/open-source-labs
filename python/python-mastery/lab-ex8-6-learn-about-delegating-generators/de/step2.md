# Verwendung von `yield from` in Koroutinen

In diesem Schritt werden wir untersuchen, wie das `yield from`-Statement in Verbindung mit Koroutinen für praktischere Anwendungen eingesetzt werden kann. Koroutinen sind ein leistungsstarkes Konzept in Python, und das Verständnis der Verwendung von `yield from` mit ihnen kann Ihren Code erheblich vereinfachen.

## Koroutinen und Nachrichtenübertragung

Koroutinen sind spezielle Funktionen, die Werte über die `yield`-Anweisung empfangen können. Sie sind äußerst nützlich für Aufgaben wie Datenverarbeitung und Ereignisbehandlung. In der Datei `cofollow.py` gibt es einen `consumer`-Decorator. Dieser Decorator hilft bei der Einrichtung von Koroutinen, indem er sie automatisch bis zum ersten `yield`-Punkt voranschreitet. Das bedeutet, dass Sie die Koroutine nicht manuell starten müssen; der Decorator erledigt dies für Sie.

Lassen Sie uns eine Koroutine erstellen, die Werte empfängt und deren Typen validiert. So können Sie es machen:

1. Öffnen Sie zunächst die Datei `cofollow.py` im Editor. Sie können den folgenden Befehl im Terminal verwenden, um in das richtige Verzeichnis zu navigieren:

```bash
cd /home/labex/project
```

2. Fügen Sie als Nächstes die folgende `receive`-Funktion am Ende der Datei `cofollow.py` hinzu. Diese Funktion ist eine Koroutine, die eine Nachricht empfängt und deren Typ validiert.

```python
def receive(expected_type):
    """
    A coroutine that receives a message and validates its type.
    Returns the received message if it matches the expected type.
    """
    msg = yield
    assert isinstance(msg, expected_type), f'Expected type {expected_type}'
    return msg
```

Was diese Funktion tut:

- Sie verwendet `yield` ohne Ausdruck, um einen Wert zu empfangen. Wenn der Koroutine ein Wert gesendet wird, wird dieser von der `yield`-Anweisung erfasst.
- Sie überprüft, ob der empfangene Wert vom erwarteten Typ ist, indem sie die `isinstance`-Funktion verwendet. Wenn der Typ nicht übereinstimmt, wird ein `AssertionError` ausgelöst.
- Wenn die Typüberprüfung erfolgreich ist, wird der Wert zurückgegeben.

3. Jetzt erstellen wir eine Koroutine, die `yield from` mit unserer `receive`-Funktion verwendet. Diese neue Koroutine wird nur Ganzzahlen empfangen und ausgeben.

```python
@consumer
def print_ints():
    """
    A coroutine that receives and prints integers only.
    Uses yield from to delegate to the receive coroutine.
    """
    while True:
        val = yield from receive(int)
        print('Got:', val)
```

4. Um diese Koroutine zu testen, öffnen Sie eine Python-Shell und führen Sie den folgenden Code aus:

```python
from cofollow import print_ints

p = print_ints()
p.send(42)
p.send(13)
try:
    p.send('13')  # This should raise an AssertionError
except AssertionError as e:
    print(f"Error: {e}")
```

Sie sollten die folgende Ausgabe sehen:

```
Got: 42
Got: 13
Error: Expected type <class 'int'>
```

## Verständnis der Funktionsweise von `yield from` mit Koroutinen

Wenn wir `yield from receive(int)` in der `print_ints`-Koroutine verwenden, erfolgen die folgenden Schritte:

1. Die Kontrolle wird an die `receive`-Koroutine delegiert. Das bedeutet, dass die `print_ints`-Koroutine anhält und die `receive`-Koroutine beginnt auszuführen.
2. Die `receive`-Koroutine verwendet `yield`, um einen Wert zu empfangen. Sie wartet darauf, dass ihr ein Wert gesendet wird.
3. Wenn ein Wert an `print_ints` gesendet wird, wird er tatsächlich von `receive` empfangen. Das `yield from`-Statement kümmert sich darum, den Wert von `print_ints` an `receive` zu übergeben.
4. Die `receive`-Koroutine validiert den Typ des empfangenen Werts. Wenn der Typ korrekt ist, wird der Wert zurückgegeben.
5. Der zurückgegebene Wert wird zum Ergebnis des `yield from`-Ausdrucks in der `print_ints`-Koroutine. Das bedeutet, dass die Variable `val` in `print_ints` den von `receive` zurückgegebenen Wert zugewiesen bekommt.

Die Verwendung von `yield from` macht den Code lesbarer als wenn wir das Yielding und Empfangen direkt handhaben müssten. Es abstrahiert die Komplexität des Wertetransfers zwischen Koroutinen.

## Erstellung fortschrittlicherer typprüfender Koroutinen

Lassen Sie uns unsere Hilfsfunktionen erweitern, um komplexere Typvalidierungen zu behandeln. So können Sie es machen:

1. Fügen Sie die folgenden Funktionen zur Datei `cofollow.py` hinzu:

```python
def receive_dict():
    """Receive and validate a dictionary"""
    result = yield from receive(dict)
    return result

def receive_str():
    """Receive and validate a string"""
    result = yield from receive(str)
    return result

@consumer
def process_data():
    """Process different types of data using the receive utilities"""
    while True:
        print("Waiting for a string...")
        name = yield from receive_str()
        print(f"Got string: {name}")

        print("Waiting for a dictionary...")
        data = yield from receive_dict()
        print(f"Got dictionary with {len(data)} items: {data}")

        print("Processing complete for this round.")
```

2. Um die neue Koroutine zu testen, öffnen Sie eine Python-Shell und führen Sie den folgenden Code aus:

```python
from cofollow import process_data

proc = process_data()
proc.send("John Doe")
proc.send({"age": 30, "city": "New York"})
proc.send("Jane Smith")
try:
    proc.send(123)  # This should raise an AssertionError
except AssertionError as e:
    print(f"Error: {e}")
```

Sie sollten eine Ausgabe wie diese sehen:

```
Waiting for a string...
Got string: John Doe
Waiting for a dictionary...
Got dictionary with 2 items: {'age': 30, 'city': 'New York'}
Processing complete for this round.
Waiting for a string...
Got string: Jane Smith
Waiting for a dictionary...
Error: Expected type <class 'dict'>
```

Das `yield from`-Statement macht den Code sauberer und lesbarer. Es ermöglicht es uns, uns auf die Hochschul-logik unseres Programms zu konzentrieren, anstatt uns in die Details der Nachrichtenübertragung zwischen Koroutinen zu verlieren.
