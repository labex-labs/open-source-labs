# Erstellen eines vertikalen gestapelten Balkendiagramms

Wir werden ein vertikales gestapeltes Balkendiagramm mit der `plt.bar`-Funktion erstellen, um die Verluste darzustellen, die durch verschiedene Naturkatastrophen in den vergangenen Jahren verursacht wurden. Wir werden eine for-Schleife verwenden, um über jede Zeile der Daten zu iterieren und die Balken zu zeichnen.

```python
n_rows = len(data)

index = np.arange(len(columns)) + 0.3
bar_width = 0.4

y_offset = np.zeros(len(columns))

cell_text = []
for row in range(n_rows):
    plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
    y_offset = y_offset + data[row]
    cell_text.append(['%1.1f' % (x / 1000.0) for x in y_offset])
```
