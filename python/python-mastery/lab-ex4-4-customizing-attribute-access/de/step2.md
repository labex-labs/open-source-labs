# Erstellen von schreibgeschützten Objekten mit Proxies

In diesem Schritt werden wir Proxy-Klassen untersuchen, ein sehr nützliches Muster in Python. Proxy-Klassen ermöglichen es Ihnen, ein vorhandenes Objekt zu nehmen und sein Verhalten zu ändern, ohne seinen ursprünglichen Code zu verändern. Dies ist wie das Umwickeln eines Objekts in eine spezielle Hülle, um neue Funktionen hinzuzufügen oder Einschränkungen zu setzen.

## Was ist ein Proxy?

Ein Proxy ist ein Objekt, das zwischen Ihnen und einem anderen Objekt steht. Es hat die gleichen Funktionen und Eigenschaften wie das ursprüngliche Objekt, kann aber zusätzliche Dinge tun. Beispielsweise kann es kontrollieren, wer auf das Objekt zugreifen kann, Aktionen protokollieren (Logging) oder andere nützliche Funktionen hinzufügen.

Lassen Sie uns einen schreibgeschützten Proxy erstellen. Dieser Proxy wird es Ihnen verhindern, die Attribute eines Objekts zu ändern.

### Schritt 1: Erstellen der schreibgeschützten Proxy-Klasse

Zunächst müssen wir eine Python-Datei erstellen, die unseren schreibgeschützten Proxy definiert.

1. Navigieren Sie zum Verzeichnis `/home/labex/project`.
2. Erstellen Sie in diesem Verzeichnis eine neue Datei namens `readonly_proxy.py`.
3. Öffnen Sie die Datei `readonly_proxy.py` und fügen Sie den folgenden Code hinzu:

```python
class ReadonlyProxy:
    def __init__(self, obj):
        # Store the wrapped object directly in __dict__ to avoid triggering __setattr__
        self.__dict__['_obj'] = obj

    def __getattr__(self, name):
        # Forward attribute access to the wrapped object
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        # Block all attribute assignments
        raise AttributeError("Cannot modify a read-only object")
```

In diesem Code wird die Klasse `ReadonlyProxy` definiert. Die `__init__`-Methode speichert das Objekt, das wir umwickeln möchten. Wir verwenden `self.__dict__`, um es direkt zu speichern, um die `__setattr__`-Methode nicht aufzurufen. Die `__getattr__`-Methode wird verwendet, wenn wir versuchen, auf ein Attribut des Proxys zuzugreifen. Sie leitet einfach die Anfrage an das umwickelte Objekt weiter. Die `__setattr__`-Methode wird aufgerufen, wenn wir versuchen, ein Attribut zu ändern. Sie löst einen Fehler aus, um jegliche Änderungen zu verhindern.

### Schritt 2: Erstellen einer Testdatei

Jetzt erstellen wir eine Testdatei, um zu sehen, wie unser schreibgeschützter Proxy funktioniert.

1. Erstellen Sie in demselben Verzeichnis `/home/labex/project` eine neue Datei namens `test_readonly.py`.
2. Fügen Sie der Datei `test_readonly.py` den folgenden Code hinzu:

```python
from stock import Stock
from readonly_proxy import ReadonlyProxy

# Create a normal Stock object
stock = Stock('AAPL', 100, 150.75)
print("Original stock object:")
print(f"Name: {stock.name}")
print(f"Shares: {stock.shares}")
print(f"Price: {stock.price}")
print(f"Cost: {stock.cost}")

# Modify the original stock object
stock.shares = 200
print(f"\nAfter modification - Shares: {stock.shares}")
print(f"After modification - Cost: {stock.cost}")

# Create a read-only proxy around the stock
readonly_stock = ReadonlyProxy(stock)
print("\nRead-only proxy object:")
print(f"Name: {readonly_stock.name}")
print(f"Shares: {readonly_stock.shares}")
print(f"Price: {readonly_stock.price}")
print(f"Cost: {readonly_stock.cost}")

# Try to modify the read-only proxy
try:
    print("\nAttempting to modify the read-only proxy...")
    readonly_stock.shares = 300
except AttributeError as e:
    print(f"Error: {e}")

# Show that the original object is unchanged
print(f"\nOriginal stock shares are still: {stock.shares}")
```

In diesem Testcode erstellen wir zunächst ein normales `Stock`-Objekt und geben seine Informationen aus. Dann ändern wir eines seiner Attribute und geben die aktualisierten Informationen aus. Als Nächstes erstellen wir einen schreibgeschützten Proxy für das `Stock`-Objekt und geben seine Informationen aus. Schließlich versuchen wir, den schreibgeschützten Proxy zu ändern und erwarten einen Fehler.

### Schritt 3: Ausführen des Testskripts

Nachdem wir die Proxy-Klasse und die Testdatei erstellt haben, müssen wir das Testskript ausführen, um die Ergebnisse zu sehen.

1. Öffnen Sie ein Terminal und navigieren Sie mit dem folgenden Befehl zum Verzeichnis `/home/labex/project`:

```bash
cd /home/labex/project
```

2. Führen Sie das Testskript mit dem folgenden Befehl aus:

```bash
python3 test_readonly.py
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
Original stock object:
Name: AAPL
Shares: 100
Price: 150.75
Cost: 15075.0

After modification - Shares: 200
After modification - Cost: 30150.0

Read-only proxy object:
Name: AAPL
Shares: 200
Price: 150.75
Cost: 30150.0

Attempting to modify the read-only proxy...
Error: Cannot modify a read-only object

Original stock shares are still: 200
```

## Wie der Proxy funktioniert

Die Klasse `ReadonlyProxy` verwendet zwei spezielle Methoden, um ihre schreibgeschützte Funktionalität zu erreichen:

1. `__getattr__(self, name)`: Diese Methode wird aufgerufen, wenn Python ein Attribut nicht auf die normale Weise finden kann. In unserer `ReadonlyProxy`-Klasse verwenden wir die `getattr()`-Funktion, um die Anfrage zum Zugriff auf das Attribut an das umwickelte Objekt weiterzuleiten. Wenn Sie also versuchen, auf ein Attribut des Proxys zuzugreifen, wird es tatsächlich das Attribut aus dem umwickelten Objekt abrufen.

2. `__setattr__(self, name, value)`: Diese Methode wird aufgerufen, wenn Sie versuchen, einem Attribut einen Wert zuzuweisen. In unserer Implementierung lösen wir einen `AttributeError` aus, um jegliche Änderungen an den Attributen des Proxys zu verhindern.

3. In der `__init__`-Methode ändern wir direkt `self.__dict__`, um das umwickelte Objekt zu speichern. Dies ist wichtig, denn wenn wir die normale Weise zur Zuweisung des Objekts verwenden würden, würde die `__setattr__`-Methode aufgerufen werden, die einen Fehler auslösen würde.

Dieses Proxy-Muster ermöglicht es uns, eine schreibgeschützte Schicht um jedes vorhandene Objekt hinzuzufügen, ohne seine ursprüngliche Klasse zu ändern. Das Proxy-Objekt verhält sich wie das umwickelte Objekt, lässt Sie aber keine Änderungen vornehmen.
