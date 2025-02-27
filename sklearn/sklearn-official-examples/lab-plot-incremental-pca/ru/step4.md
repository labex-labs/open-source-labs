# Выполнить PCA

Мы выполним PCA для датасета Iris, инициализировав экземпляр класса PCA и подгоняя его под данные.

```python
pca = PCA(n_components=n_components)
X_pca = pca.fit_transform(X)
```
