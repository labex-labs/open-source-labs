# Effiziente Klassengenerierung

Nachdem Sie nun verstehen, wie Sie Klassen mit der `type()`-Funktion erstellen können, werden wir uns eine effizientere Methode ansehen, um mehrere ähnliche Klassen zu generieren. Diese Methode spart Ihnen Zeit und reduziert Code-Duplizierung, wodurch Ihr Programmierungsprozess reibungsloser wird.

## Verständnis der bestehenden Validator-Klassen

Zunächst müssen wir die Datei `validate.py` im WebIDE öffnen. Diese Datei enthält bereits mehrere Validator-Klassen, die verwendet werden, um zu überprüfen, ob Werte bestimmten Bedingungen entsprechen. Zu diesen Klassen gehören `Validator`, `Positive`, `PositiveInteger` und `PositiveFloat`. Wir werden dieser Datei eine Basisklasse `Typed` und mehrere typspezifische Validatoren hinzufügen.

Um die Datei zu öffnen, führen Sie den folgenden Befehl im Terminal aus:

```bash
cd ~/project
```

## Hinzufügen der `Typed`-Validator-Klasse

Beginnen wir damit, die `Typed`-Validator-Klasse hinzuzufügen. Diese Klasse wird verwendet, um zu überprüfen, ob ein Wert den erwarteten Typ hat.

```python
class Typed(Validator):
    expected_type = object  # Default, will be overridden in subclasses

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        super().check(value)
```

In diesem Code ist `expected_type` standardmäßig auf `object` gesetzt. Subklassen werden dies mit dem spezifischen Typ überschreiben, den sie überprüfen. Die `check`-Methode verwendet die `isinstance`-Funktion, um zu überprüfen, ob der Wert den erwarteten Typ hat. Wenn nicht, wird ein `TypeError` ausgelöst.

Traditionell würden wir typspezifische Validatoren so erstellen:

```python
class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str
```

Dieser Ansatz ist jedoch wiederholend. Wir können es besser machen, indem wir den `type()`-Konstruktor verwenden, um diese Klassen dynamisch zu generieren.

## Dynamische Generierung von Typ-Validatoren

Wir ersetzen die einzelnen Klassendefinitionen durch einen effizienteren Ansatz.

```python
_typed_classes = [
    ('Integer', int),
    ('Float', float),
    ('String', str)
]

globals().update((name, type(name, (Typed,), {'expected_type': ty}))
                 for name, ty in _typed_classes)
```

Was dieser Code macht:

1. Er definiert eine Liste von Tupeln. Jedes Tupel enthält einen Klassennamen und den entsprechenden Python-Typ.
2. Er verwendet einen Generator-Ausdruck mit der `type()`-Funktion, um jede Klasse zu erstellen. Die `type()`-Funktion nimmt drei Argumente: den Klassennamen, ein Tupel von Basisklassen und ein Dictionary von Klassenattributen.
3. Er verwendet `globals().update()`, um die neu erstellten Klassen in den globalen Namensraum hinzuzufügen. Dadurch sind die Klassen im gesamten Modul zugänglich.

Ihre fertige `validate.py`-Datei sollte in etwa so aussehen:

```python
# Basic validator classes

class Validator:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.check(value)
        instance.__dict__[self.name] = value

    @classmethod
    def check(cls, value):
        pass

class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value <= 0:
            raise ValueError('Expected a positive value')
        super().check(value)

class PositiveInteger(Positive):
    @classmethod
    def check(cls, value):
        if not isinstance(value, int):
            raise TypeError('Expected an integer')
        super().check(value)

class PositiveFloat(Positive):
    @classmethod
    def check(cls, value):
        if not isinstance(value, float):
            raise TypeError('Expected a float')
        super().check(value)

class Typed(Validator):
    expected_type = object  # Default, will be overridden in subclasses

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        super().check(value)

# Generate type validators dynamically
_typed_classes = [
    ('Integer', int),
    ('Float', float),
    ('String', str)
]

globals().update((name, type(name, (Typed,), {'expected_type': ty}))
                 for name, ty in _typed_classes)
```

## Testen der dynamisch generierten Klassen

Jetzt testen wir unsere dynamisch generierten Validator-Klassen. Zunächst öffnen wir eine interaktive Python-Shell.

```bash
cd ~/project
python3
```

Sobald Sie sich in der Python-Shell befinden, importieren und testen Sie unsere Validatoren.

```python
from validate import Integer, Float, String

# Test the Integer validator
i = Integer()
i.__set_name__(None, 'test_int')
try:
    i.check("not an integer")
    print("Error: Check passed when it should have failed")
except TypeError as e:
    print(f"Integer validation: {e}")

# Test the String validator
s = String()
s.__set_name__(None, 'test_str')
try:
    s.check(123)
    print("Error: Check passed when it should have failed")
except TypeError as e:
    print(f"String validation: {e}")

# Add a new validator class to the list
import sys
print("Current validator classes:", [cls for cls in dir() if cls in ['Integer', 'Float', 'String']])
```

Sie sollten eine Ausgabe sehen, die die Typüberprüfungsfehler anzeigt. Dies zeigt, dass unsere dynamisch generierten Klassen korrekt funktionieren.

Wenn Sie mit dem Testen fertig sind, beenden Sie die Python-Shell:

```python
exit()
```

## Erweitern der dynamischen Klassengenerierung

Wenn Sie mehr Typ-Validatoren hinzufügen möchten, können Sie einfach die `_typed_classes`-Liste in `validate.py` aktualisieren.

```python
_typed_classes = [
    ('Integer', int),
    ('Float', float),
    ('String', str),
    ('List', list),
    ('Dict', dict),
    ('Bool', bool)
]
```

Dieser Ansatz bietet eine leistungsstarke und effiziente Möglichkeit, mehrere ähnliche Klassen zu generieren, ohne wiederholenden Code zu schreiben. Er ermöglicht es Ihnen, Ihre Anwendung einfach zu skalieren, wenn sich Ihre Anforderungen ändern.
