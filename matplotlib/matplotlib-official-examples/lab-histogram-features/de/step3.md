# Erstellen eines Histogramms

In diesem Schritt werden wir ein Histogramm mit matplotlib erstellen. Wir werden die Anzahl der Bins auf 50 setzen und den Dichteparameter aktivieren, um die Höhen der Bins zu normalisieren, sodass das Integral des Histogramms 1 ist.

```python
num_bins = 50
fig, ax = plt.subplots()
n, bins, patches = ax.hist(x, num_bins, density=True)
```
