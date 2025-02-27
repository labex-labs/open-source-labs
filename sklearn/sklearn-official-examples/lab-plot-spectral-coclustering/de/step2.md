# Erzeugen eines Datensatzes

Wir erzeugen einen Datensatz der Größe (300, 300) mit 5 Biclustern und einem Rauschen von 5 mithilfe der Funktion `make_biclusters`.

```python
data, rows, columns = make_biclusters(shape=(300, 300), n_clusters=5, noise=5, shuffle=False, random_state=0)
```
