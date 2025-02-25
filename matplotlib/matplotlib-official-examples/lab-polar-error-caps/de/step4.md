# Fehlerbalken erstellen

In diesem Schritt werden wir Fehlerbalken auf unserer polaren Achse erstellen. Wir werden die `errorbar()`-Funktion verwenden, um sowohl Radius- als auch Theta-Fehlerbalken zu erstellen.

```python
ax.errorbar(theta, r, xerr=0.25, yerr=0.1, capsize=7, fmt="o", c="seagreen")
```
