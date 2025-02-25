# Erstellen einer benutzerdefinierten Einheitsklasse

In diesem Schritt werden wir eine benutzerdefinierte Einheitsklasse - `Foo` - erstellen. Diese Klasse wird die Umwandlung und verschiedene Tick-Formatierungen je nach "Einheit" unterstützen. Hierbei ist die "Einheit" einfach ein skalarer Umrechnungsfaktor.

```python
class Foo:
    def __init__(self, val, unit=1.0):
        self.unit = unit
        self._val = val * unit

    def value(self, unit):
        if unit is None:
            unit = self.unit
        return self._val / unit
```
