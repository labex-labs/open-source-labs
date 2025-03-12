# Aufbau eines Validierungssystems mit Vererbung

In diesem Schritt werden wir ein praktisches Validierungssystem unter Verwendung von Vererbung aufbauen. Vererbung ist ein mächtiges Konzept in der Programmierung, das es Ihnen ermöglicht, neue Klassen auf der Grundlage bestehender zu erstellen. Auf diese Weise können Sie Code wiederverwenden und organisiertere und modularere Programme erstellen. Indem Sie dieses Validierungssystem aufbauen, werden Sie sehen, wie Vererbung eingesetzt werden kann, um wiederverwendbare Codekomponenten zu erstellen, die auf verschiedene Weise kombiniert werden können.

## Erstellen der Basisklasse für Validatoren

Zunächst müssen wir eine Basisklasse für unsere Validatoren erstellen. Dazu erstellen wir eine neue Datei in der WebIDE. So können Sie es machen: Klicken Sie auf "File" > "New File", oder verwenden Sie die Tastenkombination. Sobald die neue Datei geöffnet ist, benennen Sie sie `validate.py`.

Fügen wir nun etwas Code in diese Datei ein, um eine Basisklasse `Validator` zu erstellen. Diese Klasse wird als Grundlage für alle anderen Validatoren dienen.

```python
# validate.py
class Validator:
    @classmethod
    def check(cls, value):
        return value
```

In diesem Code haben wir eine `Validator`-Klasse mit einer `check`-Methode definiert. Die `check`-Methode nimmt einen Wert als Argument und gibt ihn unverändert zurück. Der `@classmethod`-Decorator wird verwendet, um diese Methode zu einer Klassenmethode zu machen. Das bedeutet, dass wir diese Methode direkt auf der Klasse aufrufen können, ohne eine Instanz der Klasse erstellen zu müssen.

## Hinzufügen von Typ-Validatoren

Als Nächstes fügen wir einige Validatoren hinzu, die den Typ eines Werts überprüfen. Diese Validatoren werden von der `Validator`-Klasse erben, die wir gerade erstellt haben. Gehen Sie zurück zur `validate.py`-Datei und fügen Sie den folgenden Code ein:

```python
class Typed(Validator):
    expected_type = object
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return super().check(value)

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str
```

Die `Typed`-Klasse ist eine Unterklasse von `Validator`. Sie hat ein `expected_type`-Attribut, das zunächst auf `object` gesetzt ist. Die `check`-Methode in der `Typed`-Klasse überprüft, ob der gegebene Wert vom erwarteten Typ ist. Wenn nicht, wird ein `TypeError` ausgelöst. Wenn der Typ korrekt ist, ruft sie die `check`-Methode der Elternklasse mit `super().check(value)` auf.

Die `Integer`-, `Float`- und `String`-Klassen erben von `Typed` und geben den genauen Typ an, den sie überprüfen sollen. Beispielsweise überprüft die `Integer`-Klasse, ob ein Wert eine Ganzzahl ist.

## Testen der Typ-Validatoren

Jetzt, da wir unsere Typ-Validatoren erstellt haben, lassen Sie uns sie testen. Öffnen Sie ein neues Terminal und starten Sie den Python-Interpreter, indem Sie den folgenden Befehl ausführen:

```bash
python3
```

Sobald der Python-Interpreter läuft, können wir unsere Validatoren importieren und testen. Hier ist ein Code, um sie zu testen:

```python
from validate import Integer, String

Integer.check(10)  # Should return 10

try:
    Integer.check('10')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")

String.check('10')  # Should return '10'
```

Wenn Sie diesen Code ausführen, sollten Sie etwas wie Folgendes sehen:

```
10
Error: Expected <class 'int'>
'10'
```

Wir können diese Validatoren auch in einer Funktion verwenden. Versuchen wir das:

```python
def add(x, y):
    Integer.check(x)
    Integer.check(y)
    return x + y

add(2, 2)  # Should return 4

try:
    add('2', '3')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")
```

Wenn Sie diesen Code ausführen, sollten Sie sehen:

```
4
Error: Expected <class 'int'>
```

## Hinzufügen von Wert-Validatoren

Bisher haben wir Validatoren erstellt, die den Typ eines Werts überprüfen. Jetzt fügen wir einige Validatoren hinzu, die den Wert selbst anstatt den Typ überprüfen. Gehen Sie zurück zur `validate.py`-Datei und fügen Sie den folgenden Code ein:

```python
class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        return super().check(value)

class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError('Must be non-empty')
        return super().check(value)
```

Der `Positive`-Validator überprüft, ob ein Wert nicht negativ ist. Wenn der Wert kleiner als 0 ist, wird ein `ValueError` ausgelöst. Der `NonEmpty`-Validator überprüft, ob ein Wert eine Länge ungleich Null hat. Wenn die Länge 0 ist, wird ein `ValueError` ausgelöst.

## Kombinieren von Validatoren mit multipler Vererbung

Jetzt werden wir unsere Validatoren unter Verwendung von multipler Vererbung kombinieren. Multiple Vererbung ermöglicht es einer Klasse, von mehr als einer Elternklasse zu erben. Gehen Sie zurück zur `validate.py`-Datei und fügen Sie den folgenden Code ein:

```python
class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

class NonEmptyString(String, NonEmpty):
    pass
```

Diese neuen Klassen kombinieren Typüberprüfung und Werteüberprüfung. Beispielsweise überprüft die `PositiveInteger`-Klasse, dass ein Wert sowohl eine Ganzzahl als auch nicht negativ ist. Die Reihenfolge der Vererbung spielt hier eine Rolle. Die Validatoren werden in der in der Klassendefinition angegebenen Reihenfolge überprüft.

## Testen der kombinierten Validatoren

Lassen Sie uns unsere kombinierten Validatoren testen. Im Python-Interpreter führen Sie den folgenden Code aus:

```python
from validate import PositiveInteger, PositiveFloat, NonEmptyString

PositiveInteger.check(10)  # Should return 10

try:
    PositiveInteger.check('10')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")

try:
    PositiveInteger.check(-10)  # Should raise ValueError
except ValueError as e:
    print(f"Error: {e}")

NonEmptyString.check('hello')  # Should return 'hello'

try:
    NonEmptyString.check('')  # Should raise ValueError
except ValueError as e:
    print(f"Error: {e}")
```

Wenn Sie diesen Code ausführen, sollten Sie sehen:

```
10
Error: Expected <class 'int'>
Error: Expected >= 0
'hello'
Error: Must be non-empty
```

Dies zeigt, wie wir Validatoren kombinieren können, um komplexere Validierungsregeln zu erstellen.

Wenn Sie mit dem Testen fertig sind, können Sie den Python-Interpreter beenden, indem Sie den folgenden Befehl ausführen:

```python
exit()
```
