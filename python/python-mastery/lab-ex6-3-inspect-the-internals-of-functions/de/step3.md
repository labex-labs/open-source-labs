# Anwendung der Funktionsuntersuchung in Klassen

Jetzt werden wir das, was wir über die Funktionsuntersuchung gelernt haben, nutzen, um die Implementierung einer Klasse zu verbessern. Die Funktionsuntersuchung ermöglicht es uns, in Funktionen hineinzuschauen und ihre Struktur zu verstehen, wie z.B. die Parameter, die sie akzeptieren. In diesem Fall werden wir es nutzen, um unseren Klassen-Code effizienter und fehlerunanfälliger zu gestalten. Wir werden eine `Structure`-Klasse modifizieren, damit sie automatisch die Feldnamen aus der Signatur der `__init__`-Methode erkennen kann.

## Verständnis der `Structure`-Klasse

Die Datei `structure.py` enthält eine `Structure`-Klasse. Diese Klasse fungiert als Basisklasse, was bedeutet, dass andere Klassen von ihr erben können, um strukturierte Datenobjekte zu erstellen. Derzeit müssen wir, um die Attribute der Objekte zu definieren, die von Klassen erstellt werden, die von `Structure` erben, eine Klassenvariable `_fields` festlegen.

Öffnen wir die Datei im Editor. Wir verwenden den folgenden Befehl, um in das Projektverzeichnis zu navigieren:

```bash
cd ~/project
```

Nachdem Sie diesen Befehl ausgeführt haben, können Sie die vorhandene `Structure`-Klasse in der Datei `structure.py` im WebIDE finden und anzeigen.

## Erstellung einer `Stock`-Klasse

Erstellen wir eine `Stock`-Klasse, die von der `Structure`-Klasse erbt. Vererbung bedeutet, dass die `Stock`-Klasse alle Funktionen der `Structure`-Klasse erhält und auch ihre eigenen hinzufügen kann. Fügen wir den folgenden Code ans Ende der Datei `structure.py` hinzu:

```python
class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    def __init__(self, name, shares, price):
        self._init()
```

Es gibt jedoch ein Problem mit diesem Ansatz. Wir müssen sowohl das `_fields`-Tupel als auch die `__init__`-Methode mit denselben Parameternamen definieren. Dies ist redundant, da wir im Wesentlichen dieselben Informationen zweimal schreiben. Wenn wir vergessen, eine der Definitionen zu aktualisieren, wenn wir die andere ändern, kann dies zu Fehlern führen.

## Hinzufügen einer `set_fields`-Klassenmethode

Um dieses Problem zu beheben, fügen wir der `Structure`-Klasse eine `set_fields`-Klassenmethode hinzu. Diese Methode wird automatisch die Feldnamen aus der Signatur der `__init__`-Methode erkennen. Hier ist der Code, den wir zur `Structure`-Klasse hinzufügen müssen:

```python
@classmethod
def set_fields(cls):
    # Get the signature of the __init__ method
    import inspect
    sig = inspect.signature(cls.__init__)

    # Get parameter names, skipping 'self'
    params = list(sig.parameters.keys())[1:]

    # Set _fields attribute on the class
    cls._fields = tuple(params)
```

Diese Methode verwendet das `inspect`-Modul, das ein leistungsstarkes Werkzeug in Python ist, um Informationen über Objekte wie Funktionen und Klassen zu erhalten. Zuerst erhält sie die Signatur der `__init__`-Methode. Dann extrahiert sie die Parameternamen, wobei sie den `self`-Parameter überspringt, da `self` ein spezieller Parameter in Python-Klassen ist, der auf die Instanz selbst verweist. Schließlich legt sie die Klassenvariable `_fields` mit diesen Parameternamen fest.

## Modifikation der `Stock`-Klasse

Jetzt, da wir die `set_fields`-Methode haben, können wir unsere `Stock`-Klasse vereinfachen. Ersetzen Sie den vorherigen Code der `Stock`-Klasse durch den folgenden:

```python
class Stock(Structure):
    def __init__(self, name, shares, price):
        self._init()

# Call set_fields to automatically set _fields from __init__
Stock.set_fields()
```

Auf diese Weise müssen wir das `_fields`-Tupel nicht manuell definieren. Die `set_fields`-Methode kümmert sich darum.

## Testen der modifizierten Klasse

Um sicherzustellen, dass unsere modifizierte Klasse korrekt funktioniert, erstellen wir ein einfaches Testskript. Erstellen Sie eine neue Datei namens `test_structure.py` und fügen Sie den folgenden Code hinzu:

```python
from structure import Stock

def test_stock():
    # Create a Stock object
    s = Stock(name='GOOG', shares=100, price=490.1)

    # Test string representation
    print(f"Stock representation: {s}")

    # Test attribute access
    print(f"Name: {s.name}")
    print(f"Shares: {s.shares}")
    print(f"Price: {s.price}")

    # Test attribute modification
    s.shares = 50
    print(f"Updated shares: {s.shares}")

    # Test attribute error
    try:
        s.share = 50  # Misspelled attribute
        print("Error: Did not raise AttributeError")
    except AttributeError as e:
        print(f"Correctly raised: {e}")

if __name__ == "__main__":
    test_stock()
```

Dieses Testskript erstellt ein `Stock`-Objekt, testet seine String-Darstellung, greift auf seine Attribute zu, modifiziert ein Attribut und versucht, auf ein falsch geschriebenes Attribut zuzugreifen, um zu überprüfen, ob es den richtigen Fehler auslöst.

Um das Testskript auszuführen, verwenden Sie den folgenden Befehl:

```bash
python3 test_structure.py
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
Stock representation: Stock('GOOG',100,490.1)
Name: GOOG
Shares: 100
Price: 490.1
Updated shares: 50
Correctly raised: No attribute share
```

## Wie es funktioniert

1. Die `set_fields`-Methode verwendet `inspect.signature()`, um die Parameternamen aus der `__init__`-Methode zu erhalten. Diese Funktion gibt uns detaillierte Informationen über die Parameter der `__init__`-Methode.
2. Sie legt dann automatisch die Klassenvariable `_fields` basierend auf diesen Parameternamen fest. So müssen wir die gleichen Parameternamen nicht an zwei verschiedenen Stellen schreiben.
3. Dies beseitigt die Notwendigkeit, sowohl `_fields` als auch `__init__` mit übereinstimmenden Parameternamen manuell zu definieren. Es macht unseren Code wartbarer, denn wenn wir die Parameter in der `__init__`-Methode ändern, werden die `_fields` automatisch aktualisiert.

Dieser Ansatz nutzt die Funktionsuntersuchung, um unseren Code wartbarer und fehlerunanfälliger zu machen. Es ist eine praktische Anwendung der Introspektionsfähigkeiten von Python, die es uns ermöglichen, Objekte zur Laufzeit zu untersuchen und zu modifizieren.
