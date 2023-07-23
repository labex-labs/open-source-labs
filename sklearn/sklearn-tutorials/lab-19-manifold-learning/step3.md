# t-distributed Stochastic Neighbor Embedding (t-SNE)

t-SNE is a popular manifold learning method that converts affinities of data points to probabilities. It is particularly effective at visualizing high-dimensional data.

```python
from sklearn.manifold import TSNE

# Create an instance of the t-SNE algorithm
tsne = TSNE(n_components=2)

# Fit the algorithm to the data and transform the data to the lower-dimensional space
X_transformed = tsne.fit_transform(X)
```
