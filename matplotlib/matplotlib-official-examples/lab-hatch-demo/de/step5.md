# Ein Diagramm mit schraffierten Flächen erstellen

Du kannst auch Schraffierungen mit Flächen in deinem Diagramm verwenden. In diesem Fall werden wir die `fill_between`-Funktion verwenden, um eine schraffierte Fläche zu erstellen.

```python
x = np.arange(0, 40, 0.2)
plt.fill_between(x, np.sin(x) * 4 + 30, y2=0, hatch='///', zorder=2, fc='c')
```
