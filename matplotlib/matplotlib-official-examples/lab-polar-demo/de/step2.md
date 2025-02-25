# Daten generieren

Als nächstes müssen wir die Daten für das Liniendiagramm generieren. Wir werden die `numpy`-Bibliothek verwenden, um einen Array von Werten für `r` und `theta` zu generieren.

```python
r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r
```
