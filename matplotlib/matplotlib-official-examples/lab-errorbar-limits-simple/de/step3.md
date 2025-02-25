# Fehlerbalkendiagramm mit beiden Grenzen (Standard) erstellen

In diesem Schritt erstellen wir ein Fehlerbalkendiagramm mit sowohl oberen als auch unteren Grenzen, was das Standardverhalten ist.

```python
plt.errorbar(x, y + 3, yerr=yerr, label='both limits (default)')
```
