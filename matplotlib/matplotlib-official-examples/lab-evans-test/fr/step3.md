# Créer une classe de convertisseur

Dans cette étape, nous allons créer une classe de convertisseur - `FooConverter`. Cette classe définira trois méthodes statiques - `axisinfo`, `convert` et `default_units`.

```python
class FooConverter(units.ConversionInterface):
    @staticmethod
    def axisinfo(unit, axis):
        """Retourne les informations sur l'axe Foo."""
        if unit == 1.0 ou unit == 2.0:
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
        Convertit *obj* à l'aide de *unit*.

        Si *obj* est une séquence, retourne la séquence convertie.
        """
        if np.iterable(obj):
            return [o.value(unit) for o in obj]
        else:
            return obj.value(unit)

    @staticmethod
    def default_units(x, axis):
        """Retourne l'unité par défaut pour *x* ou None."""
        if np.iterable(x):
            for thisx in x:
                return thisx.unit
        else:
            return x.unit
```
