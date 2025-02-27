# Выполнить IPCA

Мы выполним IPCA для датасета Iris, инициализировав экземпляр класса IPCA и подгоняя его под данные.

```python
n_components = 2
ipca = IncrementalPCA(n_components=n_components, batch_size=10)
X_ipca = ipca.fit_transform(X)
```
