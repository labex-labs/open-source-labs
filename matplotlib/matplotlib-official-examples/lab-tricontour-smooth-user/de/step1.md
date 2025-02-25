# Analytische Testfunktion

In diesem Schritt definieren wir eine analytische Testfunktion, die verwendet wird, um Z-Werte für die Triangulation zu generieren. Die Funktion heißt `function_z` und nimmt zwei Argumente, `x` und `y`, entgegen. Sie berechnet `z` basierend auf den Werten von `x` und `y` und gibt die normalisierten `z`-Werte zurück.

```python
def function_z(x, y):
    r1 = np.sqrt((0.5 - x)**2 + (0.5 - y)**2)
    theta1 = np.arctan2(0.5 - x, 0.5 - y)
    r2 = np.sqrt((-x - 0.2)**2 + (-y - 0.2)**2)
    theta2 = np.arctan2(-x - 0.2, -y - 0.2)
    z = -(2 * (np.exp((r1 / 10)**2) - 1) * 30. * np.cos(7. * theta1) +
          (np.exp((r2 / 10)**2) - 1) * 30. * np.cos(11. * theta2) +
          0.7 * (x**2 + y**2))
    return (np.max(z) - z) / (np.max(z) - np.min(z))
```
