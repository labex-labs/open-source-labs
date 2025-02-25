# Fehlerbalkendiagramm mit nur oberen Grenzen erstellen

In diesem Schritt erstellen wir ein Fehlerbalkendiagramm mit nur oberen Grenzen.

```python
plt.errorbar(x, y + 2, yerr=yerr, uplims=True, label='uplims=True')
```
