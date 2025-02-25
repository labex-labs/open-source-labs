# Zufällige Daten generieren

In diesem Schritt werden wir Zufällige Daten für unseren Scatter Plot generieren. Wir werden mit der NumPy-Bibliothek 50 Datenpunkte für jede Variable generieren.

```python
np.random.seed(19680801)

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
```
