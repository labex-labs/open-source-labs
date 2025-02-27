# Zeichnen des Datensatzes

Jetzt zeichnen wir den zufällig generierten Mehrfachklassifizierungsdatensatz mit der Funktion `plot_2d`. Wir erstellen eine Figur mit zwei Teilplots und rufen für jeden Teilplot die Funktion `plot_2d` mit unterschiedlichen Parametern auf.

```python
_, (ax1, ax2) = plt.subplots(1, 2, sharex="row", sharey="row", figsize=(8, 4))
plt.subplots_adjust(bottom=0.15)

p_c, p_w_c = plot_2d(ax1, n_labels=1)
ax1.set_title("n_labels=1, length=50")
ax1.set_ylabel("Feature 1 count")

plot_2d(ax2, n_labels=3)
ax2.set_title("n_labels=3, length=50")
ax2.set_xlim(left=0, auto=True)
ax2.set_ylim(bottom=0, auto=True)

plt.show()
```
