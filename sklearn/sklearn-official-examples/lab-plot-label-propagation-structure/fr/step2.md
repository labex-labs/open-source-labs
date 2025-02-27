# Générer un ensemble de données

Ensuite, nous générons un ensemble de données contenant deux cercles concentriques à l'aide de `make_circles`. Nous attribuons des étiquettes à l'ensemble de données de sorte que tous les échantillons soient inconnus, sauf deux échantillons qui appartiennent respectivement aux cercles extérieur et intérieur.

```python
n_samples = 200
X, y = make_circles(n_samples=n_samples, shuffle=False)
outer, inner = 0, 1
labels = np.full(n_samples, -1.0)
labels[0] = outer
labels[-1] = inner
```
