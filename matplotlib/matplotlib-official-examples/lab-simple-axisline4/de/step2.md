# Daten generieren

Als nächstes müssen wir unsere x- und y-Daten generieren. Für dieses Beispiel werden wir eine Sinuswelle generieren.

```python
xx = np.arange(0, 2*np.pi, 0.01)
yy = np.sin(xx)
```
