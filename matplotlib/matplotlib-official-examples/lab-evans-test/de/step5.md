# Erstellen von Datenpunkten

In diesem Schritt werden wir einige Datenpunkte mit der benutzerdefinierten Einheitsklasse - `Foo` - erstellen.

```python
# create some Foos
x = [Foo(val, 1.0) for val in range(0, 50, 2)]
# and some arbitrary y data
y = [i for i in range(len(x))]
```
