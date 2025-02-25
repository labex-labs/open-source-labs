# Fehlerbalkendiagramm mit Teilmengen von oberen und unteren Grenzen erstellen

In diesem Schritt erstellen wir ein Fehlerbalkendiagramm mit Teilmengen von oberen und unteren Grenzen.

```python
upperlimits = [True, False] * 5
lowerlimits = [False, True] * 5
plt.errorbar(x, y, yerr=yerr, uplims=upperlimits, lolims=lowerlimits, label='subsets of uplims and lolims')
```
