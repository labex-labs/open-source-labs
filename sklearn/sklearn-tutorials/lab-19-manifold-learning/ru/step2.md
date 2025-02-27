# Locally Linear Embedding (LLE)

Locally Linear Embedding (LLE) - еще один алгоритм обучения многообразия. Он ищет проекцию данных с меньшей размерностью, которая сохраняет расстояния внутри локальных окрестностей.

```python
from sklearn.manifold import LocallyLinearEmbedding

# Создайте экземпляр алгоритма LLE
lle = LocallyLinearEmbedding(n_components=2)

# Примените алгоритм к данным и преобразуйте данные в пространство с меньшей размерностью
X_transformed = lle.fit_transform(X)
```
