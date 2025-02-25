# Daten plotten

Jetzt, nachdem wir unsere Teilplots erstellt haben, können wir unsere Daten mit `np.sin(x)` plotten.

```python
x = np.arange(0, 2*np.pi, 0.01)
ax0.plot(x, np.sin(x))
ax1.plot(x, np.sin(x))
```
