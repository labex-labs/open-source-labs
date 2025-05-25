# Usar PCA para projetar o conjunto de dados

A PCA é usada para projetar o conjunto de dados em um novo espaço que preserva a maior parte de sua variação original.

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)

X_test_pca = pca.fit(X_train).transform(X_test)
```
