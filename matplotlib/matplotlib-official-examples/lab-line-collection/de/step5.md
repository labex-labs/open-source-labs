# Farben auf Werte abbilden

Wir können auch ein Array von Werten auf Farben abbilden, indem wir die `ScalarMappable.set_array`-Funktion verwenden. Wir werden einen neuen Datensatz und ein neues `LineCollection`-Objekt erstellen, wobei der `array`-Parameter auf die `x`-Werte gesetzt ist. Anschließend können wir die `colorbar`-Methode des `Figure`-Objekts verwenden, um eine Farbskala zum Diagramm hinzuzufügen.

```python
N = 50
x = np.arange(N)
ys = [x + i for i in x]
segs = [np.column_stack([x, y]) for y in ys]

fig, ax = plt.subplots()
ax.set_xlim(np.min(x), np.max(x))
ax.set_ylim(np.min(ys), np.max(ys))

line_segments = LineCollection(segs, array=x,
                               linewidths=(0.5, 1, 1.5, 2),
                               linestyles='solid')
ax.add_collection(line_segments)
axcb = fig.colorbar(line_segments)
axcb.set_label('Line Number')
ax.set_title('Line Collection with mapped colors')
plt.sci(line_segments)
plt.show()
```
