# Definieren der Größe und Farbe der Punkte

In diesem Schritt werden wir die Größe und die Farbe der Punkte in unserem Scatter Plot definieren. Wir werden die NumPy-Bibliothek verwenden, um Zufallswerte für die Größe und die Farbe der Punkte zu generieren.

```python
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2
```
