# Implementierung einer abstrakten Basisklasse

In diesem Schritt werden wir die `TableFormatter`-Klasse mithilfe des `abc`-Moduls in Python in eine richtige abstrakte Basisklasse (ABC) umwandeln. Aber zunächst verstehen wir, was eine abstrakte Basisklasse ist und warum wir sie benötigen.

## Verständnis von abstrakten Basisklassen

Eine abstrakte Basisklasse ist ein spezieller Klassen-Typ in Python. Es ist eine Klasse, von der man direkt kein Objekt erstellen kann, das heißt, man kann sie nicht instanziieren. Der Hauptzweck einer abstrakten Basisklasse besteht darin, eine gemeinsame Schnittstelle für ihre Unterklassen zu definieren. Sie legt eine Reihe von Regeln fest, denen alle Unterklassen folgen müssen. Insbesondere erfordert sie, dass Unterklassen bestimmte Methoden implementieren.

Hier sind einige Schlüsselkonzepte zu abstrakten Basisklassen:

- Wir verwenden das `abc`-Modul in Python, um abstrakte Basisklassen zu erstellen.
- Methoden, die mit dem `@abstractmethod`-Decorator markiert sind, sind wie Regeln. Jede Unterklasse, die von einer abstrakten Basisklasse erbt, muss diese Methoden implementieren.
- Wenn Sie versuchen, ein Objekt einer Klasse zu erstellen, die von einer abstrakten Basisklasse erbt, aber nicht alle erforderlichen Methoden implementiert hat, wird Python einen Fehler auslösen.

Nachdem Sie die Grundlagen von abstrakten Basisklassen verstanden haben, sehen wir uns an, wie wir die `TableFormatter`-Klasse so modifizieren können, dass sie eine wird.

## Modifizieren der TableFormatter-Klasse

Öffnen Sie die Datei `tableformat.py`. Wir werden einige Änderungen an der `TableFormatter`-Klasse vornehmen, damit sie das `abc`-Modul verwendet und eine abstrakte Basisklasse wird.

1. Zunächst müssen wir die erforderlichen Elemente aus dem `abc`-Modul importieren. Fügen Sie die folgende Importanweisung oben in der Datei hinzu:

```python
# tableformat.py
from abc import ABC, abstractmethod
```

Diese Importanweisung bringt zwei wichtige Dinge mit sich: `ABC`, die Basisklasse für alle abstrakten Basisklassen in Python, und `abstractmethod`, ein Decorator, den wir verwenden werden, um Methoden als abstrakt zu markieren.

2. Als Nächstes werden wir die `TableFormatter`-Klasse modifizieren. Sie sollte von `ABC` erben, um eine abstrakte Basisklasse zu werden, und wir werden ihre Methoden mit dem `@abstractmethod`-Decorator als abstrakt markieren. So sollte die modifizierte Klasse aussehen:

```python
class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        pass

    @abstractmethod
    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        pass
```

Beachten Sie einige Dinge an dieser modifizierten Klasse:

- Die Klasse erbt jetzt von `ABC`, was bedeutet, dass sie offiziell eine abstrakte Basisklasse ist.
- Sowohl die `headings`- als auch die `row`-Methode sind mit `@abstractmethod` dekoriert. Dies teilt Python mit, dass jede Unterklasse von `TableFormatter` diese Methoden implementieren muss.
- Wir haben den `NotImplementedError` durch `pass` ersetzt. Der `@abstractmethod`-Decorator sorgt dafür, dass Unterklassen diese Methoden implementieren, sodass wir den `NotImplementedError` nicht mehr benötigen.

## Testen Ihrer abstrakten Basisklasse

Nachdem wir die `TableFormatter`-Klasse zu einer abstrakten Basisklasse gemacht haben, testen wir, ob sie korrekt funktioniert. Wir erstellen eine Datei namens `test_abc.py` mit dem folgenden Code:

```python
from tableformat import TableFormatter

# Test case 1: Define a class with a misspelled method
try:
    class NewFormatter(TableFormatter):
        def headers(self, headings):  # Misspelled 'headings'
            pass
        def row(self, rowdata):
            pass

    f = NewFormatter()
    print("Test 1 failed - abstract method enforcement not working")
except TypeError as e:
    print(f"Test 1 passed - caught error: {e}")

# Test case 2: Define a class that properly implements all methods
try:
    class ProperFormatter(TableFormatter):
        def headings(self, headers):
            pass
        def row(self, rowdata):
            pass

    f = ProperFormatter()
    print("Test 2 passed - proper implementation works")
except TypeError as e:
    print(f"Test 2 failed - error: {e}")
```

In diesem Code haben wir zwei Testfälle. Der erste Testfall definiert eine Klasse `NewFormatter`, die versucht, von `TableFormatter` zu erben, aber einen falsch geschriebenen Methodennamen hat. Der zweite Testfall definiert eine Klasse `ProperFormatter`, die alle erforderlichen Methoden korrekt implementiert.

Um den Test auszuführen, öffnen Sie Ihr Terminal und führen Sie den folgenden Befehl aus:

```bash
python test_abc.py
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
Test 1 passed - caught error: Can't instantiate abstract class NewFormatter with abstract methods headings
Test 2 passed - proper implementation works
```

Diese Ausgabe bestätigt, dass unsere abstrakte Basisklasse wie erwartet funktioniert. Der erste Testfall schlägt fehl, weil die `NewFormatter`-Klasse die `headings`-Methode nicht korrekt implementiert hat. Der zweite Testfall schlägt fehl, weil die `ProperFormatter`-Klasse alle erforderlichen Methoden implementiert hat.
