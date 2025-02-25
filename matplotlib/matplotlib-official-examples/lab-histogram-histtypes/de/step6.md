# Erstellen eines Histogramms mit benutzerdefinierten Bin-Breiten

Wir können ein Histogramm mit benutzerdefinierten und ungleichen Bin-Breiten erstellen, indem wir eine Liste von Bin-Rändern angeben. In diesem Beispiel werden wir ein Histogramm mit ungleichmäßig verteilten Bins erstellen.

```python
bins = [100, 150, 180, 195, 205, 220, 250, 300]
plt.hist(x, bins=bins, density=True, histtype='bar', rwidth=0.8)
plt.show()
```
