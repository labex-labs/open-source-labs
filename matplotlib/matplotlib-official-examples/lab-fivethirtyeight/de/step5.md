# Plotten der Daten

In diesem Schritt werden wir die Daten auf dem Axes-Objekt mit der `plot`-Funktion von Matplotlib plotten. Wir werden sechs verschiedene Linien mit unterschiedlichen Steigungen und zufälligem Rauschen plotten.

```python
ax.plot(x, np.sin(x) + x + noise)
ax.plot(x, np.sin(x) + 0.5 * x + noise)
ax.plot(x, np.sin(x) + 2 * x + noise)
ax.plot(x, np.sin(x) - 0.5 * x + noise)
ax.plot(x, np.sin(x) - 2 * x + noise)
ax.plot(x, np.sin(x) + noise)
```
