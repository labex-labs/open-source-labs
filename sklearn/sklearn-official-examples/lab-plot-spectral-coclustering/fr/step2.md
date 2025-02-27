# Générer un ensemble de données

Nous générons un ensemble de données de forme (300, 300) avec 5 bi-classes et un bruit de 5 à l'aide de la fonction `make_biclusters`.

```python
data, rows, columns = make_biclusters(shape=(300, 300), n_clusters=5, noise=5, shuffle=False, random_state=0)
```
