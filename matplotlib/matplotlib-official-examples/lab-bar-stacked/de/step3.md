# Ein gestapeltes Balkendiagramm erstellen

Wir werden ein gestapeltes Balkendiagramm erstellen, indem wir `matplotlib.pyplot.bar` verwenden und durch jede Gewichtskategorie iterieren, um die Balken zu stapeln.

```python
fig, ax = plt.subplots()
bottom = np.zeros(3)

for boolean, weight_count in weight_counts.items():
    p = ax.bar(species, weight_count, width, label=boolean, bottom=bottom)
    bottom += weight_count

ax.set_title("Number of penguins with above average body mass")
ax.legend(loc="upper right")
```
