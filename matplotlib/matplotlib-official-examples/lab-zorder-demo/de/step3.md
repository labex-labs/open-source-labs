# Das Festlegen von zorder für Markierungen und Rasterlinien

Wir können die `set_axisbelow()`-Methode oder den `axes.axisbelow`-Parameter verwenden, um den `zorder` von Markierungen und Rasterlinien festzulegen.

```python
ax = plt.axes()
ax.plot([1, 2, 3], [2, 4, 3])
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')
```
