# Führe PCA durch

Als nächstes werden wir die Principal Component Analysis (PCA) auf dem Datensatz durchführen, um die Kombination von Attributen zu identifizieren, die die meiste Varianz im Datensatz erklären. Wir werden die verschiedenen Samples auf den ersten beiden Hauptkomponenten darstellen.

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_r = pca.fit(X).transform(X)

# Prozentsatz der erklärten Varianz für jede Komponente
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
