# Fehlerbalkendiagramm mit sowohl oberen als auch unteren Grenzen erstellen

In diesem Schritt erstellen wir ein Fehlerbalkendiagramm mit sowohl oberen als auch unteren Grenzen.

```python
plt.errorbar(x, y + 1, yerr=yerr, uplims=True, lolims=True, label='uplims=True, lolims=True')
```
