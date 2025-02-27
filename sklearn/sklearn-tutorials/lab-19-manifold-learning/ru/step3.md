# t-distributed Stochastic Neighbor Embedding (t-SNE)

t-SNE - популярный метод обучения многообразия, который преобразует схожести точек данных в вероятности. Он особенно эффективен при визуализации высокомерных данных.

```python
from sklearn.manifold import TSNE

# Создайте экземпляр алгоритма t-SNE
tsne = TSNE(n_components=2)

# Примените алгоритм к данным и преобразуйте данные в пространство с меньшей размерностью
X_transformed = tsne.fit_transform(X)
```
