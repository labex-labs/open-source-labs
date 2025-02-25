# Selektives Markieren horizontaler Bereiche über die gesamte Achse

Der gleiche Auswahlmechanismus kann angewendet werden, um die volle vertikale Höhe der Achse zu füllen. Um unabhängig von den y-Grenzen zu sein, fügen wir eine Transformation hinzu, die die x-Werte in Datenkoordinaten und die y-Werte in Achsenkoordinaten interpretiert. Das folgende Beispiel markiert die Bereiche, in denen die y-Daten über einem angegebenen Schwellenwert liegen.

```python
fig, ax = plt.subplots()
x = np.arange(0, 4 * np.pi, 0.01)
y = np.sin(x)
ax.plot(x, y, color='black')

threshold = 0.75
ax.axhline(threshold, color='green', lw=2, alpha=0.7)
ax.fill_between(x, 0, 1, where=y > threshold,
                color='green', alpha=0.5, transform=ax.get_xaxis_transform())
```
