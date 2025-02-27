# PCA を実行する

次に、データセットに対して主成分分析 (Principal Component Analysis: PCA) を実行し、データ内の最も分散をもたらす属性の組み合わせを特定します。最初の 2 つの主成分上に異なるサンプルをプロットします。

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_r = pca.fit(X).transform(X)

# 各成分によって説明される分散の割合
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
