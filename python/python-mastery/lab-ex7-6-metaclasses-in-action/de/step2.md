# Sammeln von Validator-Typen

In Python sind Validatoren Klassen, die uns helfen, sicherzustellen, dass Daten bestimmte Kriterien erfüllen. Unsere erste Aufgabe in diesem Experiment besteht darin, die Basisklasse `Validator` so zu modifizieren, dass sie alle ihre Unterklassen sammeln kann. Warum müssen wir das tun? Nun, indem wir alle Validator-Unterklassen sammeln, können wir einen Namensraum erstellen, der alle Validator-Typen enthält. Später werden wir diesen Namensraum in die `Structure`-Klasse einfügen, was es uns erleichtern wird, verschiedene Validatoren zu verwalten und zu verwenden.

Jetzt beginnen wir mit der Arbeit am Code. Öffnen Sie die Datei `validate.py`. Sie können den folgenden Befehl im Terminal verwenden, um sie zu öffnen:

```bash
code validate.py
```

Sobald die Datei geöffnet ist, müssen wir der `Validator`-Klasse ein Klassen-Level-Wörterbuch und eine `__init_subclass__()`-Methode hinzufügen. Das Klassen-Level-Wörterbuch wird verwendet, um alle Validator-Unterklassen zu speichern, und die `__init_subclass__()`-Methode ist eine spezielle Methode in Python, die jedes Mal aufgerufen wird, wenn eine Unterklasse der aktuellen Klasse definiert wird.

Fügen Sie den folgenden Code direkt nach der Klassendefinition der `Validator`-Klasse hinzu:

```python
# Add this to the Validator class in validate.py
validators = {}  # Dictionary to collect all validator subclasses

@classmethod
def __init_subclass__(cls):
    """Register each validator subclass in the validators dictionary"""
    Validator.validators[cls.__name__] = cls
```

Nachdem Sie den Code hinzugefügt haben, sollte Ihre modifizierte `Validator`-Klasse nun so aussehen:

```python
class Validator:
    validators = {}  # Dictionary to collect all validator subclasses

    @classmethod
    def __init_subclass__(cls):
        """Register each validator subclass in the validators dictionary"""
        Validator.validators[cls.__name__] = cls

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.name] = value

    def validate(self, value):
        pass
```

Jetzt wird jedes Mal, wenn ein neuer Validator-Typ definiert wird, wie `String` oder `PositiveInteger`, Python automatisch die `__init_subclass__()`-Methode aufrufen. Diese Methode fügt dann die neue Validator-Unterklasse dem `validators`-Wörterbuch hinzu, wobei der Klassenname als Schlüssel verwendet wird.

Lassen Sie uns testen, ob unser Code funktioniert. Wir erstellen ein einfaches Python-Skript, um den Inhalt des `validators`-Wörterbuchs zu überprüfen. Sie können den folgenden Befehl im Terminal ausführen:

```bash
python3 -c "from validate import Validator; print(Validator.validators)"
```

Wenn alles korrekt funktioniert, sollten Sie eine Ausgabe ähnlich der folgenden sehen, die alle Validator-Typen und ihre entsprechenden Klassen anzeigt:

```
{'Typed': <class 'validate.Typed'>, 'Positive': <class 'validate.Positive'>, 'NonEmpty': <class 'validate.NonEmpty'>, 'String': <class 'validate.String'>, 'Integer': <class 'validate.Integer'>, 'Float': <class 'validate.Float'>, 'PositiveInteger': <class 'validate.PositiveInteger'>, 'PositiveFloat': <class 'validate.PositiveFloat'>, 'NonEmptyString': <class 'validate.NonEmptyString'>}
```

Jetzt, da wir ein Wörterbuch haben, das alle unsere Validator-Typen enthält, können wir es im nächsten Schritt verwenden, um unsere Metaklasse zu erstellen.
