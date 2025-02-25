# Definieren der Testfunktion

Als nächstes definieren wir eine Funktion, die die Ergebnisse eines Experiments repräsentiert. Diese Funktion wird verwendet, um die Testdatenpunkte zu generieren.

```python
def experiment_res(x, y):
    """Eine analytische Funktion, die die Experimentergebnisse repräsentiert."""
    x = 2 * x
    r1 = np.sqrt((0.5 - x)**2 + (0.5 - y)**2)
    theta1 = np.arctan2(0.5 - x, 0.5 - y)
    r2 = np.sqrt((-x - 0.2)**2 + (-y - 0.2)**2)
    theta2 = np.arctan2(-x - 0.2, -y - 0.2)
    z = (4 * (np.exp((r1/10)**2) - 1) * 30 * np.cos(3 * theta1) +
         (np.exp((r2/10)**2) - 1) * 30 * np.cos(5 * theta2) +
         2 * (x**2 + y**2))
    return (np.max(z) - z) / (np.max(z) - np.min(z))
```
