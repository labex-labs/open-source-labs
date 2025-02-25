# Erstellen einer Konverterklasse

In diesem Schritt werden wir eine Konverterklasse - `FooConverter` - erstellen. Diese Klasse wird drei statische Methoden definieren - `axisinfo`, `convert` und `default_units`.

```python
class FooConverter(units.ConversionInterface):
    @staticmethod
    def axisinfo(unit, axis):
        """Gibt die Foo AxisInfo zurück."""
        if unit == 1.0 oder unit == 2.0:
            return units.AxisInfo(
                majloc=ticker.IndexLocator(8, 0),
                majfmt=ticker.FormatStrFormatter("VAL: %s"),
                label='foo',
                )

        else:
            return None

    @staticmethod
    def convert(obj, unit, axis):
        """
        Konvertiert *obj* mit *unit*.

        Wenn *obj* eine Sequenz ist, gibt die konvertierte Sequenz zurück.
        """
        if np.iterable(obj):
            return [o.value(unit) for o in obj]
        else:
            return obj.value(unit)

    @staticmethod
    def default_units(x, axis):
        """Gibt die Standard-Einheit für *x* zurück oder None."""
        if np.iterable(x):
            for thisx in x:
                return thisx.unit
        else:
            return x.unit
```
