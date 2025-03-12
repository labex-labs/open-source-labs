# Beschränkung von Attributnamen

Derzeit erlaubt unsere `Structure`-Klasse die Festlegung beliebiger Attribute für ihre Instanzen. Für Anfänger mag dies zunächst bequem erscheinen, kann aber tatsächlich zu vielen Problemen führen. Wenn Sie mit einer Klasse arbeiten, erwarten Sie, dass bestimmte Attribute vorhanden sind und auf eine bestimmte Weise verwendet werden. Wenn Benutzer Attributnamen falsch schreiben oder versuchen, Attribute festzulegen, die nicht Teil des ursprünglichen Designs waren, kann dies zu Fehlern führen, die schwer zu finden sind.

## Die Notwendigkeit der Attributbeschränkung

Schauen wir uns ein einfaches Szenario an, um zu verstehen, warum wir Attributnamen beschränken müssen. Betrachten Sie den folgenden Code:

```python
s = Stock('GOOG', 100, 490.1)
s.shares = 50      # Correct attribute name
s.share = 60       # Typo in attribute name - creates a new attribute instead of updating
```

In der zweiten Zeile ist ein Tippfehler. Anstelle von `shares` haben wir `share` geschrieben. In Python wird anstelle eines Fehlers einfach ein neues Attribut namens `share` erstellt. Dies kann zu subtilen Fehlern führen, da Sie möglicherweise denken, dass Sie das `shares`-Attribut aktualisieren, aber tatsächlich erstellen Sie ein neues. Dies kann dazu führen, dass Ihr Code unerwartet verhält und sehr schwierig zu debuggen ist.

## Implementierung der Attributbeschränkung

Um dieses Problem zu lösen, können wir die `__setattr__`-Methode überschreiben. Diese Methode wird jedes Mal aufgerufen, wenn Sie versuchen, ein Attribut für ein Objekt festzulegen. Indem wir sie überschreiben, können wir steuern, welche Attribute festgelegt werden können und welche nicht.

Aktualisieren Sie Ihre `Structure`-Klasse in `structure.py` mit dem folgenden Code:

```python
def __setattr__(self, name, value):
    """
    Restrict attribute setting to only those defined in _fields
    or attributes starting with underscore (private attributes).
    """
    if name.startswith('_'):
        # Allow setting private attributes (starting with '_')
        super().__setattr__(name, value)
    elif name in self._fields:
        # Allow setting attributes defined in _fields
        super().__setattr__(name, value)
    else:
        # Raise an error for other attributes
        raise AttributeError(f'No attribute {name}')
```

So funktioniert diese Methode:

1. Wenn der Attributname mit einem Unterstrich (`_`) beginnt, wird er als privates Attribut angesehen. Private Attribute werden oft für interne Zwecke in einer Klasse verwendet. Wir erlauben die Festlegung dieser Attribute, da sie Teil der internen Implementierung der Klasse sind.
2. Wenn der Attributname in der `_fields`-Liste enthalten ist, bedeutet dies, dass es sich um eines der Attribute handelt, die im Klassenentwurf definiert sind. Wir erlauben die Festlegung dieser Attribute, da sie Teil des erwarteten Verhaltens der Klasse sind.
3. Wenn der Attributname keiner dieser Bedingungen entspricht, werfen wir einen `AttributeError`. Dies teilt dem Benutzer mit, dass er versucht, ein Attribut festzulegen, das in der Klasse nicht existiert.

## Testen der Attributbeschränkung

Nachdem wir die Attributbeschränkung implementiert haben, lassen Sie uns sie testen, um sicherzustellen, dass sie wie erwartet funktioniert. Erstellen Sie eine Datei namens `test_attributes.py` mit dem folgenden Code:

```python
# test_attributes.py
from structure import Stock

s = Stock('GOOG', 100, 490.1)

# This should work - valid attribute
print("Setting shares to 50")
s.shares = 50
print(f"Shares is now: {s.shares}")

# This should work - private attribute
print("\nSetting _internal_data")
s._internal_data = "Some data"
print(f"_internal_data is: {s._internal_data}")

# This should fail - invalid attribute
print("\nTrying to set an invalid attribute:")
try:
    s.share = 60  # Typo in attribute name
    print("This should not print")
except AttributeError as e:
    print(f"Error correctly caught: {e}")
```

Um den Test auszuführen, öffnen Sie Ihr Terminal und geben Sie den folgenden Befehl ein:

```bash
python3 test_attributes.py
```

Sie sollten die folgende Ausgabe sehen:

```
Setting shares to 50
Shares is now: 50

Setting _internal_data
_internal_data is: Some data

Trying to set an invalid attribute:
Error correctly caught: No attribute share
```

Diese Ausgabe zeigt, dass unsere Klasse nun versehentliche Attributfehler verhindert. Sie ermöglicht es uns, gültige Attribute und private Attribute festzulegen, wirft jedoch einen Fehler, wenn wir versuchen, ein ungültiges Attribut festzulegen.

## Der Wert der Attributbeschränkung

Die Beschränkung von Attributnamen ist sehr wichtig für die Schreibung von robustem und wartbarem Code. Hier ist warum:

1. Sie hilft, Tippfehler in Attributnamen zu erkennen. Wenn Sie einen Fehler beim Eingeben eines Attributnamens machen, wird der Code einen Fehler auslösen, anstatt ein neues Attribut zu erstellen. Dies erleichtert es, Fehler früh im Entwicklungsprozess zu finden und zu beheben.
2. Sie verhindert Versuche, Attribute festzulegen, die nicht im Klassenentwurf existieren. Dies stellt sicher, dass die Klasse wie beabsichtigt verwendet wird und dass der Code vorhersehbar verhält.
3. Sie vermeidet die versehentliche Erstellung neuer Attribute. Die Erstellung neuer Attribute kann zu unerwartetem Verhalten führen und den Code schwieriger zu verstehen und zu warten machen.

Durch die Beschränkung von Attributnamen machen wir unseren Code zuverlässiger und einfacher zu bearbeiten.
