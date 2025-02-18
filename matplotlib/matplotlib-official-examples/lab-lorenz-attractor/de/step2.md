# Die Lorenz-Funktion definieren

Wir definieren die Lorenz-Funktion, die drei Parameter entgegennimmt und ein Array mit drei Werten zurückgibt. Wir verwenden die Standardwerte `s = 10`, `r = 28` und `b = 2,667` für die Lorenz-Parameter.

```python
def lorenz(xyz, *, s=10, r=28, b=2.667):
    """
    Parameter
    ----------
    xyz : array-ähnlich, Form (3,)
       Punkt von Interesse im dreidimensionalen Raum.
    s, r, b : float
       Parameter, die den Lorenz-Attraktor definieren.

    Rückgabewerte
    -------
    xyz_dot : Array, Form (3,)
       Werte der partiellen Ableitungen des Lorenz-Attraktors an der Stelle *xyz*.
    """
    x, y, z = xyz
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return np.array([x_dot, y_dot, z_dot])
```
