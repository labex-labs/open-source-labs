# Выполняем PCA

Теперь, когда мы визуализировали датасет, давайте выполним PCA для него. Для этого мы будем использовать функцию `PCA()` из scikit-learn. Мы установим количество компонентов равным 3, так как мы хотим уменьшить размерность датасета с 4-х размерностей (4 признака) до 3-х размерностей.

```python
pca = decomposition.PCA(n_components=3)
pca.fit(X)
X = pca.transform(X)
```
