# Datensatz generieren

Als nächstes generieren wir einen Datensatz, der zwei konzentrische Kreise enthält, mithilfe von `make_circles`. Wir weisen den Datensatz Labels zu, sodass alle Samples unbekannt sind, außer zwei Samples, die jeweils dem äußeren und inneren Kreis angehören.

```python
n_samples = 200
X, y = make_circles(n_samples=n_samples, shuffle=False)
outer, inner = 0, 1
labels = np.full(n_samples, -1.0)
labels[0] = outer
labels[-1] = inner
```
