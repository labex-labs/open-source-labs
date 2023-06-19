# Perform PCA

Next, we will perform Principal Component Analysis (PCA) on the dataset to identify the combination of attributes that account for the most variance in the data. We will plot the different samples on the first two principal components.

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_r = pca.fit(X).transform(X)

# Percentage of variance explained for each component
print("Explained variance ratio (first two components): %s" % str(pca.explained_variance_ratio_))

plt.figure()
colors = ["navy", "turquoise", "darkorange"]
lw = 2

for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(X_r[y == i, 0], X_r[y == i, 1], color=color, alpha=0.8, lw=lw, label=target_name)

plt.legend(loc="best", shadow=False, scatterpoints=1)
plt.title("PCA of Iris Dataset")
plt.show()
```


