# Erstellen einer Figur mit zwei anpassbaren Achsen

In diesem Schritt erstellen wir eine Figur mit zwei anpassbaren Achsen. Wir verwenden die `make_axes_locatable`-Methode, um einen Divider zu erstellen, der es ermöglicht, die Achsen anzupassen. Wir fügen eine neue Achse rechts von der ersten Achse hinzu, indem wir die `append_axes`-Methode verwenden.

```python
fig = plt.figure()
ax1 = fig.add_axes([0, 0, 1, 1])
divider = make_axes_locatable(ax1)
ax2 = divider.append_axes("right", "100%", pad=0.3, sharey=ax1)
fig.add_axes(ax2)
```
