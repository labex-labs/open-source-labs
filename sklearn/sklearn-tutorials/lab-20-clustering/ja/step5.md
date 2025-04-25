# クラスタを可視化する

k-means アルゴリズムによって形成されたクラスタを可視化しましょう。

```python
# Get the cluster labels for each data point
labels = kmeans.labels_

# Plot the data points with color-coded clusters
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
```
