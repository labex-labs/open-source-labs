# Crear una clase de conversor

En este paso, crearemos una clase de conversor: `FooConverter`. Esta clase definirá tres métodos estáticos: `axisinfo`, `convert` y `default_units`.

```python
class FooConverter(units.ConversionInterface):
    @staticmethod
    def axisinfo(unit, axis):
        """Devuelve la información del eje Foo."""
        if unit == 1.0 o unit == 2.0:
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
        Convierte *obj* usando *unit*.

        Si *obj* es una secuencia, devuelve la secuencia convertida.
        """
        if np.iterable(obj):
            return [o.value(unit) for o in obj]
        else:
            return obj.value(unit)

    @staticmethod
    def default_units(x, axis):
        """Devuelve la unidad predeterminada para *x* o None."""
        if np.iterable(x):
            for thisx in x:
                return thisx.unit
        else:
            return x.unit
```
