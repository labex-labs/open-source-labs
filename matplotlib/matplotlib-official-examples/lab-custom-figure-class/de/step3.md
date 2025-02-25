# Erstelle Daten für den Graphen

Erstelle einige Daten für den Graphen. In diesem Beispiel werden wir die `x`- und `y`-Arrays mit der `numpy`-Bibliothek erstellen.

```python
x = np.linspace(-3, 3, 201)
y = np.tanh(x) + 0.1 * np.cos(5 * x)
```
