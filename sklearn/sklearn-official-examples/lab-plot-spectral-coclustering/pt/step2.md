# Gerar um conjunto de dados

Geramos um conjunto de dados com forma (300, 300) contendo 5 biclusters e ruído de 5 usando a função `make_biclusters`.

```python
data, rows, columns = make_biclusters(shape=(300, 300), n_clusters=5, noise=5, shuffle=False, random_state=0)
```
