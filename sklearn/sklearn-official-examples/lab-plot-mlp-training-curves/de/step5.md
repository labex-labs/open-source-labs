# Zeichnen der Lernkurven für jeden Datensatz

Schließlich können wir die Lernkurven für jeden Datensatz mit der Funktion plot_on_dataset zeichnen. Wir werden ein 2x2-Grafik erstellen und jeden Datensatz auf einer separaten Achse zeichnen.

```python
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

for ax, data, name in zip(
    axes.ravel(), data_sets, ["iris", "digits", "circles", "moons"]
):
    plot_on_dataset(*data, ax=ax, name=name)

fig.legend(ax.get_lines(), labels, ncol=3, loc="upper center")
plt.show()
```