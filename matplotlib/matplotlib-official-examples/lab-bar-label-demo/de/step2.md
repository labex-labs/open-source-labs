# Beschriftung von vertikalen Balkendiagrammen

Wir beginnen mit der Erstellung eines vertikalen Balkendiagramms und der Beschriftung mit der `bar_label`-Funktion. Die Daten, die wir verwenden werden, sind die Anzahl der Pinguine nach Geschlecht, entnommen von https://allisonhorst.github.io/palmerpenguins/.

```python
species = ('Adelie', 'Chinstrap', 'Gentoo')
sex_counts = {
    'Male': np.array([73, 34, 61]),
    'Female': np.array([73, 34, 58]),
}
width = 0.6  # die Breite der Balken: kann auch eine len(x)-Sequenz sein

fig, ax = plt.subplots()
bottom = np.zeros(3)

for sex, sex_count in sex_counts.items():
    p = ax.bar(species, sex_count, width, label=sex, bottom=bottom)
    bottom += sex_count

    ax.bar_label(p, label_type='center')

ax.set_title('Number of penguins by sex')
ax.legend()

plt.show()
```
