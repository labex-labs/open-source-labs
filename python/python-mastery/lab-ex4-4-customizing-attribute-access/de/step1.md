# Verständnis von `__setattr__` für die Attributsteuerung

In Python gibt es spezielle Methoden, die es Ihnen ermöglichen, anzupassen, wie auf Attribute eines Objekts zugegriffen und diese modifiziert werden. Eine solche wichtige Methode ist `__setattr__()`. Diese Methode wird jedes Mal aufgerufen, wenn Sie versuchen, einem Attribut eines Objekts einen Wert zuzuweisen. Sie ermöglicht es Ihnen, den Prozess der Attributzuweisung fein abzustimmen.

## Was ist `__setattr__`?

Die Methode `__setattr__(self, name, value)` fungiert als Interceptor für alle Attributzuweisungen. Wenn Sie eine einfache Zuweisungsanweisung wie `obj.attr = value` schreiben, weist Python den Wert nicht einfach direkt zu. Stattdessen ruft es intern `obj.__setattr__("attr", value)` auf. Dieser Mechanismus gibt Ihnen die Möglichkeit zu entscheiden, was während der Attributzuweisung passieren soll.

Schauen wir uns nun ein praktisches Beispiel an, wie wir `__setattr__` verwenden können, um zu beschränken, welche Attribute in einer Klasse gesetzt werden können.

### Schritt 1: Erstellen einer neuen Datei

Öffnen Sie zunächst eine neue Datei in der WebIDE. Sie können dies tun, indem Sie auf das Menü "File" klicken und dann "New File" auswählen. Benennen Sie diese Datei `restricted_stock.py` und speichern Sie sie im Verzeichnis `/home/labex/project`. In dieser Datei wird die Klassendefinition enthalten sein, in der wir `__setattr__` verwenden, um die Attributzuweisung zu steuern.

### Schritt 2: Hinzufügen von Code zu `restricted_stock.py`

Fügen Sie den folgenden Code zur Datei `restricted_stock.py` hinzu. Dieser Code definiert eine Klasse `RestrictedStock`.

```python
class RestrictedStock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __setattr__(self, name, value):
        # Only allow specific attributes
        if name not in {'name', 'shares', 'price'}:
            raise AttributeError(f'Cannot set attribute {name}')

        # If attribute is allowed, set it using the parent method
        super().__setattr__(name, value)
```

In der `__init__`-Methode initialisieren wir das Objekt mit den Attributen `name`, `shares` und `price`. Die `__setattr__`-Methode prüft, ob der Name des zuzuweisenden Attributs in der Menge der erlaubten Attribute (`name`, `shares`, `price`) enthalten ist. Wenn dies nicht der Fall ist, wird ein `AttributeError` ausgelöst. Wenn das Attribut erlaubt ist, wird die `__setattr__`-Methode der Basisklasse verwendet, um das Attribut tatsächlich zu setzen.

### Schritt 3: Erstellen einer Testdatei

Erstellen Sie eine neue Datei namens `test_restricted.py` und fügen Sie den folgenden Code hinzu. Dieser Code wird die Funktionalität der Klasse `RestrictedStock` testen.

```python
from restricted_stock import RestrictedStock

# Create a new stock
stock = RestrictedStock('GOOG', 100, 490.1)

# Test accessing existing attributes
print(f"Name: {stock.name}")
print(f"Shares: {stock.shares}")
print(f"Price: {stock.price}")

# Test modifying an existing attribute
print("\nChanging shares to 75...")
stock.shares = 75
print(f"New shares value: {stock.shares}")

# Test setting an invalid attribute
try:
    print("\nTrying to set an invalid attribute 'share'...")
    stock.share = 50
except AttributeError as e:
    print(f"Error: {e}")
```

In diesem Code importieren wir zunächst die Klasse `RestrictedStock`. Dann erstellen wir eine Instanz der Klasse. Wir testen den Zugriff auf vorhandene Attribute, die Modifikation eines vorhandenen Attributs und versuchen schließlich, ein ungültiges Attribut zu setzen, um zu überprüfen, ob die `__setattr__`-Methode wie erwartet funktioniert.

### Schritt 4: Ausführen der Testdatei

Öffnen Sie ein Terminal in der WebIDE und führen Sie die folgenden Befehle aus, um die Datei `test_restricted.py` auszuführen:

```bash
cd /home/labex/project
python3 test_restricted.py
```

Nachdem Sie diese Befehle ausgeführt haben, sollten Sie eine Ausgabe ähnlich der folgenden sehen:

```
Name: GOOG
Shares: 100
Price: 490.1

Changing shares to 75...
New shares value: 75

Trying to set an invalid attribute 'share'...
Error: Cannot set attribute share
```

## Wie es funktioniert

Die `__setattr__`-Methode in unserer Klasse `RestrictedStock` funktioniert in folgenden Schritten:

1. Sie prüft zunächst, ob der Attributname in der Menge der erlaubten Attribute (`name`, `shares`, `price`) enthalten ist.
2. Wenn der Attributname nicht in der erlaubten Menge enthalten ist, wird ein `AttributeError` ausgelöst. Dies verhindert die Zuweisung von unerwünschten Attributen.
3. Wenn das Attribut erlaubt ist, wird `super().__setattr__()` verwendet, um das Attribut tatsächlich zu setzen. Dies stellt sicher, dass der normale Prozess der Attributzuweisung für die erlaubten Attribute stattfindet.

Diese Methode ist flexibler als die Verwendung von `__slots__`, wie wir es in früheren Beispielen gesehen haben. Während `__slots__` die Speichernutzung optimieren und Attribute einschränken kann, hat es Einschränkungen bei der Arbeit mit Vererbung und kann mit anderen Python-Funktionen in Konflikt geraten. Unser Ansatz mit `__setattr__` gibt uns ähnliche Kontrolle über die Attributzuweisung ohne einige dieser Einschränkungen.
