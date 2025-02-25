# Generieren von Beispiel-Daten

Wir werden einige Beispiel-Daten generieren, die wir verwenden, um unsere Diagramme zu zeichnen.

```python
# Create some fake data.
x1 = np.linspace(0.0, 5.0)
y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
x2 = np.linspace(0.0, 2.0)
y2 = np.cos(2 * np.pi * x2)
```
