# Hinzufügen von Grenzen zu beiden Achsen (x und y)

Schließlich werden wir Grenzen zu beiden Achsen (x und y) hinzufügen. Wir werden die Parameter `xlolims` und `xuplims` verwenden, um Grenzen zu den Fehlerbalken der x-Achse hinzuzufügen.

```python
# Plot a series with lower and upper limits in both x & y
# constant x-error with varying y-error
xerr = 0.2
yerr = np.full_like(x, 0.2)
yerr[[3, 6]] = 0.3

# mock up some limits by modifying previous data
xlolims = lolims
xuplims = uplims
lolims = np.zeros_like(x)
uplims = np.zeros_like(x)
lolims[[6]] = True  # nur begrenzt an diesem Index
uplims[[3]] = True  # nur begrenzt an diesem Index

# do the plotting
ax.errorbar(x, y + 2.1, xerr=xerr, yerr=yerr,
            xlolims=xlolims, xuplims=xuplims,
            uplims=uplims, lolims=lolims,
            marker='o', markersize=8, linestyle='none')
```
