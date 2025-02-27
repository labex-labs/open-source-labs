# Генерируем набор данных

Мы генерируем набор данных размером (300, 300) с 5 бикластерами и шумом в размере 5 с использованием функции `make_biclusters`.

```python
data, rows, columns = make_biclusters(shape=(300, 300), n_clusters=5, noise=5, shuffle=False, random_state=0)
```
