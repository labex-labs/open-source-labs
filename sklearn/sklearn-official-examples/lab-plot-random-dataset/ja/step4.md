# 2 つの情報提供特徴量、クラスごとに 1 つのクラスタ

2 つの情報提供特徴量とクラスごとに 1 つのクラスタを持つデータセットを作成し、プロットします。

```python
plt.subplot(322)
plt.title("Two informative features, one cluster per class", fontsize="small")
X1, Y1 = make_classification(n_features=2, n_redundant=0, n_informative=2, n_clusters_per_class=1)
plt.scatter(X1[:, 0], X1[:, 1], marker="o", c=Y1, s=25, edgecolor="k")
```
