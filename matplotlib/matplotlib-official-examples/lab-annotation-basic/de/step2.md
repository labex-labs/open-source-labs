# Ein Diagramm erstellen

Als nächstes werden wir mit Matplotlib ein Diagramm erstellen. In diesem Beispiel werden wir die Kosinusfunktion über einen Wertebereich plotten.

```python
fig, ax = plt.subplots()

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = ax.plot(t, s, lw=2)
```
