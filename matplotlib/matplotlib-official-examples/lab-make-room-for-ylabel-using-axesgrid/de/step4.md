# Erstellen einer Figur mit zwei Achsen

In diesem Schritt erstellen wir eine Figur mit zwei Achsen. Wir verwenden die `add_axes`-Methode, um zwei Achsen zur Figur hinzuzufügen. Wir legen auch die Y-Achsenbezeichnung für die erste Achse und den Titel für die zweite Achse fest.

```python
fig = plt.figure()
ax1 = fig.add_axes([0, 0, 1, 0.5])
ax2 = fig.add_axes([0, 0.5, 1, 0.5])

ax1.set_yticks([0.5], labels=["very long label"])
ax1.set_ylabel("Y label")

ax2.set_title("Title")
```
