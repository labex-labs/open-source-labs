# Visualize Data

Before applying the K-Means Clustering algorithm, let's first visualize the data to get a better understanding of it. We will be using a 3D scatter plot to visualize the data.

```python
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(X[:, 0], X[:, 1], X[:, 2])
ax.set_xlabel("Sepal length")
ax.set_ylabel("Sepal width")
ax.set_zlabel("Petal length")
plt.show()
```


