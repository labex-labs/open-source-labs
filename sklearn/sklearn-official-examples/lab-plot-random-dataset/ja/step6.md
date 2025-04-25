# 多クラス、2 つの情報提供特徴量、1 つのクラスタ

複数のクラスと 2 つの情報提供特徴量、そして 1 つのクラスタを持つデータセットを作成し、プロットします。

```python
plt.subplot(324)
plt.title("Multi-class, two informative features, one cluster", fontsize="small")
X1, Y1 = make_classification(n_features=2, n_redundant=0, n_informative=2, n_clusters_per_class=1, n_classes=3)
plt.scatter(X1[:, 0], X1[:, 1], marker="o", c=Y1, s=25, edgecolor="k")
```
