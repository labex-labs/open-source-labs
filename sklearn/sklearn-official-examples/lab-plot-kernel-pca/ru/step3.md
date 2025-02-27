# Использование PCA для проекции набора данных

PCA используется для проекции набора данных на новое пространство, которое сохраняет большую часть его исходной вариации.

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)

X_test_pca = pca.fit(X_train).transform(X_test)
```
