# Plot von Kreuzmustern ohne Farbe mit einer Legende

In diesem Schritt werden wir einen Plot von Kreuzmustern ohne Farbe erstellen und eine Legende hinzufügen. Wir werden die `contour`-Funktion verwenden, um die Konturlinien zu erstellen und die `contourf`-Funktion, um die Kreuzmuster ohne Farbe anzugeben.

```python
fig2, ax2 = plt.subplots()
n_levels = 6
ax2.contour(x, y, z, n_levels, colors='black', linestyles='-')
cs = ax2.contourf(x, y, z, n_levels, colors='none',
                  hatches=['.', '/', '\\', None, '\\\\', '*'],
                  extend='lower')

# create a legend for the contour set
artists, labels = cs.legend_elements(str_format='{:2.1f}'.format)
ax2.legend(artists, labels, handleheight=2, framealpha=1)
```
