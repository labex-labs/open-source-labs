# Визуализируем кластеры

Давайте визуализируем кластеры, которые были сформированы алгоритмом k-средних.

```python
# Get the cluster labels for each data point
labels = kmeans.labels_

# Plot the data points with color-coded clusters
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
```
