# Ändere das Aussehen des Violindiagramms

Jetzt werden wir das Aussehen des Violindiagramms anpassen. Zunächst werden wir beschränken, was Matplotlib zeichnet, indem wir die Argumente `showmeans`, `showmedians` und `showextrema` auf `False` setzen. Anschließend werden wir die Farbe und die Transparenz der Violinkörper mit den Methoden `set_facecolor` und `set_alpha` ändern. Schließlich werden wir eine vereinfachte Darstellung eines Boxplots über dem Violindiagramm hinzufügen, indem wir die `percentile`-Funktion aus NumPy verwenden, um die Quartile, Medianen und Schnurrbögen zu berechnen.

```python
# customize violin plot appearance
fig, ax2 = plt.subplots()
ax2.set_title('Customized Violin Plot')
ax2.set_ylabel('Observed Values')

# create violin plot
parts = ax2.violinplot(
        data, showmeans=False, showmedians=False,
        showextrema=False)

# customize violin bodies
for pc in parts['bodies']:
    pc.set_facecolor('#D43F3A')
    pc.set_edgecolor('black')
    pc.set_alpha(1)

# add box plot
quartile1, medians, quartile3 = np.percentile(data, [25, 50, 75], axis=1)
whiskers = np.array([
    adjacent_values(sorted_array, q1, q3)
    for sorted_array, q1, q3 in zip(data, quartile1, quartile3)])
whiskers_min, whiskers_max = whiskers[:, 0], whiskers[:, 1]

inds = np.arange(1, len(medians) + 1)
ax2.scatter(inds, medians, marker='o', color='white', s=30, zorder=3)
ax2.vlines(inds, quartile1, quartile3, color='k', linestyle='-', lw=5)
ax2.vlines(inds, whiskers_min, whiskers_max, color='k', linestyle='-', lw=1)
```
