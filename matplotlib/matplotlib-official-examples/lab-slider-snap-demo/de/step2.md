# Generiere Daten

In diesem Schritt wirst du die Daten generieren, die geplottet werden sollen. Du wirst eine Sinuswelle mit einer Frequenz von 3 Hz und einer Amplitude von 5 erstellen.

```python
t = np.arange(0.0, 1.0, 0.001)
a0 = 5
f0 = 3
s = a0 * np.sin(2 * np.pi * f0 * t)
```
